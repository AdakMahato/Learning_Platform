"""
System Design Story Lab - Part 1: Cases 0 to 4
Covers:
  - Case 0: Back-of-the-Envelope Estimations & Latency Math
  - Case 1: DNS, L4/L7 Load Balancers & CDNs
  - Case 2: Distributed Caching & O(1) LRU Eviction Code Lab
  - Case 3: Replication, Sharding & Hotspot Mitigation
  - Case 4: Consistent Hashing Rings & Virtual Nodes Code Lab
"""

SD_CASES_PART1 = {
    "0": {
        "title": "Back-of-the-Envelope Estimations & Latency Math",
        "episodes": [
            {
                "title": "Module 1: Capacity Constants, 86,400s Shortcut & Traffic Sizing",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Launch-Day 10x Peak Surprise",
                        "content": "A streaming startup provisioned database capacity for **average** daily QPS (`2,300 writes/sec`). When an evening sports finale drove a **5x peak burst (`11,500 writes/sec`)**, connection pools saturated, P99 latency spiked from `18 ms` to `9.4 s`, and retry storms knocked out the cluster!\n\n> [!IMPORTANT]\n> **First Rule of Capacity Planning:** Size throughput for **Peak QPS** (`2x`–`5x` average QPS) and network bandwidth/storage for **5-year cumulative retention + replication factor (typically 3x)**."
                    },
                    {
                        "type": "concept",
                        "title": "Numbers Every Systems Engineer Memorizes",
                        "content": "Rapid interview back-of-the-envelope math relies on clean rounding:\n\n- **Seconds per Day:** $24 \\times 3600 = 86,400 \\approx 10^5$ seconds! (Or $8.64 \\times 10^4$ when exactness helps.)\n  - Rule of thumb: **$100\\text{M requests/day} \\div 10^5 \\approx 1,000\\text{ QPS}$ average**!\n- **Powers of 2 Data Sizes:** $2^{10} \\approx 1\\text{ KB}$, $2^{20} \\approx 1\\text{ MB}$, $2^{30} \\approx 1\\text{ GB}$, $2^{40} \\approx 1\\text{ TB}$, $2^{50} \\approx 1\\text{ PB}$.\n- **Jeff Dean Latency Ladder:**\n  - L1 cache reference: **1 ns**\n  - RAM read: **100 ns**\n  - SSD random read: **150 $\\mu$s**\n  - Same-DC network round-trip: **500 $\\mu$s (0.5 ms)**\n  - Transcontinental US <-> Europe RTT: **75–150 ms** (speed of light in fiber!)",
                        "technical_explanation": "**Why Fiber RTT Beats Bandwidth Optimizations:** Even on a 100 Gbps link, sending 1 packet across 6,000 km of optical fiber (refractive index $n \\approx 1.47$, $c_{\\text{fiber}} \\approx 200,000\\text{ km/s}$) costs at least **60 ms round-trip**! Only **CDN edge caching** and **multi-region replicas** reduce speed-of-light latency."
                    },
                    {
                        "type": "comparison_table",
                        "title": "Typical Storage & Latency Order-of-Magnitude Sheet",
                        "headers": ["Operation / Metric", "Typical Value", "Design Implication"],
                        "rows": [
                            ["Sequential RAM Read (1 MB)", "~250 us", "In-memory indexes & Redis sub-ms reads"],
                            ["Sequential SSD Read (1 MB)", "~1 ms", "Kafka sequential log append throughput"],
                            ["Cross-Region Network RTT", "~80–150 ms", "Avoid chatty synchronous RPCs across WAN"],
                            ["1 Tweet / Short Text Record", "~300 bytes", "1B tweets/day = ~300 GB/day raw text"]
                        ]
                    }
                ]
            },
            {
                "title": "Module 2: Tail Latency (P99), Mean Deception & Fan-Out Amplification",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Why Averages Lie: Tail-at-Scale Mathematics",
                        "content": "Suppose a single microservice call succeeds under `10 ms` **99% of the time** ($p_{\\text{fast}} = 0.99$), while **1% (P99)** takes `500 ms` due to GC pauses or disk contention.\n\nIf an API gateway fans out **50 parallel microservice calls** to assemble one homepage and must wait for the **slowest** response:\n$$P(\\text{all 50 fast}) = (0.99)^{50} \\approx 0.605$$\nTherefore, **$1 - 0.605 = 39.5\\%$** of users experience the `500 ms` tail stall!",
                        "technical_explanation": "**Tail Mitigation Trio:**\n1. **Hedged Requests:** If primary replica hasn't answered within P95 (`15 ms`), dispatch an idempotent duplicate to a secondary replica and return whichever completes first.\n2. **SLA Budgets & Deadlines:** Propagate remaining timeout `deadline_ms` down RPC headers (`grpc-timeout`) so doomed downstream work cancels instead of piling onto overloaded queues.\n3. **Tiers of Degradation:** Serve stale/cached recommendations if personalization engine misses a `30 ms` budget."
                    },
                    {
                        "type": "visual",
                        "title": "Tail Amplification Across 50 Parallel Fan-Out Subrequests",
                        "code": """flowchart LR
    GW["API Gateway Request"] --> F1["Svc 1..49: 9 ms each"]
    GW --> F50["Svc 50 (1% P99 GC Pause): 500 ms"]
    F1 --> Join["Wait-All Barrier: Delayed to 500 ms!"]
    F50 --> Join"""
                    }
                ]
            },
            {
                "title": "Module 3: Estimation Drills — QPS & 5-Year Storage Sizing",
                "blocks": [
                    {
                        "type": "calculation_challenge",
                        "title": "Peak Write QPS Estimation",
                        "formula": "Average QPS = (DAU * Actions/Day) / 86400; Peak QPS = 3 * Average QPS (using 10^5 sec/day approximation)",
                        "question": "A microblogging platform has **50 million DAU**, each posting **2 tweets per day** on average. Using the standard `100,000` seconds/day shortcut (`10^5`) and a **3x peak multiplier**, what is the estimated **Peak Write QPS**?",
                        "answer": "3000",
                        "alternatives": ["3000", "3,000", "3000 QPS"],
                        "step_by_step": "1. Daily writes = $50 \\times 10^6 \\times 2 = 100 \\times 10^6 = 10^8$ writes/day.\n2. Average Write QPS $\\approx 10^8 / 10^5 = 1,000$ QPS.\n3. Peak Write QPS ($3\\times$) $= 3 \\times 1,000 = \\mathbf{3,000\\text{ QPS}}$."
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Cumulative Object Storage Over 5 Years",
                        "question": "Suppose **1 million new photos/day** are uploaded at an average compressed size of **200 KB** each. Ignoring metadata overhead and before replication, approximately how many **TB per year** does raw photo storage require? (Use `1 year = 365 days`, round to nearest integer TB if decimal, e.g., `73`.)",
                        "answer": "73",
                        "alternatives": ["73", "73 TB"],
                        "step_by_step": "1. Daily storage = $10^6 \\times 200\\text{ KB} = 200 \\times 10^6\\text{ KB} = 200\\text{ GB/day} = 0.2\\text{ TB/day}$.\n2. Yearly storage = $0.2\\text{ TB/day} \\times 365 = \\mathbf{73\\text{ TB/year}}$ (or ~365 TB over 5 years, ~1.1 PB with 3x replication)."
                    }
                ]
            },
            {
                "title": "Module 4: SLA Defense & Hedged Request Strategy",
                "blocks": [
                    {
                        "type": "scenario_decision",
                        "title": "Taming P99 Spikes on a Multi-Service Feed Page",
                        "scenario": "Your e-commerce homepage makes 20 parallel read RPCs to fetch price, inventory, and reviews. 99% of individual read calls take `8 ms`, yet `1%` hit RocksDB compaction stalls (`400 ms`), causing `18%` of page loads to breach the `150 ms` SLO.",
                        "question": "Which architectural strategy eliminates tail latency on idempotent reads WITHOUT doubling normal cluster load?",
                        "options": [
                            "Dispatch a Hedged Request to a secondary replica ONLY after the primary call exceeds its P95 threshold (~12 ms), cancelling slower in-flight work upon first reply",
                            "Always fire 2 duplicate requests immediately for every user request (200% permanent traffic)",
                            "Switch all 20 parallel RPCs to run sequentially so they don't compete",
                            "Replace SSD replicas with magnetic HDDs to smooth compaction latency"
                        ],
                        "answer": "Dispatch a Hedged Request to a secondary replica ONLY after the primary call exceeds its P95 threshold (~12 ms), cancelling slower in-flight work upon first reply",
                        "rationale": "Google's *Tail at Scale* paper showed delaying hedged requests until the P95 latency threshold adds only **~5% extra load** while cutting P99 tail latency by over **80%**, because 95% of requests finish cleanly before the timer fires!"
                    },
                    {
                        "type": "fill_in_the_blank",
                        "title": "Backpressure Mechanism",
                        "question": "To prevent a degraded downstream dependency from collapsing under retry traffic during an outage, callers use a _____ pattern (tripping open on error threshold) plus exponential backoff with jitter.",
                        "answer": "circuit breaker",
                        "alternatives": ["circuit breaker", "Circuit Breaker"],
                        "explanation": "A **Circuit Breaker** stops sending doomed traffic when failures exceed a threshold, letting the downstream cluster recover cleanly instead of drowning in immediate synchronous retries."
                    }
                ]
            }
        ]
    },
    "1": {
        "title": "Traffic Mesh: DNS, L4/L7 Load Balancers & CDNs",
        "episodes": [
            {
                "title": "Module 1: Global Ingress — Anycast DNS, Geo-Routing & TTL Trade-offs",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Failover That Took 24 Hours",
                        "content": "When Region `us-east-1` suffered a regional outage, engineers updated their DNS A-record to point traffic to `us-west-2`—yet **40% of corporate users still hammered the dead IP 6 hours later**! Why? Both legacy ISP resolvers and aggressive JVM DNS caches ignored short-TTL hints after an earlier **24-hour TTL (`86400s`)** had been pinned.\n\n> [!IMPORTANT]\n> **DNS Failover Reality Check:** DNS is NOT instantaneous failover. Pair short DNS TTLs (`30s–60s`) with **BGP Anycast** or a **Global Load Balancer** so traffic drains rapidly at the IP routing layer!"
                    },
                    {
                        "type": "concept",
                        "title": "Multi-Layer Edge Traffic Pipeline",
                        "content": "A modern client request traverses four distinct edge layers before touching business compute:\n\n1. **Authoritative / Geo-DNS:** Resolves `api.example.com` to the geographically closest Point of Presence (PoP) via GeoIP or latency-based routing.\n2. **Anycast BGP Routing:** Multiple global edge routers announce the **exact same IP prefix**; Internet BGP automatically routes each client to the topologically nearest PoP.\n3. **CDN Edge PoPs:** Terminate TCP/TLS close to users (~10 ms RTT!) and serve cacheable static assets (`Cache-Control: public, max-age=86400`).\n4. **L4 -> L7 Load Balancers:** Route dynamic API requests across healthy stateless backend pods.",
                        "technical_explanation": "**Why Edge TLS Termination Cuts Latency in Half:** A TCP + TLS 1.3 handshake requires 2 RTTs. Terminating TLS at an edge PoP `12 ms` away (versus an origin server `140 ms` away) saves **`256 ms`** before a single HTTP byte even streams, and keeps persistent HTTP/2 multiplexed connections warm back to origin!"
                    },
                    {
                        "type": "visual",
                        "title": "Global Edge-to-Origin Request Path",
                        "code": """flowchart LR
    User["Client Browser"] -->|Anycast BGP IP| CDN["CDN Edge PoP (TLS Termination)"]
    CDN -->|Cache Hit static| User
    CDN -->|Cache Miss dynamic| L4["L4 Maglev / IPVS Balancer"]
    L4 --> L7["L7 Reverse Proxy (Envoy / NGINX)"]
    L7 -->|Health-checked Pool| App["Stateless App Servers"]"""
                    }
                ]
            },
            {
                "title": "Module 2: L4 Transport Balancers vs L7 Application Reverse Proxies",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Layer 4 vs Layer 7 Load Balancing Mechanics",
                        "content": "- **L4 Load Balancer (TCP/UDP packet forwarding):** Inspects ONLY the **5-tuple** `(src_ip, src_port, dst_ip, dst_port, proto)`. Supports **Direct Server Return (DSR)** so outbound video/file bytes stream straight from backend to client bypassing the LB! Zero HTTP parsing -> tens of millions of Packets/sec.\n- **L7 Reverse Proxy (HTTP/gRPC aware):** Terminates TCP and decrypts TLS to inspect **URL path (`/api/v2/pay`), HTTP Headers (`Authorization`, `Cookie`), and cookies**. Enables canary routing (`5%` to v2), WAF inspection, gRPC frame balancing, and connection multiplexing.",
                        "technical_explanation": "**Consistent Architecture Pattern:** Use **two tiers**: a fast stateless **L4 fleet** (`Maglev` / AWS NLB) receiving Anycast VIP packets via ECMP (Equal-Cost Multi-Path routing), forwarding to an auto-scaling **L7 fleet** (`Envoy` / `NGINX`) that handles TLS, auth middleware, rate limiting, and backend microservice routing."
                    },
                    {
                        "type": "comparison_table",
                        "title": "L4 vs L7 Load Balancing Comparison",
                        "headers": ["Capability", "L4 Load Balancer", "L7 Load Balancer"],
                        "rows": [
                            ["OSI Layer", "Transport (TCP/UDP)", "Application (HTTP/HTTPS/gRPC)"],
                            ["TLS Termination", "No (passthrough) or limited", "Yes (decryption + mTLS re-encrypt)"],
                            ["Content Routing (`/img` vs `/api`)", "No — cannot read HTTP URI", "Yes (path, header, cookie routing)"],
                            ["Direct Server Return (DSR)", "Yes — highest video throughput", "No (full reverse proxy terminates both sides)"]
                        ]
                    }
                ]
            },
            {
                "title": "Module 3: Edge SPOF Audits & CDN Pull vs Push Strategy",
                "blocks": [
                    {
                        "type": "diagram_critique",
                        "title": "Audit This Production Edge Topology",
                        "scenario": "A fast-growing SaaS launches worldwide with this exact request architecture and hits 100% downtime during a cloud AZ brownout.",
                        "code": """flowchart LR
    U["Global Users"] --> S["Single NGINX VM (us-east-1a)"]
    S -->|HTTP| DB["All Traffic -> Origin Server"]
    DB --> S3["Origin Disk Images"]""",
                        "question": "What are the **primary architectural flaws** shown in this ingress design?",
                        "options": [
                            "Single NGINX node is a hard Single Point of Failure (SPOF) AND lacks a CDN for static images, forcing all global reads across WAN to one AZ",
                            "NGINX should never speak HTTP to origin servers",
                            "Using a database server to store PNG images is mandatory before adding a LB",
                            "DNS must route straight to user browsers without a port number"
                        ],
                        "answer": "Single NGINX node is a hard Single Point of Failure (SPOF) AND lacks a CDN for static images, forcing all global reads across WAN to one AZ",
                        "remedy": "Deploy Active-Active L4/L7 Load Balancers across multiple Availability Zones behind Anycast/Health-checked DNS, and offload static media behind a Pull CDN with versioned asset URLs."
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Latency Saved by Regional Edge TLS Termination",
                        "question": "A user has a `15 ms` RTT to the nearest CDN Edge PoP and `140 ms` RTT direct to Origin. Assuming a fresh **TCP + TLS 1.3 connection costs 2 RTTs** before the HTTP GET is sent (plus 1 RTT for HTTP payload = **3 RTTs** if un-terminated, whereas CDN already holds a **warm persistent TCP/TLS pool** back to Origin costing only 1 origin RTT for cache miss), how many total milliseconds does the handshake-warmed Edge path take for an initial dynamic origin fetch? (`2*15 + 15 + 140`? Wait carefully: 2 RTTs edge handshake `2*15 = 30 ms` + HTTP request edge `15 ms` + origin fetch over warm pool `140 ms`.)",
                        "answer": "185",
                        "alternatives": ["185", "185 ms"],
                        "step_by_step": "- **Direct Origin (no warm edge):** `3 RTTs * 140 ms = 420 ms`.\n- **Warm Edge PoP:** Edge TCP+TLS 1.3 handshake (`2 * 15 = 30 ms`) + Edge HTTP transit (`15 ms`) + Warm Origin link (`1 * 140 ms`) = **`185 ms`** (saving `235 ms`!)."
                    }
                ]
            },
            {
                "title": "Module 4: Push vs Pull CDNs & Cache-Busting Invalidation",
                "blocks": [
                    {
                        "type": "scenario_decision",
                        "title": "CDN Architecture for 50M Monthly Long-Tail User Images",
                        "scenario": "You run an online classifieds marketplace with 50M user-uploaded item photos. 95% of older listings are rarely viewed after 7 days, while fresh viral listings spike heavily across cities.",
                        "question": "Which CDN strategy and invalidation policy prevents wasting petabytes of Edge SSD capacity while keeping active listings blazing fast?",
                        "options": [
                            "Pull CDN with long immutable `Cache-Control: max-age=31536000` and content-hashed filenames (`/img/a8f91c.webp`), letting LRU evict cold long-tail files automatically",
                            "Push CDN proactively pre-uploading every single uploaded thumbnail to all 300 global PoPs immediately",
                            "Set `Cache-Control: no-store` on all images so every image fetch validates at Origin",
                            "Manually run a global CDN PURGE API call every 10 seconds across all 50M images"
                        ],
                        "answer": "Pull CDN with long immutable `Cache-Control: max-age=31536000` and content-hashed filenames (`/img/a8f91c.webp`), letting LRU evict cold long-tail files automatically",
                        "rationale": "**Pull CDNs** only replicate hot objects into PoPs on first demand and naturally evict cold objects. **Content-hashed filenames** eliminate expensive global cache invalidations because updated files get a brand-new URL!"
                    },
                    {
                        "type": "concept",
                        "title": "Health Checks & Connection Draining",
                        "content": "L4/L7 balancers differentiate **Liveness (`/healthz`)** vs **Readiness (`/readyz`)**:\n\n- During blue-green deploys or scale-down, remove an instance from DNS/LB rotation FIRST (**graceful draining**), wait for active TCP/HTTP requests to finish (~30s), and ONLY then terminate the process (`SIGTERM -> SIGKILL`) so zero in-flight user requests see `502 Bad Gateway`!"
                    }
                ]
            }
        ]
    },
    "2": {
        "title": "Sub-Millisecond Memory: Distributed Caching & LRU Eviction",
        "episodes": [
            {
                "title": "Module 1: Caching Write/Read Topologies (Aside, Through, Back)",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Thundering Herd at Midnight",
                        "content": "When a trending flash-sale item's cache TTL expired at `00:00:00`, **45,000 concurrent threads** simultaneously saw a Redis cache miss, bypassed Redis, and slammed the exact same `SELECT * FROM products WHERE id=99` query into PostgreSQL! CPU pegged at `100%` within 400 milliseconds!\n\n> [!IMPORTANT]\n> Caching isn't just `if hit: return; else query()`. You must select the right **Write Consistency Pattern** AND engineer defenses for **Cache Stampede**, **Penetration**, and **Avalanche**!"
                    },
                    {
                        "type": "concept",
                        "title": "Four Core Caching Topologies",
                        "content": "1. **Cache-Aside (Lazy Loading):** Application checks Cache -> on miss, reads DB -> populates Cache -> returns. Resilient (cache crash just degrades to DB), stores only active working set.\n2. **Read-Through:** App talks ONLY to Cache; Cache library/provider itself fetches DB on miss.\n3. **Write-Through:** Write goes synchronously to Cache AND DB before ACK. Zero stale writes, higher write latency.\n4. **Write-Back (Write-Behind):** App writes to fast Cache RAM only and returns `200 OK`; background workers flush dirty batches to DB asynchronously. **Blazing write throughput**, but risk of **data loss** if cache node crashes before flush!",
                        "technical_explanation": "**Best Default Pairings:** Use **Cache-Aside + short TTL + explicit DB invalidation** for general read-heavy web services (profiles, catalogs). Use **Write-Back** for high-frequency non-critical counters (like video view counts flushed to DB every 5s)."
                    },
                    {
                        "type": "comparison_table",
                        "title": "Caching Strategy Trade-off Matrix",
                        "headers": ["Pattern", "Read Latency", "Write Latency", "Stale / Data-Loss Risk"],
                        "rows": [
                            ["Cache-Aside", "Fast on hit (miss costs 1 DB hop)", "Normal DB speed", "Brief staleness until TTL or delete"],
                            ["Write-Through", "Fast on read (pre-warmed)", "Slowest (2 sync writes)", "Low stale risk, zero data loss"],
                            ["Write-Back (Behind)", "Fast on read", "Fastest (RAM ACK only)", "HIGH data loss risk if RAM node dies!"]
                        ]
                    }
                ]
            },
            {
                "title": "Module 2: Failure Trio — Stampede, Penetration & Avalanche",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Three Classic Distributed Cache Outages & Remedies",
                        "content": "- **1. Cache Stampede (Thundering Herd):** One ultra-hot key expires -> thousands of concurrent threads miss and query DB.\n  - *Fix:* **Request Coalescing (`Singleflight` / Mutex Lock)** so ONLY **1 flight** hits DB while concurrent misses await that shared result, OR **logical probabilistic early refresh**.\n- **2. Cache Penetration (Non-Existent Key Attack):** Attackers query `user_id=-99999` which exists in NEITHER Cache nor DB -> 100% miss ratio hits DB!\n  - *Fix:* Cache **Null Sentinels** with short TTL (`60s`) AND check an in-memory **Bloom Filter** before touching DB!\n- **3. Cache Avalanche (Synchronized Expiry):** Bulk-loaded 1M keys with identical `TTL = 3600s` expire at once.\n  - *Fix:* **TTL Jitter (`base_ttl + random(0, 300s)`)** + Cluster HA (Redis Sentinel/Cluster).",
                        "technical_explanation": "**Delete vs Update Cache on Write:** Always **DELETE** the key from cache after committing DB rather than trying to update both in parallel! Concurrent writers `W1` then `W2` could update DB in order `W1 -> W2` yet apply Cache updates out-of-order `W2 -> W1`, permanently corrupting cache with stale `W1`!"
                    },
                    {
                        "type": "debugger",
                        "title": "Bug Hunt: The Stale Cache Race Condition",
                        "code": """def update_profile(user_id, new_bio):
    # Writer sets DB first, then updates cache:
    db.execute("UPDATE users SET bio=%s WHERE id=%s", (new_bio, user_id))
    redis.set(f"user:{user_id}", json.dumps({"bio": new_bio}), ex=3600)""",
                        "question": "Why can two concurrent requests (`update_profile(1, 'Alice-v2')` and `update_profile(1, 'Alice-v3')`) permanently leave `'Alice-v2'` stuck in Redis while Postgres holds `'Alice-v3'`?",
                        "options": [
                            "Thread reordering between DB commit and `redis.set`: `v3` can commit to DB last, yet stall right before `redis.set`, allowing `v2`'s delayed `redis.set` to overwrite cache last!",
                            "JSON serialization is non-deterministic in Python",
                            "Redis `ex=3600` rejects keys longer than 32 bytes",
                            "SQL `UPDATE` statements cannot run concurrently on PostgreSQL"
                        ],
                        "answer": "Thread reordering between DB commit and `redis.set`: `v3` can commit to DB last, yet stall right before `redis.set`, allowing `v2`'s delayed `redis.set` to overwrite cache last!",
                        "explanation": "Prefer **DB Update -> Cache `DEL`** (or CDC binlog invalidation via Debezium) so subsequent misses cleanly re-read the authoritative committed DB state."
                    }
                ]
            },
            {
                "title": "Module 3: Mitigating Stampede & Penetration Decisions",
                "blocks": [
                    {
                        "type": "scenario_decision",
                        "title": "Stopping a Bot Scraping Fake Product IDs",
                        "scenario": "Malicious scrapers flood `/api/product?id=<random_9_digit_uuid>` at `25,000 QPS`. Over 99% of those IDs don't exist in your SQL table, so Redis returns `nil` and every request hits MySQL `PRIMARY KEY` lookup.",
                        "question": "Which two complementary defenses eliminate the MySQL load immediately with minimal RAM?",
                        "options": [
                            "Place a compact Bloom Filter in front of DB lookups AND cache short-TTL Null Sentinel values (`'__NULL__'`) for missed queries",
                            "Pre-load the entire 4 TB MySQL database into Redis RAM on every edge host",
                            "Turn off Redis completely so MySQL caches queries in InnoDB Buffer Pool",
                            "Rate limit legitimate logged-in buyers to 1 request per minute"
                        ],
                        "answer": "Place a compact Bloom Filter in front of DB lookups AND cache short-TTL Null Sentinel values (`'__NULL__'`) for missed queries",
                        "rationale": "A **Bloom Filter** uses mere megabytes (`~10 bits/element` for 1% false-positive rate) to reject `definitely NOT present` IDs in $O(k)$ CPU before hitting DB; Null Sentinels neutralize any remaining misses or false positives."
                    },
                    {
                        "type": "fill_in_the_blank",
                        "title": "Coalescing Duplicate Cache Misses",
                        "question": "The concurrency pattern (popularized in Go's `golang.org/x/sync/singleflight`) where multiple goroutines/threads missing the same hot key wait for ONE leader DB fetch to share its result is called request _____.",
                        "answer": "coalescing",
                        "alternatives": ["coalescing", "singleflight", "Coalescing"],
                        "explanation": "**Request Coalescing (`Singleflight`)** collapses 10,000 simultaneous cache misses for key `K` into **1 backend query**!"
                    }
                ]
            },
            {
                "title": "Module 4: Code Lab — Implement O(1) LRU Cache Engine (Doubly Linked List + HashMap)",
                "blocks": [
                    {
                        "type": "code_lab",
                        "language": "python",
                        "title": "Implement O(1) Thread-Ready LRU Eviction Engine",
                        "instruction": "Every distributed cache node (`Redis`, `Memcached`) must evict the **Least Recently Used** key in strict **$O(1)$ time** when memory hits capacity.\n\nImplement `class LRUCache:` from scratch using a **Hash Map + Doubly Linked List** (sentinel `head` = MRU side, sentinel `tail` = LRU side — avoid `OrderedDict` so you master the pointer mechanics!).\n\nImplement:\n- `get(key: int) -> int`: Return value if present (and promote node to MRU front), else `-1`.\n- `put(key: int, value: int) -> None`: Insert/update key and promote to MRU front; if size exceeds `capacity`, evict the LRU node at `tail.prev` in $O(1)$.",
                        "starter_code": "class _Node:\n    def __init__(self, k: int = 0, v: int = 0):\n        self.k = k\n        self.v = v\n        self.prev = None\n        self.next = None\n\nclass LRUCache:\n    def __init__(self, capacity: int):\n        self.cap = capacity\n        self.cache = {}\n        self.head = _Node()\n        self.tail = _Node()\n        self.head.next = self.tail\n        self.tail.prev = self.head\n\n    def get(self, key: int) -> int:\n        # TODO: return value & move to MRU front, else -1\n        return -1\n\n    def put(self, key: int, value: int) -> None:\n        # TODO: insert/update & evict LRU if > capacity\n        pass\n",
                        "solution_code": "class _Node:\n    def __init__(self, k: int = 0, v: int = 0):\n        self.k = k\n        self.v = v\n        self.prev = None\n        self.next = None\n\nclass LRUCache:\n    def __init__(self, capacity: int):\n        self.cap = capacity\n        self.cache = {}\n        self.head = _Node()\n        self.tail = _Node()\n        self.head.next = self.tail\n        self.tail.prev = self.head\n\n    def _remove(self, node: _Node) -> None:\n        p, n = node.prev, node.next\n        p.next = n\n        n.prev = p\n\n    def _add_front(self, node: _Node) -> None:\n        first = self.head.next\n        self.head.next = node\n        node.prev = self.head\n        node.next = first\n        first.prev = node\n\n    def get(self, key: int) -> int:\n        node = self.cache.get(key)\n        if not node:\n            return -1\n        self._remove(node)\n        self._add_front(node)\n        return node.v\n\n    def put(self, key: int, value: int) -> None:\n        if key in self.cache:\n            node = self.cache[key]\n            node.v = value\n            self._remove(node)\n            self._add_front(node)\n            return\n        if self.cap <= 0:\n            return\n        if len(self.cache) == self.cap:\n            lru = self.tail.prev\n            self._remove(lru)\n            del self.cache[lru.k]\n        node = _Node(key, value)\n        self.cache[key] = node\n        self._add_front(node)\n",
                        "test_code": "lru = LRUCache(2)\nlru.put(1, 10)\nlru.put(2, 20)\nassert lru.get(1) == 10, 'Key 1 should be promoted to MRU'\nlru.put(3, 30)  # evicts key 2!\nassert lru.get(2) == -1, 'Key 2 should have been evicted'\nlru.put(1, 100) # update existing value & keep key 1 MRU\nlru.put(4, 40)  # evicts key 3!\nassert lru.get(3) == -1 and lru.get(1) == 100 and lru.get(4) == 40\nprint('LRU_VERIFIED: capacity=2 O(1) promote/evict/update passed!')",
                        "expected_output": "LRU_VERIFIED: capacity=2 O(1) promote/evict/update passed!",
                        "hint": "Write two clean $O(1)$ helpers: `_remove(node)` relinks `node.prev <-> node.next`, and `_add_front(node)` splices right after dummy `self.head`. Updating an existing key MUST ALSO move it to front!",
                        "why_it_works": "A **Hash Map** locates any node reference in $O(1)$ without scanning, while sentinel `head`/`tail` pointers on a **Doubly Linked List** remove/reinsert nodes in exact $O(1)$ pointer reassignments with zero `null` edge-case branches.",
                        "complexity": "**Time:** $O(1)$ exact per `get` and `put`.\n**Space:** $O(\\text{capacity})$.",
                        "alternatives": [
                            {"title": "LFU Cache (Least Frequently Used)", "desc": "Evicts lowest frequency counter (breaking ties via LRU list per frequency bucket). Better hit ratio on power-law workloads, but suffers stale historical hot keys unless aged."},
                            {"title": "W-TinyLFU (Caffeine / modern Go caches)", "desc": "Uses a tiny Count-Min Sketch frequency estimator + Segmented LRU window achieving near-optimal hit rates with minimal RAM."}
                        ],
                        "edge_cases": [
                            {"title": "Update Existing Key (`put(1, 100)`) Must Promote", "desc": "Overwriting an existing key's value must ALSO move that node to the MRU front; otherwise a freshly updated hot key gets evicted next!"},
                            {"title": "Sentinel Dummy Nodes Eliminate Null Checks", "desc": "Dummy `head` and `tail` guarantee every real node ALWAYS has non-null `prev` and `next`."}
                        ]
                    }
                ]
            }
        ]
    },
    "3": {
        "title": "Scaling Stateful Data: Replication, Sharding & Hotspots",
        "episodes": [
            {
                "title": "Module 1: Replication Topologies, WAL Streaming & Lag Anomalies",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Phantom Missing Comment",
                        "content": "A user hit **Post Comment**, saw HTTP `201 Created`, immediately refreshed the page—and their comment had vanished! Wait 2 seconds and refresh again, and it magically reappeared!\n\n> [!IMPORTANT]\n> **Root Cause (Replication Lag):** The `POST` wrote to the **Leader**, while the immediate `GET` routed to an asynchronous **Read Replica** that hadn't finished applying the WAL stream yet!"
                    },
                    {
                        "type": "concept",
                        "title": "Leader-Follower Replication & Consistency Guarantees",
                        "content": "- **Synchronous Replication:** Leader waits for follower `fsync` before confirming client write. **Zero data loss**, yet doubles write latency and halts writes if follower dies!\n- **Asynchronous Replication (Default MySQL/Postgres):** Leader ACKs immediately and ships WAL/Binlog asynchronously. High throughput, risking milliseconds-to-seconds of **Replication Lag**.\n- **How to Guarantee Read-Your-Own-Writes:**\n  1. Route the **author's own reads** (`user_id == post_author`) or any write within `< 5s` (`last_write_ts` session cookie / LSN watermark) straight to the **Leader**.\n  2. Route normal public read traffic across **Read Replicas**.",
                        "technical_explanation": "**Monotonic Reads:** Ensure a single user never reads backward in time (e.g., first hitting fast Replica A at LSN `500`, then stale Replica B at LSN `480`) by sticky-hashing `session_id -> replica`."
                    },
                    {
                        "type": "visual",
                        "title": "Write-to-Leader / Read-Your-Writes Watermark Routing",
                        "code": """flowchart LR
    C["Client (Write LSN=105)"] -->|Mutation| L["Primary Leader (LSN=105)"]
    L -.->|Async WAL lag=40ms| R1["Replica 1 (LSN=105)"]
    L -.->|Async WAL lag=200ms| R2["Replica 2 (LSN=101: STALE!)"]
    C -->|Read within 5s OR LSN>=105| L"""
                    }
                ]
            },
            {
                "title": "Module 2: Vertical Partitioning, Horizontal Sharding & Routing",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Sharding Strategies & Choosing the Shard Key",
                        "content": "When a single primary overflows **write QPS** or **multi-TB disk/index RAM**, split data horizontally across independent shards:\n\n1. **Range Sharding (`user_id 1..10M -> Shard 0`):** Great range scans, terrible **temporal write hotspots** if IDs grow monotonically!\n2. **Hash Sharding (`hash(shard_key) % N`):** Evenly spreads write QPS across shards, breaks cross-shard range scans and requires massive data movement if `N` changes without **Consistent Hashing**.\n3. **Shard Key Selection Rule:** Pick a high-cardinality key appearing in **90%+ of queries** (e.g., `tenant_id` in SaaS or `user_id` for user profiles) so queries target **1 shard**, avoiding expensive scatter-gather fan-out!",
                        "technical_explanation": "**Painful Side Effects of Sharding:** Foreign keys can't enforce cross-shard integrity in SQL; cross-shard `JOIN`s become expensive application-layer merges; cross-shard ACID commits require heavyweight **2PC / Saga patterns**."
                    },
                    {
                        "type": "comparison_table",
                        "title": "Database Scaling Progression",
                        "headers": ["Technique", "Solves Read QPS?", "Solves Write QPS?", "Solves Storage Size?"],
                        "rows": [
                            ["Indexes + Caching", "Yes (10x–100x)", "No (slows writes slightly)", "No"],
                            ["Read Replicas", "Yes (scales horizontally)", "No (single leader bottleneck)", "No (full copy per node)"],
                            ["Functional / Vertical Partitioning", "Yes (isolated tables)", "Partially (split hot tables)", "Partially"],
                            ["Horizontal Sharding", "Yes", "Yes (multi-leader partitions!)", "Yes (split across nodes)"]
                        ]
                    }
                ]
            },
            {
                "title": "Module 3: Debugging Stale Replicas & Calculating Shard Capacity",
                "blocks": [
                    {
                        "type": "debugger",
                        "title": "Bug Hunt: Multi-Replica Backwards Time Travel (Non-Monotonic Reads)",
                        "code": """def get_comment_feed(post_id):
    # Random load-balancing across 3 async read replicas:
    replica = random.choice([REPLICA_A, REPLICA_B, REPLICA_C])
    return replica.query("SELECT * FROM comments WHERE post_id = %s", post_id)""",
                        "question": "A user sees a new comment on refresh #1, then refreshes #2 (`200ms` later) and sees the old comment **disappear**! Why does `random.choice` cause this regression?",
                        "options": [
                            "Request #1 hit up-to-date `REPLICA_A`, while Request #2 landed on lagging `REPLICA_C` behind by 500ms—violating Monotonic Reads!",
                            "`SELECT *` always returns rows in reverse insertion order across replicas",
                            "Python `random.choice` modifies SQL isolation level to READ UNCOMMITTED",
                            "Multiple replicas cannot hold indexes simultaneously"
                        ],
                        "answer": "Request #1 hit up-to-date `REPLICA_A`, while Request #2 landed on lagging `REPLICA_C` behind by 500ms—violating Monotonic Reads!",
                        "explanation": "Pin each user session to a consistent replica (`replicas[hash(user_id) % K]`) or enforce a **minimum LSN check** (`wait_for_lsn >= client_seen_lsn`)."
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Database Shard Count Sizing",
                        "question": "Your telemetry store will accumulate **64 TB** over 3 years. To ensure fast backup recovery and balanced B-Tree indexes fitting nicely in NVMe + buffer pool, your SRE policy caps **each primary DB shard at 2 TB**. How many shards are needed?",
                        "answer": "32",
                        "alternatives": ["32", "32 shards"],
                        "step_by_step": "$64\\text{ TB} \\div 2\\text{ TB/shard} = \\mathbf{32\\text{ shards}}$ (in production often provisioned as 32 logical/physical shards or 64 virtual shards for easier future splits!)."
                    }
                ]
            },
            {
                "title": "Module 4: Taming the Justin Bieber Celebrity Hotspot",
                "blocks": [
                    {
                        "type": "scenario_decision",
                        "title": "Shard #4 Meltdown on Viral Celebrity Drops",
                        "scenario": "Your user/creator table is cleanly hash-sharded by `creator_id` across 32 database shards. During a live pop-concert merch drop by `creator_id=42` (`100M` fans), Shard #4's CPU hits `100%` while the other 31 shards sit at `3%` idle!",
                        "question": "What architectural fix eliminates the hot partition on `creator_id=42` while keeping standard creators' reads fast?",
                        "options": [
                            "Shard-Key Salting for flagged hot creators (`42#0 .. 42#9` spread across 10 shards) paired with read caching in Redis Cluster",
                            "Switch from Hash Sharding to Range Sharding by ascending `creator_id`",
                            "Scale Shard #4 down to force traffic to fail faster",
                            "Merge all 32 shards back onto 1 single machine so there is no skew"
                        ],
                        "answer": "Shard-Key Salting for flagged hot creators (`42#0 .. 42#9` spread across 10 shards) paired with read caching in Redis Cluster",
                        "rationale": "**Key Salting (Suffixing)** appends a random or hashed bucket `_0 .. _k-1` ONLY for identified hot keys so writes/counters spread evenly across shards, while reads either hit an edge/Redis cache or aggregate the `k` sub-buckets!"
                    },
                    {
                        "type": "fill_in_the_blank",
                        "title": "Dedicated Read Scaling Tier",
                        "question": "When 95% of database traffic consists of `SELECT` queries, engineers attach asynchronous _____ nodes behind a read load balancer to scale read capacity independently of writes.",
                        "answer": "read replica",
                        "alternatives": ["read replica", "read replicas", "follower", "followers"],
                        "explanation": "**Read Replicas** absorb read QPS horizontally, though they do NOT alleviate single-leader **write** bottlenecks (which require Sharding)."
                    }
                ]
            }
        ]
    },
    "4": {
        "title": "Ring Topology: Consistent Hashing & Virtual Nodes",
        "episodes": [
            {
                "title": "Module 1: Why Modulo Hashing Breaks & How the Hash Ring Saves Us",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Auto-Scaler That Nuked 92% of Redis",
                        "content": "An engineer routed cache requests via **`server = servers[hash(key) % N]`**. When auto-scaling added 1 extra server (`N = 10 -> 11`), **`91%` of keys hashed to completely different slots (`hash(k) % 10 != hash(k) % 11`)**! Overnight, 91% of requests became cache misses and flooded PostgreSQL!\n\n> [!IMPORTANT]\n> **Consistent Hashing Invariant:** When scaling a ring from $N - 1$ to $N$ nodes, ONLY **$\\approx \\frac{K}{N}$** keys need to move—zero global cache invalidation storm!"
                    },
                    {
                        "type": "concept",
                        "title": "How Consistent Hashing + Virtual Nodes Work",
                        "content": "1. **Circular Ring `[0, 2^32 - 1]`:** Hash BOTH server IDs AND data keys onto the same 32-bit integer circle.\n2. **Clockwise Assignment:** Given `h = hash(key)`, walk **clockwise** (`bisect_right` binary search!) to find the first node position `>= h` (wrapping around to index `0` past `max_pos`).\n3. **Why Virtual Nodes (VNodes) Are Mandatory:**\n   - With only 3 physical servers on a raw ring, random hashes create huge uneven arcs (`65%` load on Node A, `10%` on Node B!).\n   - Assign each physical machine **`V = 100` to `200` virtual tokens** (`nodeA#0, nodeA#1, ...`) scattered around the ring! Law of Large Numbers shrinks standard deviation of load below **`5%`** AND supports **heterogeneous hardware** (give a 2x RAM box `2*V` tokens!).",
                        "technical_explanation": "**Bounded Loads Extension (Vimeo/Google):** Even with VNodes, a single viral key makes one node hot. **Consistent Hashing with Bounded Loads** sets a per-server capacity cap `ceil(avg_load * (1 + epsilon))` and continues clockwise along the ring if the primary node is saturated!"
                    },
                    {
                        "type": "visual",
                        "title": "Consistent Hash Ring Clockwise Lookup",
                        "code": """flowchart LR
    K["Key hash = 140"] --> BS["Binary Search sorted VNode Ring: [50:A, 120:B, 210:C, 380:A]"]
    BS --> First["First VNode >= 140 is 210:C"]
    First --> Owner["Route key cleanly to Node C!"]"""
                    }
                ]
            },
            {
                "title": "Module 2: Partitioning Trade-offs & Rebalancing Operations",
                "blocks": [
                    {
                        "type": "comparison_table",
                        "title": "Modulo Hashing vs Hash Ring vs Ring + Virtual Nodes",
                        "headers": ["Scheme", "Keys Moved on Add/Remove Node", "Load Uniformity", "Heterogeneous Hardware?"],
                        "rows": [
                            ["Modulo (`h % N`)", "~(N-1)/N (up to 95%!)", "Uniform on keys", "No (hardcoded % N)"],
                            ["Raw Ring (No VNodes)", "Optimal ~K/N (~1/N)", "Poor (huge arc skew!)", "No"],
                            ["Ring + Virtual Nodes", "Optimal ~K/N", "Excellent (<5% variance)", "Yes! Proportional VNode count"]
                        ]
                    },
                    {
                        "type": "concept",
                        "title": "Cascading Node Failure Hazard & Mitigation",
                        "content": "Wait—if physical Node A fails **without VNodes**, its entire huge key range shifts onto its **single clockwise neighbor Node B**, potentially overloading and killing B in a **domino cascade**! **With Virtual Nodes**, Node A's `150` virtual segments sit scattered across the ring, so A's orphaned keys distribute **evenly across ALL remaining healthy nodes**!"
                    }
                ]
            },
            {
                "title": "Module 3: Remapping Math & Ring Skew Flaw Review",
                "blocks": [
                    {
                        "type": "calculation_challenge",
                        "title": "Fraction of Keys Remapped on Scale-Out",
                        "formula": "Consistent Hashing expected movement = K / N_new",
                        "question": "A cluster stores **$K = 10,000,000$** cache keys cleanly balanced on a Consistent Hash Ring across **$N = 9$** servers. When you add a **10th server** (total $N_{\\text{new}} = 10$), approximately how many million keys (`e.g. 1`) shift ownership? (Answer as an integer number of **millions**, e.g. `1`.)",
                        "answer": "1",
                        "alternatives": ["1", "1M", "1 million", "10%"],
                        "step_by_step": "Under Consistent Hashing, the new 10th node steals $\\approx 1/10 = 10\\%$ from its clockwise neighbors: $10\\text{M} / 10 = \\mathbf{1\\text{ million}}$ keys (whereas `hash(k) % N` would reshuffle `~9 million` keys!)."
                    },
                    {
                        "type": "diagram_critique",
                        "title": "Diagnose the Broken Dynamo Ring Setup",
                        "scenario": "A storage team deployed Dynamo-style partitioning across 4 cache nodes with `virtual_nodes_per_server = 1`. Telemetry shows Node 2 handling 68% of all production traffic while Node 1 sits at 4%.",
                        "code": """flowchart TD
    Ring["Ring [0..360 deg]"] --> N1["N1 at 10 deg"]
    N1 --> N2["N2 at 250 deg (Owns huge 240-deg arc 10..250!)"]
    N2 --> N3["N3 at 275 deg"]
    N3 --> N4["N4 at 355 deg"]""",
                        "question": "Why is Node 2 carrying 68% of traffic despite uniform hash keys, and what is the direct fix?",
                        "options": [
                            "With `virtual_nodes = 1`, random server hashes cluster unevenly leaving Node 2 owning a 240-degree arc; increasing to 100–200 Virtual Nodes per server evens arc coverage",
                            "SHA-256 produces negative integers on odd ports",
                            "Consistent hashing works ONLY when the number of nodes is a power of 3",
                            "Nodes must walk counter-clockwise instead of clockwise"
                        ],
                        "answer": "With `virtual_nodes = 1`, random server hashes cluster unevenly leaving Node 2 owning a 240-degree arc; increasing to 100–200 Virtual Nodes per server evens arc coverage",
                        "remedy": "Configure `vnodes = 150` per physical node (hashed as `f'{node_id}#v{i}'`) so every server owns 150 thin randomized slices around the entire circle."
                    }
                ]
            },
            {
                "title": "Module 4: Code Lab — Implement ConsistentHashRing with Virtual Nodes & Binary Search",
                "blocks": [
                    {
                        "type": "code_lab",
                        "language": "python",
                        "title": "Build a Production Consistent Hash Ring with Binary Search",
                        "instruction": "Implement `class ConsistentHashRing:` using **MD5/SHA-256 hashing (`hashlib`)** and **`bisect.bisect_right`** for **$O(\\log(N \\cdot V))$** clockwise lookup!\n\nRequired methods:\n- `__init__(self, vnodes: int = 100)`\n- `add_node(self, node: str) -> None`: Insert `vnodes` sorted positions (`f\"{node}#{i}\"`) onto `self.ring` and map `pos -> node`.\n- `remove_node(self, node: str) -> None`: Remove all virtual node positions belonging to `node`.\n- `get_node(self, key: str) -> Optional[str]`: Return clockwise owner (wrapping to `self.ring[0]` if past the largest token), or `None` if empty.",
                        "starter_code": "import bisect\nimport hashlib\n\nclass ConsistentHashRing:\n    def __init__(self, vnodes: int = 100):\n        self.vnodes = vnodes\n        self.ring = []       # sorted integer hashes\n        self.pos_to_node = {}\n\n    def _hash(self, s: str) -> int:\n        return int(hashlib.md5(s.encode('utf-8')).hexdigest()[:8], 16)\n\n    def add_node(self, node: str) -> None:\n        # TODO: insert virtual nodes sorted onto ring\n        pass\n\n    def remove_node(self, node: str) -> None:\n        # TODO: remove virtual nodes belonging to node\n        pass\n\n    def get_node(self, key: str):\n        # TODO: clockwise bisect lookup with wrap-around\n        return None\n",
                        "solution_code": "import bisect\nimport hashlib\n\nclass ConsistentHashRing:\n    def __init__(self, vnodes: int = 100):\n        self.vnodes = vnodes\n        self.ring = []\n        self.pos_to_node = {}\n\n    def _hash(self, s: str) -> int:\n        return int(hashlib.md5(s.encode('utf-8')).hexdigest()[:8], 16)\n\n    def add_node(self, node: str) -> None:\n        for i in range(self.vnodes):\n            h = self._hash(f\"{node}#{i}\")\n            if h not in self.pos_to_node:\n                self.pos_to_node[h] = node\n                bisect.insort(self.ring, h)\n\n    def remove_node(self, node: str) -> None:\n        to_del = [h for h, n in self.pos_to_node.items() if n == node]\n        for h in to_del:\n            del self.pos_to_node[h]\n            idx = bisect.bisect_left(self.ring, h)\n            if idx < len(self.ring) and self.ring[idx] == h:\n                self.ring.pop(idx)\n\n    def get_node(self, key: str):\n        if not self.ring:\n            return None\n        h = self._hash(key)\n        idx = bisect.bisect_right(self.ring, h)\n        if idx == len(self.ring):\n            idx = 0\n        return self.pos_to_node[self.ring[idx]]\n",
                        "test_code": "ring = ConsistentHashRing(vnodes=120)\nfor srv in ['cache-A', 'cache-B', 'cache-C', 'cache-D']:\n    ring.add_node(srv)\n\nkeys = [f'user:{i}' for i in range(2000)]\nbefore = {k: ring.get_node(k) for k in keys}\ncounts = {s: sum(1 for v in before.values() if v == s) for s in ['cache-A', 'cache-B', 'cache-C', 'cache-D']}\nassert all(300 <= c <= 700 for c in counts.values()), f'Skewed VNode distribution: {counts}'\n\nring.add_node('cache-E')\nafter = {k: ring.get_node(k) for k in keys}\nmoved = sum(1 for k in keys if before[k] != after[k])\nassert moved < 550, f'Too many keys moved on 4->5 expansion: {moved}/2000 (expected ~400)'\nring.remove_node('cache-E')\nrestored = {k: ring.get_node(k) for k in keys}\nassert restored == before, 'Removing node E must cleanly restore exact original mapping!'\nprint(f'RING_VERIFIED: dist={counts} moved_on_scale={moved}/2000 ({moved/20:.1f}%)')",
                        "hint": "Use `bisect.insort(self.ring, h)` (or sort once) when adding, `bisect_right(self.ring, h)` wrapped via `if idx == len(self.ring): idx = 0` when looking up, and filter/pop cleanly on `remove_node`.",
                        "why_it_works": "Mapping `vnodes=120` tokens per physical node reduces statistical variance below ~10%, while `bisect_right` walks clockwise in $O(\\log(N \\cdot V))$ time and adding a 5th node moves only `~1/5 = ~20%` of keys instead of `80%` with modulo hashing!",
                        "complexity": "**Lookup:** $O(\\log(N \\cdot V))$.\n**Key Churn on Add/Remove Node:** $O(K / N)$ optimal.",
                        "alternatives": [
                            {"title": "Jump Consistent Hash (Google)", "desc": "O(ln N) time, ZERO memory ring storage! Fast & uniform, but requires integer node IDs `0..N-1` (cannot remove an arbitrary middle node like `cache-B`)."},
                            {"title": "Rendezvous Hashing (HRW)", "desc": "Computes `score(key, node)` for all N nodes and picks max — works with arbitrary node failures without ring state in $O(N)$."}
                        ],
                        "edge_cases": [
                            {"title": "Token Hash Collisions Between Different Nodes", "desc": "With 32-bit hashes across thousands of VNodes, birthday paradox collisions are non-zero—guard `if h not in self.pos_to_node` (or use 64-bit hashes)."},
                            {"title": "Wrap-Around Past Largest Ring Position", "desc": "When `bisect_right(ring, h) == len(ring)`, wrap `idx = 0` back around the circle!"}
                        ]
                    }
                ]
            }
        ]
    }
}
