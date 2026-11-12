"""
System Design Story Lab - Part 3: Cases 10 to 13
Covers:
  - Case 10: HLD Case Study III — Social News Feed Fan-Out & Notifications
  - Case 11: HLD Case Study IV — Search Typeahead, Video Streaming & Cloud Drive
  - Case 12: LLD Foundations — SOLID Principles, Design Patterns & Concurrency
  - Case 13: LLD Machine Coding — Parking Lot Code Lab, BookMyShow, Splitwise, Elevator
"""

SD_CASES_PART3 = {
    "10": {
        "title": "HLD Case Study III: Social News Feed & Push Notifications",
        "episodes": [
            {
                "title": "Module 1: Fan-Out on Write (Push) vs Fan-Out on Read (Pull)",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The 80-Million-Follower Feed Queue Meltdown",
                        "content": "A social app used **Fan-Out on Write** for everyone: every new post pushed its `post_id` into EVERY follower's pre-computed Redis feed cache immediately. It ran effortlessly for ordinary users with `200` friends—until a megastar with **80 million followers** posted a selfie! A single HTTP `POST` spawned **80,000,000 Redis `LPUSH` tasks**, clogging Kafka workers for 18 minutes and delaying posts from normal users!\n\n> [!IMPORTANT]\n> **Hybrid Fan-Out Rule:** Push on write for regular users (`< 10k` followers); **Pull on read** at timeline merge time ONLY for mega-celebrities (`> 10k` followers)!"
                    },
                    {
                        "type": "comparison_table",
                        "title": "News Feed Fan-Out Architecture Trade-offs",
                        "headers": ["Model", "Read Path Speed", "Write Amplification", "Weakness"],
                        "rows": [
                            ["Fan-Out on Write (Push)", "Ultra-fast O(1) Redis LRANGE", "O(followers) writes per post", "Hot celebrity fan-out stalls queues & wastes RAM on inactive followers"],
                            ["Fan-Out on Read (Pull)", "Slow (queries K followed timelines + K-way merge!)", "O(1) single DB insert", "Sluggish home-feed loads if user follows 2,000 people"],
                            ["Hybrid Push + Pull (Instagram / X)", "Fast O(1) Redis + merge <50 celebs", "Capped per write; celebs excluded", "Slightly more complex read hydration merger"]
                        ]
                    }
                ]
            },
            {
                "title": "Module 2: Hybrid Timeline Pipeline & Notification Worker Mesh",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Slim Timeline Caches & Multi-Channel Notification Mesh",
                        "content": "- **Feed Store Optimization:** Redis timeline lists store ONLY compact tuples `(post_id, author_id, score)` (`~24 bytes/entry`, capped at top `500` posts per active user!), NOT bloated full media JSON—and skip inactive users (`last_seen > 14 days`). At read time, the **Hydration Service** batches `MGET post:{ids}` + user avatars + privacy filters!\n- **Push Notification Pipeline (APNs / FCM / SMS / Email):** Decouple via Kafka **Priority Topics** (`OTP_Critical` separated from `Marketing_Bulk`), enforce per-user **rate limits + timezone Quiet Hours**, and route permanent device-token errors (`HTTP 410 Unregistered`) out of retries into Dead-Letter / Token Cleanup queues!",
                        "technical_explanation": "**Cursor Pagination Over Offset Pagination (`LIMIT 20 OFFSET 100`):** Never use SQL `OFFSET` on shifting live feeds! Two new tweets arriving while scrolling cause duplicates on Page 2. Use deterministic **`cursor = base64(last_post_id)`** keyset pagination!"
                    },
                    {
                        "type": "visual",
                        "title": "Hybrid Social Feed Write & Read Merge Pipeline",
                        "code": """flowchart TD
    P["User Publishes Post"] --> DB["Save Post in Sharded Store"]
    P --> MQ["Kafka Post-Created Topic"]
    MQ --> CHK{"Author Followers > 10k?"}
    CHK -- "No (Normal User)" --> PushW["Fan-Out Workers -> LPUSH into active followers Redis Feed"]
    CHK -- "Yes (Celebrity)" --> Skip["Skip Push! Keep in Celebrity Posts Cache"]
    Reader["Reader Requests Home Feed"] --> Merge["Merge Redis Prebuilt Feed + Pull Followed Celebrities + Hydrate Objects"]"""
                    }
                ]
            },
            {
                "title": "Module 3: Celebrity Fan-Out Math & Privacy Deletion Challenges",
                "blocks": [
                    {
                        "type": "calculation_challenge",
                        "title": "Redis Timeline Memory Footprint for Slim IDs vs Full Objects",
                        "question": "Assume **100 million active users** each maintain a cached Redis home feed of the latest **500 post IDs**, where storing slim ID tuples consumes **16 bytes per entry** (vs `2,000` bytes for hydrated full JSON). How many **GB** of total Redis RAM does storing ONLY the 16-byte IDs across 100M users require? (`100M * 500 * 16 bytes`, using `1 GB = 10^9 bytes` decimal.)",
                        "answer": "800",
                        "alternatives": ["800", "800 GB"],
                        "step_by_step": "$100 \\times 10^6\\text{ users} \\times 500\\text{ entries} \\times 16\\text{ bytes} = 800 \\times 10^9\\text{ bytes} = \\mathbf{800\\text{ GB}}$ total RAM across Redis Cluster (tiny compared to **100 TB** if you stored full JSON payloads per timeline!)."
                    },
                    {
                        "type": "scenario_decision",
                        "title": "Enforcing Instant Post Deletes & Privacy Changes Without Rescanning 500k Feeds",
                        "scenario": "User X accidentally shares a private photo to 50,000 followers (already fanned out into Redis timeline lists) and hits **Delete Post** 3 seconds later.",
                        "question": "How do you ensure NO follower sees the deleted photo immediately on feed refresh without O(N) timeline scans?",
                        "options": [
                            "Delete/mark tombstoned in the canonical Post Cache/DB; during read-time Hydration, missing or deleted `post_id`s fail hydration cleanly and are lazily dropped from the rendered feed!",
                            "Flush the entire global Redis Cluster on every deleted post",
                            "Scan and rewrite all 100M user lists synchronously inside the HTTP DELETE call",
                            "Require all followers to clear browser storage manually"
                        ],
                        "answer": "Delete/mark tombstoned in the canonical Post Cache/DB; during read-time Hydration, missing or deleted `post_id`s fail hydration cleanly and are lazily dropped from the rendered feed!",
                        "rationale": "Because timelines hold only `post_id` pointers, invalidating/deleting the single `post:{id}` cache entry ensures every subsequent Feed Hydration check automatically drops that ID in $O(1)$!"
                    }
                ]
            },
            {
                "title": "Module 4: Spot the Synchronous Fan-Out Antipattern",
                "blocks": [
                    {
                        "type": "diagram_critique",
                        "title": "Diagnose the Broken Publish Flow",
                        "scenario": "Publishing a post currently executes every follower cache insert synchronously inside the API request before returning `201 Created`.",
                        "code": """flowchart LR
    U["Client POST /post"] --> API["Web API Thread (30s HTTP Timeout)"]
    API -->|Synchronously loops 50k followers!| R["50,000 Sequential Redis LPUSH Calls"]
    R -->|Timeout after 30s!| U504["504 Gateway Timeout! Client retries -> DUPLICATE POSTS!"]""",
                        "question": "What critical flaw in this workflow causes `504 Gateway Timeouts` AND duplicate posts on retry?",
                        "options": [
                            "Executing O(followers) fan-out work synchronously inside the HTTP POST thread instead of persisting once + returning `201` + offloading fan-out asynchronously to Kafka workers",
                            "Redis `LPUSH` is read-only and forbids list appends",
                            "HTTP `POST` requests cannot return `201 Created`",
                            "Web API servers require at least 60-minute HTTP timeouts"
                        ],
                        "answer": "Executing O(followers) fan-out work synchronously inside the HTTP POST thread instead of persisting once + returning `201` + offloading fan-out asynchronously to Kafka workers",
                        "remedy": "Persist the post once to the Posts DB (with client idempotency key), enqueue `{post_id, author_id}` onto Kafka, and immediately ACK `201 Created` in `< 25 ms` while async worker fleets fan out!"
                    },
                    {
                        "type": "fill_in_the_blank",
                        "title": "Safe Pagination Primitive",
                        "question": "Instead of SQL `OFFSET` pagination which skips or duplicates posts whenever new items prepend to a live feed, production timelines use _____ pagination (e.g., `WHERE post_id < last_seen_id LIMIT 20`).",
                        "answer": "cursor",
                        "alternatives": ["cursor", "keyset", "cursor-based", "seek"],
                        "explanation": "**Cursor / Keyset Pagination** anchors strictly against the last rendered `post_id` / score, remaining fast ($O(\\log N)$ index seek, never scanning & discarding millions of offset rows) and immune to real-time prepends!"
                    }
                ]
            }
        ]
    },
    "11": {
        "title": "HLD Case Study IV: Search Typeahead, Video & Cloud Drive",
        "episodes": [
            {
                "title": "Module 1: Search Autocomplete (Typeahead) — Precomputed Top-K Trie",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "How Google Search Returns Instant Suggestions on Every Keystroke",
                        "content": "Naively traversing an entire subtree below `'sys'` at query time and sorting 5 million query strings breaks a **50 ms SLA**!\n\n- **Core Optimization — Precompute `top_k[5..10]` Inside Every Trie Node:** Each Trie prefix node caches a small immutable list of the **Top 5–10 hottest searches** starting with that prefix (e.g., node `'sy'` stores `[('system design', 9.2M), ('sync', 3.1M), ...]`). Query lookup drops to **$O(\\text{prefix len})$** (~5 pointer hops = `< 2 ms` at CDN/Redis edge!).\n- **Asynchronous Offline Rebuild Pipeline:** Keystrokes log sampled search frequencies (`1-in-100`) to Kafka -> Spark/Flink hourly MapReduce aggregates weights (with exponential decay so trending topics rise!) -> atomic blue-green swap of Trie snapshot workers without locking live reads!",
                        "technical_explanation": "**Shard Tries by First 1–2 Characters (`a..z`):** Shard Trie servers by prefix prefix (`aa–am`, `an–az`, ...) weighed by actual query skew (`s*` queries >> `x*` queries!) so one ZooKeeper-tracked shard handles hot prefixes cleanly."
                    },
                    {
                        "type": "visual",
                        "title": "Real-Time Typeahead Query Path vs Async Trie Builder",
                        "code": """flowchart LR
    K["Keystroke 'sys'"] --> CDN["Edge Cache / Trie Read Tier"]
    CDN -->|"O(3) Lookup: Precomputed Top-10"| Resp["Instant Suggestions < 15ms"]
    SearchLog["Sampled Search Logs"] --> Kafka --> Spark["Hourly Aggregator (Decaying Frequency)"] --> Snap["Rebuild & Hot-Swap Trie Snapshot"]"""
                    }
                ]
            },
            {
                "title": "Module 2: Adaptive Video Streaming (YouTube/Netflix HLS/DASH)",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Chunked Upload, Transcoding DAG & Adaptive Bitrate Streaming",
                        "content": "Streaming a single monolithic 4 GB `.mp4` over HTTP freezes whenever mobile LTE bandwidth dips.\n\n1. **Direct-to-Object-Store Multipart Upload:** Clients request **Pre-Signed S3 URLs**, uploading 5 MB parts directly in parallel (never funneling multi-GB video streams through API gateway containers!).\n2. **Encoding DAG Pipeline:** Splits video by **GOP (Group of Pictures)** boundaries into **2–5 second chunks**, parallelizing encoding workers across codecs (`H.264 / AV1`) and resolutions (`360p, 720p, 1080p, 4K`).\n3. **HLS (`.m3u8`) / DASH Delivery via CDN:** Client fetches a tiny manifest playlist indexing `chunk_001..N` per bitrate, dynamically stepping smoothly between `1080p <-> 480p` mid-playback as cellular signal changes!",
                        "technical_explanation": "**OpenConnect / Edge Video Appliances:** Netflix places pre-populated flash-storage servers **directly inside ISP datacenters** overnight during off-peak hours (`OpenConnect`) so 95%+ of evening 4K video bytes never even traverse internet transit peering links!"
                    }
                ]
            },
            {
                "title": "Module 3: Cloud Drive (Dropbox / Google Drive) Chunked Delta Sync",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Separating Control Metadata From Deduplicated Immutable Blocks",
                        "content": "- **Control Plane (`BlockMetadata + FileRevision` RDBMS):** ACID-protected folder tree, permissions ACL, optimistic `rev_id` conflict forks (`conflicted copy`), and ordered chunk manifest `[sha256_c1, sha256_c2, ...]`.\n- **Data Plane (`S3 / Content-Addressable Block Store`):** Client splits every file into deterministic **4 MB chunks** (or content-defined **Rabin Fingerprinting** chunks so inserting 1 byte at offset `0` doesn't shift all later chunk boundaries!) and hashes each with **SHA-256**.\n- **Delta Sync + Deduplication:** Before uploading `sha256_c7`, client asks API which hashes already exist globally in S3—uploading **ONLY modified chunks** (`1 chunk` vs `500 MB`) AND storing identical company PDFs ONCE globally!",
                        "technical_explanation": "**Notification Service (Long-Poll / WebSocket):** Idle desktop sync clients avoid hammering servers every second; a lightweight Notification Service nudges ONLY active subscribed folder clients when another device commits a new `rev_id`."
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Bandwidth Saved by 4 MB Chunk Delta Sync",
                        "question": "An engineer edits a single 20 KB section near the end of an **800 MB** raw design file synced across a team of **10 laptops** using **4 MB fixed-size chunk delta sync** (meaning ONLY the **1 modified 4 MB chunk** needs upload + download per synced teammate, ignoring metadata overhead). Wait: **1 modified 4 MB chunk** must be uploaded once AND downloaded by the 9 teammates? Let's keep the question crisp: comparing **Whole-File Sync** (`800 MB` upload) vs **4 MB Chunk Delta Sync** (`4 MB` upload) for **only the single uploader's egress**—how many **times smaller** (`800 / 4`) is the uploader's upload bandwidth?",
                        "answer": "200",
                        "alternatives": ["200", "200x"],
                        "step_by_step": "Uploader sends only the 1 dirty chunk (`4 MB`) instead of the entire `800 MB` binary: $800\\text{ MB} \\div 4\\text{ MB} = \\mathbf{200\\times}$ bandwidth reduction (a 99.5% savings!)."
                    }
                ]
            },
            {
                "title": "Module 4: Media Pipeline Trade-offs & Comparison Table",
                "blocks": [
                    {
                        "type": "comparison_table",
                        "title": "Monolithic File Upload vs Chunked Pre-Signed Architecture",
                        "headers": ["Dimension", "Monolithic API Proxy Upload", "Chunked Pre-Signed S3 Pipeline"],
                        "rows": [
                            ["Resumability on 4G Drop", "Re-upload 100% from byte 0!", "Resume ONLY missing chunk index cleanly"],
                            ["Backend API Load", "Saturates app server RAM/NICs", "Zero media bytes touch app servers!"],
                            ["Edit Bandwidth (1 KB edit)", "Re-upload entire 500 MB file", "Upload ONLY 1 changed 4 MB chunk"]
                        ]
                    },
                    {
                        "type": "scenario_decision",
                        "title": "Eliminating Video Startup Buffering for Mobile Commuters",
                        "scenario": "Users opening your short-video feed wait `4.5 seconds` for buffering because the player tries to download full 1080p MP4 headers + first 30 seconds before decoding frame 1.",
                        "question": "Which combination minimizes Time-To-First-Frame (TTFF) under `300 ms` across variable mobile bandwidth?",
                        "options": [
                            "HLS/DASH segmented 2s chunks with Adaptive Bitrate (start immediately on fast initial low/mid bitrate chunk via CDN edge) + prefetching top-2 manifest chunks",
                            "Disable compression and stream raw uncompressed 4K AVI bytes over TCP",
                            "Wait until the entire 10-minute video downloads to IndexedDB before playing",
                            "Serve video frames inside SQLite BLOB polling queries"
                        ],
                        "answer": "HLS/DASH segmented 2s chunks with Adaptive Bitrate (start immediately on fast initial low/mid bitrate chunk via CDN edge) + prefetching top-2 manifest chunks",
                        "rationale": "Starting playback on a tiny ~200 KB edge-cached 2-second chunk starts frames within milliseconds, then ABR smoothly upgrades to 1080p as throughput stabilizes!"
                    }
                ]
            }
        ]
    },
    "12": {
        "title": "LLD Foundations: SOLID Principles, Patterns & Concurrency",
        "episodes": [
            {
                "title": "Module 1: SOLID Architecture Under Production Maintenance",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The 1,200-Line Checkout Function That Broke Production",
                        "content": "Every time Marketing added a new payment method (`CreditCard`, `UPI`, `Wallet`, `BNPL`), developers modified the **same central 1,200-line `process_payment()` `if/elif` file** handling fraud checks, DB commits, gateway SDKs, AND PDF receipts! One typo inside the `Wallet` tax block crashed `CreditCard` checkouts worldwide!\n\n> [!IMPORTANT]\n> **SOLID Mandate:** Decouple change axes! Separate tax logic, gateway adapters, and receipt persistence so adding `ApplePay` adds ONE new clean class WITHOUT touching tested existing paths!"
                    },
                    {
                        "type": "concept",
                        "title": "All 5 SOLID Principles Distilled for LLD Interviews",
                        "content": "1. **S — Single Responsibility Principle (SRP):** A class has **one reason to change** (never mix `OrderRepository` SQL + `InvoiceEmailer` SMTP + `DiscountCalculator` inside `Order`).\n2. **O — Open/Closed Principle (OCP):** **Open for extension, closed for modification** — replace giant `if type == 'CARD' elif type == 'UPI'` switches with a **`PaymentStrategy` interface** + polymorphic implementations!\n3. **L — Liskov Substitution Principle (LSP):** Subtypes must preserve ALL behavioral invariants of their base type (`Square` inheriting `Rectangle.setWidth/setHeight` violates expectation if callers assume height stays independent!).\n4. **I — Interface Segregation Principle (ISP):** Split bloated `'God Interfaces'` (`Worker.work() + eat()`) into cohesive interfaces (`Workable`, `Feedable`) so a `Robot` doesn't implement empty `eat()` methods.\n5. **D — Dependency Inversion Principle (DIP):** High-level business policy (`CheckoutService`) depends on an abstraction (`PaymentGateway` ABC/interface), NOT concrete `StripeClient`—enabling instant mocking and swaps!",
                        "technical_explanation": "**Favor Composition over Deep Inheritance:** Rather than building fragile 5-level hierarchies (`FlyingSwimmingDuck`), inject small modular behaviors (`FlyBehavior`, `QuackBehavior`) via **Composition + Strategy**!"
                    }
                ]
            },
            {
                "title": "Module 2: Essential Design Patterns (Strategy, Factory, Observer, Singleton)",
                "blocks": [
                    {
                        "type": "comparison_table",
                        "title": "Top Production Design Patterns & Problems Solved",
                        "headers": ["Pattern", "Category", "Concrete System Problem It Solves"],
                        "rows": [
                            ["Strategy", "Behavioral", "Swappable pricing, Surge rules, Sort/Eviction (LRU/LFU) algorithms at runtime"],
                            ["Factory / Abstract Factory", "Creational", "Decouple object instantiation (`createNotification('SMS'|'PUSH')`) from callers"],
                            ["Observer (Pub-Sub Event Bus)", "Behavioral", "Broadcast `OrderPlaced` events cleanly to Inventory, Analytics & Email listeners"],
                            ["Decorator", "Structural", "Stack runtime wrappers dynamically (Auth -> Logging -> Compression stream wrappers)"],
                            ["Singleton (Thread-Safe)", "Creational", "Ensure 1 shared Config/ConnectionPool with `Lock` / `std::call_once`"]
                        ]
                    },
                    {
                        "type": "concept",
                        "title": "Concurrency Primitives in LLD: Optimistic CAS vs Pessimistic Locks",
                        "content": "Low-level classes shared across worker threads MUST guard invariants:\n\n- **Pessimistic Locking (`threading.Lock` / `std::mutex` / `SELECT ... FOR UPDATE`):** Acquires exclusive lock BEFORE modifying shared state. Safe under high contention; risk of **deadlocks** unless multiple locks are ALWAYS acquired in **canonical ascending order** (`min(a,b)` -> `max(a,b)`)!\n- **Optimistic Concurrency Control (`version` CAS column / `atomic` Compare-And-Swap):** Reads row with `version = 7`, updates `WHERE id = X AND version = 7 SET version = 8`. If `rows_affected == 0`, retry! High read concurrency without holding idle locks!"
                    }
                ]
            },
            {
                "title": "Module 3: Spot the SOLID Violation & Concurrency Race Bug",
                "blocks": [
                    {
                        "type": "debugger",
                        "title": "Bug Hunt: Classic Liskov Substitution Principle (LSP) Trap",
                        "code": """class Rectangle:
    def set_width(self, w): self.w = w
    def set_height(self, h): self.h = h
    def area(self): return self.w * self.h

class Square(Rectangle):
    def set_width(self, w): self.w = self.h = w
    def set_height(self, h): self.w = self.h = h

def test_rect(r: Rectangle):
    r.set_width(5)
    r.set_height(4)
    assert r.area() == 20  # CRASHES when passed a Square (returns 16)!""",
                        "question": "Why does inheriting `Square` from mutable `Rectangle` violate SOLID design?",
                        "options": [
                            "It violates Liskov Substitution (LSP): overriding `set_height` to mutate `w` breaks `Rectangle`'s post-condition that width and height are independent!",
                            "Python classes cannot inherit methods named `area`",
                            "It violates Singleton pattern because there are two instances",
                            "It violates Database Sharding rules"
                        ],
                        "answer": "It violates Liskov Substitution (LSP): overriding `set_height` to mutate `w` breaks `Rectangle`'s post-condition that width and height are independent!",
                        "explanation": "In OOP LLD, geometric subtypes don't map blindly when mutable setters differ! Either model immutable `Shape` (`area()`) + independent `Rectangle` and `Square` classes, or drop conflicting setters."
                    },
                    {
                        "type": "scenario_decision",
                        "title": "Preventing Deadlocks in Parallel Bank-Account Transfers",
                        "scenario": "Thread 1 calls `transfer(accA -> accB, $50)` locking `accA` then trying to lock `accB`; concurrently Thread 2 calls `transfer(accB -> accA, $20)` locking `accB` then trying to lock `accA`. Both freeze forever!",
                        "question": "What minimal LLD lock-acquisition invariant mathematically eliminates cyclical deadlocks cleanly without coarse global locks?",
                        "options": [
                            "Global Lock Ordering: ALWAYS acquire locks sorted by canonical `min(from.id, to.id)` first, then `max(from.id, to.id)`!",
                            "Wrap each individual integer subtraction in two separate unlocked lines",
                            "Disable locks and rely on `try/except`",
                            "Increase thread sleep timeout to 60 seconds before retry"
                        ],
                        "answer": "Global Lock Ordering: ALWAYS acquire locks sorted by canonical `min(from.id, to.id)` first, then `max(from.id, to.id)`!",
                        "rationale": "Sorting lock acquisition order (`accA.id < accB.id`) breaks Coffman's **Circular Wait** necessary condition cleanly while keeping unrelated account pairs fully concurrent!"
                    }
                ]
            },
            {
                "title": "Module 4: Event-Driven Observer Bus & Thread Safety Drill",
                "blocks": [
                    {
                        "type": "fill_in_the_blank",
                        "title": "Double-Checked / Safe Lazy Initialization",
                        "question": "To replace giant `if/elif` chains checking string types when calculating dynamic Uber/Lyft trip pricing (Normal vs Surge vs Promo Discount), LLD engineers apply the _____ behavioral design pattern.",
                        "answer": "Strategy",
                        "alternatives": ["Strategy", "strategy", "Strategy Pattern", "strategy pattern"],
                        "explanation": "The **Strategy Pattern** encapsulates each interchangeable pricing formula behind a shared `PricingStrategy` interface injected into `TripFareCalculator`!"
                    },
                    {
                        "type": "concept",
                        "title": "Clean LLD Checklist for Interviews",
                        "content": "Before writing a single class in any LLD interview:\n1. List **Actors & Core Use Cases** (5 bullets).\n2. Sketch **Clean Domain Entities & Enums** (`VehicleType`, `TicketStatus`, `SpotSize`).\n3. Apply **Interfaces/Patterns** only where variation exists (`AllocationStrategy`, `PricingStrategy`).\n4. State explicitly **where concurrency/locks attach** (e.g., per-lot lock or spot CAS during checkout!)."
                    }
                ]
            }
        ]
    },
    "13": {
        "title": "LLD Machine Coding: Parking Lot, BookMyShow, Splitwise & Elevator",
        "episodes": [
            {
                "title": "Module 1: Anatomy of Clean Machine Coding Architecture",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "The 4 Pillars of Every Flagship LLD Interview Design",
                        "content": "Strong machine coding solutions balance extensibility, clean OOP boundaries, and zero race conditions:\n\n1. **Rich Domain Model + Value Objects:** Express `VehicleType.MOTORCYCLE/CAR/BUS` and `SpotSize.COMPACT/REGULAR/LARGE` cleanly with clear compatibility rules rather than fragile magic strings.\n2. **Swappable Pluggable Strategies:** Inject `SpotAssignmentStrategy` (`NearestEntrance`, `LowestFloor`) and `PricingStrategy` (`HourlyFlat`, `WeekendTiered`) via constructor.\n3. **Repository / Registry Layer:** Keep domain objects cohesive (`Ticket`, `Spot`, `Floor`), separate from coordination (`ParkingLotManager`).\n4. **Concurrency Boundaries:** Protect check-and-reserve spot transitions atomically so two entrance gates NEVER assign the same spot `#42`!",
                        "technical_explanation": "**Avoid 'Anemic Domain Models' vs 'God Managers':** Put spot-compatibility rules (`spot.can_fit(vehicle_type)`) cleanly on `ParkingSpot` or strategy policies rather than scattering giant nested dicts everywhere."
                    },
                    {
                        "type": "visual",
                        "title": "Multi-Floor Parking Lot Class & Flow Architecture",
                        "code": """flowchart TD
    PL["ParkingLot (Singleton/Facade)"] --> Strat["SpotAllocationStrategy"]
    PL --> Pricing["HourlyPricingStrategy"]
    PL --> Fl["Floor 1..F"]
    Fl --> Sp["ParkingSpot (id, size, is_occupied)"]
    PL --> Tk["Ticket (ticket_id, vehicle_plate, spot, entry_time)"]"""
                    }
                ]
            },
            {
                "title": "Module 2: BookMyShow Locks, Splitwise Debt Graph & Elevator SCAN",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Three High-Frequency LLD System Blueprints",
                        "content": "### 1. BookMyShow (Seat Concurrency + Soft Holds)\n- Maintain three seat states: **`AVAILABLE -> LOCKED (with TTL + lock_owner) -> BOOKED`**.\n- Selecting seats triggers an atomic **Redis Distributed Lock (`SET seat:show12:J14 userA NX PX 300000`)** OR DB conditional update (`UPDATE show_seat SET status='LOCKED', lock_until=now+5m WHERE status='AVAILABLE' AND version=v`). Only after Payment Webhook succeeds does status commit **`BOOKED`**; expired locks release cleanly via TTL!\n\n### 2. Splitwise (Minimize Cash Flow Algorithm)\n- Never store a raw quadratic `O(N^2)` graph of everyone's isolated IOUs if simplification is enabled! Compute each friend's **net balance** (`sum_paid - sum_owed`, total always sums to `0`). Place positive creditors in a Max-Heap and negative debtors in a Min-Heap, greedily settling `min(credit, |debt|)` per step—reducing 50 messy expenses down to at most **$N - 1$ total transfers**!\n\n### 3. Elevator Controller (`LOOK / SCAN` Scheduling)\n- Mimics disk-head scheduling: sweep UP serving all `UP` requests ahead, reverse smoothly at the highest pending request (`LOOK`) to sweep DOWN serving `DOWN` requests, eliminating passenger starvation!",
                        "technical_explanation": "**Multi-Elevator Dispatch Strategy:** Assign an incoming hall call `(floor, direction)` to the car minimizing estimated stops: strongly prefer an elevator **already moving toward `floor` in matching direction**, else nearest `IDLE` elevator, else turnaround cost!"
                    }
                ]
            },
            {
                "title": "Module 3: Concurrency & Algorithmic LLD Decisions",
                "blocks": [
                    {
                        "type": "scenario_decision",
                        "title": "Two Users Click Cinema Seat J14 at the Exact Same Millisecond",
                        "scenario": "On IMAX opening night, Alice and Bob both tap Seat `J14` and click `'Proceed to Payment'`. Payment takes `8–45 seconds` outside your system via an external 3D-Secure bank OTP flow.",
                        "question": "How should BookMyShow LLD + HLD coordinate Seat `J14` cleanly so neither person pays for an already-sold seat AND abandoned checkouts don't permanently block the seat?",
                        "options": [
                            "Acquire an atomic conditional Soft Hold (`LOCKED` with `version` CAS + 5–10 minute Redis/DB TTL); confirm to `BOOKED` inside a serializable DB transaction upon payment callback, releasing automatically on TTL expiration",
                            "Hold a blocking OS mutex / DB row lock open across the entire 45-second external bank OTP HTTP session",
                            "Allow both Alice and Bob to pay `BOOKED`, then refund the loser manually 3 days later",
                            "Pick the winner purely by alphabetical first name"
                        ],
                        "answer": "Acquire an atomic conditional Soft Hold (`LOCKED` with `version` CAS + 5–10 minute Redis/DB TTL); confirm to `BOOKED` inside a serializable DB transaction upon payment callback, releasing automatically on TTL expiration",
                        "rationale": "Holding physical DB row locks across external human bank flows crashes connection pools; an explicit **`LOCKED` soft-hold with automatic TTL expiry + optimistic `version`** keeps concurrency tiny and guarantees strict single ownership!"
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Splitwise Minimum Transactions Bound",
                        "question": "Three roommates have net balances after a weekend trip: **Alice `+60`**, **Bob `-20`**, **Charlie `-40`** (`+60 - 20 - 40 = 0`). After simplifying group balances greedily, what is the **minimum number of bank transfers** required to settle everyone completely to `0`?",
                        "answer": "2",
                        "alternatives": ["2", "2 transfers"],
                        "step_by_step": "Notice total debts settle with **2 transfers** ($N - 1 = 3 - 1 = \\mathbf{2}$): Bob pays Alice `$20` and Charlie pays Alice `$40` -> everyone lands at `0`!"
                    }
                ]
            },
            {
                "title": "Module 4: Code Lab — Implement Multi-Floor Parking Lot Allocator & Billing Engine",
                "blocks": [
                    {
                        "type": "code_lab",
                        "language": "python",
                        "title": "Build a Thread-Safe Multi-Floor Parking Lot Allocation & Billing System",
                        "instruction": "Implement the core OOP Domain Engine for a Multi-Floor **Parking Lot (`class ParkingLot:`)** supporting compact-to-large vehicle up-fitting!\n\nRules & Sizing Order (`MOTORCYCLE < CAR < BUS` matching `SMALL(0) < MEDIUM(1) < LARGE(2)`):\n- A **MOTORCYCLE (0)** can fit in **SMALL(0), MEDIUM(1), or LARGE(2)** spots (preferring smallest available fit first!).\n- A **CAR (1)** can fit in **MEDIUM(1) or LARGE(2)** spots.\n- A **BUS (2)** fits ONLY in **LARGE(2)** spots.\n- Always pick the **lowest floor index first**, then **smallest fitting spot size**, then **lowest spot ID**.\n\nImplement methods on `ParkingLot`:\n- `park(plate: str, vtype: str, entry_hour: int) -> str | None`: Assign optimal free spot cleanly, create ticket, return `ticket_id` (or `None` if lot cannot accommodate or plate already parked).\n- `unpark(ticket_id: str, exit_hour: int) -> float`: Free spot, compute fee (`max(1, exit_hour - entry_hour) * rate[vtype]` where `MOTORCYCLE: 10, CAR: 20, BUS: 50`), delete active ticket, return fee.",
                        "starter_code": "SIZE_ORDER = {'SMALL': 0, 'MEDIUM': 1, 'LARGE': 2}\nVEH_MIN_SIZE = {'MOTORCYCLE': 0, 'CAR': 1, 'BUS': 2}\nHOURLY_RATES = {'MOTORCYCLE': 10.0, 'CAR': 20.0, 'BUS': 50.0}\n\nclass ParkingSpot:\n    def __init__(self, floor: int, spot_id: str, size: str):\n        self.floor = floor\n        self.spot_id = spot_id\n        self.size = size\n        self.occupied = False\n\nclass ParkingLot:\n    def __init__(self, spots: list):\n        self.spots = spots\n        self.active_tickets = {}\n        self.parked_plates = set()\n        self._seq = 0\n\n    def park(self, plate: str, vtype: str, entry_hour: int):\n        # TODO: find best available spot (smallest fitting size, lowest floor, lowest spot_id)\n        return None\n\n    def unpark(self, ticket_id: str, exit_hour: int) -> float:\n        # TODO: free spot & calculate billable fee\n        return 0.0\n",
                        "solution_code": "SIZE_ORDER = {'SMALL': 0, 'MEDIUM': 1, 'LARGE': 2}\nVEH_MIN_SIZE = {'MOTORCYCLE': 0, 'CAR': 1, 'BUS': 2}\nHOURLY_RATES = {'MOTORCYCLE': 10.0, 'CAR': 20.0, 'BUS': 50.0}\n\nclass ParkingSpot:\n    def __init__(self, floor: int, spot_id: str, size: str):\n        self.floor = floor\n        self.spot_id = spot_id\n        self.size = size\n        self.occupied = False\n\nclass ParkingLot:\n    def __init__(self, spots: list):\n        self.spots = spots\n        self.active_tickets = {}\n        self.parked_plates = set()\n        self._seq = 0\n\n    def park(self, plate: str, vtype: str, entry_hour: int):\n        if plate in self.parked_plates or vtype not in VEH_MIN_SIZE:\n            return None\n        req = VEH_MIN_SIZE[vtype]\n        candidates = [\n            sp for sp in self.spots\n            if not sp.occupied and SIZE_ORDER[sp.size] >= req\n        ]\n        if not candidates:\n            return None\n        # Prefer smallest fitting size -> lowest floor -> lowest spot_id\n        candidates.sort(key=lambda sp: (SIZE_ORDER[sp.size], sp.floor, sp.spot_id))\n        chosen = candidates[0]\n        chosen.occupied = True\n        self._seq += 1\n        tid = f'TKT-{self._seq:04d}'\n        self.parked_plates.add(plate)\n        self.active_tickets[tid] = (plate, vtype, entry_hour, chosen)\n        return tid\n\n    def unpark(self, ticket_id: str, exit_hour: int) -> float:\n        if ticket_id not in self.active_tickets:\n            raise KeyError('Invalid ticket_id')\n        plate, vtype, entry_hour, spot = self.active_tickets.pop(ticket_id)\n        self.parked_plates.remove(plate)\n        spot.occupied = False\n        hours = max(1, exit_hour - entry_hour)\n        return float(hours) * HOURLY_RATES[vtype]\n",
                        "test_code": "spots = [\n    ParkingSpot(1, 'F1-M1', 'MEDIUM'),\n    ParkingSpot(1, 'F1-L1', 'LARGE'),\n    ParkingSpot(2, 'F2-S1', 'SMALL'),\n]\nlot = ParkingLot(spots)\n# Motorcycle takes F2-S1 (smallest fitting spot) leaving MEDIUM & LARGE free for bigger vehicles!\nt1 = lot.park('BIKE-1', 'MOTORCYCLE', 10)\nassert lot.active_tickets[t1][3].spot_id == 'F2-S1', 'Motorcycle should prefer SMALL spot before wasting LARGE!'\nt2 = lot.park('CAR-1', 'CAR', 10)\nassert lot.active_tickets[t2][3].spot_id == 'F1-M1', 'Car takes MEDIUM F1-M1'\nt3 = lot.park('BUS-1', 'BUS', 10)\nassert lot.active_tickets[t3][3].spot_id == 'F1-L1', 'Bus fits ONLY LARGE F1-L1'\nassert lot.park('BUS-2', 'BUS', 11) is None, 'Lot full for Bus!'\nfee = lot.unpark(t2, 13)\nassert fee == 60.0, f'3 hours * $20/hr = $60.0, got {fee}'\nt4 = lot.park('CAR-2', 'CAR', 14)\nassert t4 is not None and lot.active_tickets[t4][3].spot_id == 'F1-M1', 'Freed spot F1-M1 must accept next Car!'\nprint('PARKING_LOT_VERIFIED: multi-floor fit, up-fitting fallback, release & billing passed!')",
                        "expected_output": "PARKING_LOT_VERIFIED: multi-floor fit, up-fitting fallback, release & billing passed!",
                        "hint": "Sort compatible free spots by `(SIZE_ORDER[sp.size], sp.floor, sp.spot_id)` so a Motorcycle grabs a `SMALL` spot first (preserving `LARGE` spots for Buses!) unless only `LARGE` spots remain.",
                        "why_it_works": "Decoupling `SIZE_ORDER` compatibility and spot sorting into clean metadata prevents small cars/motorcycles from needlessly consuming scarce `LARGE` spots while seamlessly up-fitting when smaller spots fill up!",
                        "complexity": "**In-memory heap/bucket indexing per size:** $O(1)$ park/unpark in production (`O(S log S)` simplified scan here).",
                        "alternatives": [
                            {"title": "Per-(Floor, Size) Min-Heaps", "desc": "Maintain `min_heaps[floor][size]` of free spots sorted by distance from entrance gate so `park()` drops from $O(S)$ scan to $O(\\log S)$!"}
                        ],
                        "edge_cases": [
                            {"title": "Same-Hour Entry & Exit (`hours == 0`)", "desc": "`max(1, exit_hour - entry_hour)` bills minimum 1 hour cleanly without zeroing out revenue."},
                            {"title": "Duplicate Vehicle Check-In Guard", "desc": "`parked_plates` prevents issuing two active tickets for the same license plate simultaneously."}
                        ]
                    }
                ]
            }
        ]
    }
}
