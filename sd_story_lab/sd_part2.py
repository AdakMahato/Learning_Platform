"""
System Design Story Lab - Part 2: Cases 5 to 9
Covers:
  - Case 5: CAP, PACELC, Quorums & Raft Consensus
  - Case 6: API Gateways & Token Bucket Rate Limiter Code Lab
  - Case 7: Distributed Snowflake Unique IDs Code Lab
  - Case 8: HLD Case Study I — URL Shortener (Base62 Code Lab)
  - Case 9: HLD Case Study II — Real-Time Chat (WebSockets & Ordering)
"""

SD_CASES_PART2 = {
    "5": {
        "title": "Split-Brain Survivors: CAP, PACELC, Quorums & Raft",
        "episodes": [
            {
                "title": "Module 1: CAP Reality Check & PACELC Latency-vs-Consistency",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Cross-Rack Split-Brain Double Spend",
                        "content": "A rack top-of-rack switch dropped packets between two storage halves for 40 seconds. Both halves thought the other was dead, promoted themselves Primary Leader, and approved **competing withdrawals from the exact same checking balance**!\n\n> [!IMPORTANT]\n> **CAP Theorem Corrected:** Network Partitions (**P**) WILL happen over physical hardware. Therefore, during a partition, a distributed data store MUST choose either **CP (Reject conflicting writes to preserve Linearizability)** or **AP (Accept writes on both sides and resolve conflicts later)**!"
                    },
                    {
                        "type": "concept",
                        "title": "CAP -> PACELC: Why Latency Matters Even When Healthy",
                        "content": "CAP only describes behavior *during a partition*. **PACELC** adds the healthy-network trade-off:\n\n- **If there is a Partition (P):** choose between **Availability (A)** or **Consistency (C)**.\n- **Else (E, normal operation):** choose between lower **Latency (L)** (async replication) or stronger **Consistency (C)** (synchronous quorum before ACK)!\n\nExamples:\n- **PC / EC (`ZooKeeper`, `etcd`, `Google Spanner`):** Always strictly consistent (`Raft`/`Paxos`), pays quorum RTT on writes.\n- **PA / EL (`Cassandra` default, `Dynamo`):** Always available and ultra-low local write latency; reconciles conflicts via **Last-Write-Wins (LWW)** or **CRDTs / Vector Clocks**.",
                        "technical_explanation": "**Fencing Tokens Prevent Zombie Leaders:** Even after Partition ends, an old paused leader (e.g. long JVM Stop-the-World GC pause!) might wake up and commit a stale write. Every Raft/Lease grant must attach a **monotonically increasing Fencing Token** checked by storage nodes to reject stale epoch writes!"
                    },
                    {
                        "type": "comparison_table",
                        "title": "PACELC Production Database Profiles",
                        "headers": ["System", "PACELC Profile", "Replication Protocol", "Ideal Workload"],
                        "rows": [
                            ["etcd / ZooKeeper", "PC / EC", "Raft / ZAB Majority Quorum", "Service discovery, leader leases, config"],
                            ["Google Spanner", "PC / EC", "Paxos + TrueTime atomic clocks", "Global strongly consistent financial ledger"],
                            ["Apache Cassandra", "PA / EL (tunable)", "Leaderless Quorum (R, W)", "High write ingestion telemetry, timelines"],
                            ["MongoDB (default)", "PC / EC", "Single Primary + Oplog", "General operational document store"]
                        ]
                    }
                ]
            },
            {
                "title": "Module 2: Raft Consensus & Leaderless Quorums (R + W > N)",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "How Raft Elects Leaders & Guarantees Committed Entries Survive",
                        "content": "1. **Randomized Election Timers (`150ms–300ms`):** Prevents split-vote livelock among followers.\n2. **Term Numbers:** Logical clock incrementing on every election; any node seeing a higher `term` immediately steps down to Follower.\n3. **Majority Commit (`floor(N/2) + 1`):** Leader appends to its local WAL, sends `AppendEntries` RPCs, and marks entry **committed** ONLY after a **strict majority** ACKs. Thus any future majority Leader Election overlaps at least 1 voter holding every committed record!",
                        "technical_explanation": "**Sloppy Quorum & Hinted Handoff (AP Mode):** When partition prevents contacting `W` home replicas, Dynamo accepts writes onto `W` reachable fallback nodes (`Sloppy Quorum`) with a `hint` header—preserving 100% write Availability while temporarily sacrificing strict `R + W > N` read freshness until network heals!"
                    },
                    {
                        "type": "visual",
                        "title": "Raft Log Replication Commit Flow (3 Nodes)",
                        "code": """sequenceDiagram
    participant C as Client
    participant L as Raft Leader (Term 4)
    participant F1 as Follower 1
    participant F2 as Follower 2
    C->>L: SET balance = 500
    L->>F1: AppendEntries(idx=12, term=4)
    L->>F2: AppendEntries(idx=12, term=4)
    F1-->>L: ACK (Majority = 2/3 reached!)
    L-->>C: Commit OK! (Apply to state machine)"""
                    }
                ]
            },
            {
                "title": "Module 3: Strict Quorum Math & Split-Brain Fencing Bug Hunt",
                "blocks": [
                    {
                        "type": "calculation_challenge",
                        "title": "Minimum Read Quorum Size for Strong Consistency",
                        "formula": "Strict Quorum overlap guarantee: R + W > N",
                        "question": "A Dynamo-style ring replicates each partition across **$N = 5$** replicas, and configures Write Quorum **$W = 3$**. What is the **minimum Read Quorum $R$** required to guarantee every read sees at least one copy of the latest committed write?",
                        "answer": "3",
                        "alternatives": ["3"],
                        "step_by_step": "By Pigeonhole Principle, we need $R + W > N \\implies R + 3 > 5 \\implies R \\ge \\mathbf{3}$. Then any read set of 3 nodes and write set of 3 nodes among 5 MUST overlap in at least $3 + 3 - 5 = 1$ up-to-date node!"
                    },
                    {
                        "type": "debugger",
                        "title": "Bug Hunt: Stale Lease GC-Pause Split-Brain",
                        "code": """# Lock server grants lease to Worker A (no epoch/fencing token sent to storage!)
if lock_service.acquire("shard-7"):
    # Worker A pauses 35s for Stop-the-World GC! Lock expires; Worker B acquires it!
    storage.write_file("shard-7/ledger.dat", old_data)  # Executes after GC wakes!""",
                        "question": "Worker A held a valid lock lease when entering GC, then woke up after lease expiry and overwrote Worker B's newer write! Why didn't Redis Redlock / ZooKeeper lock alone prevent this corruption?",
                        "options": [
                            "The storage server performed zero fencing-token monotonicity check (`token >= last_seen_token`) when accepting `write_file`",
                            "Stop-the-World GC corrupts local TCP checksums inside `write_file`",
                            "Distributed locks require odd lock names to avoid hash collisions",
                            "Worker B should sleep 60 seconds before writing"
                        ],
                        "answer": "The storage server performed zero fencing-token monotonicity check (`token >= last_seen_token`) when accepting `write_file`",
                        "explanation": "Distributed locks are **advisory** unless the downstream storage engine enforces an increasing **Fencing Token** returned by the lock service and rejects requests carrying stale tokens!"
                    }
                ]
            },
            {
                "title": "Module 4: Choosing CP vs AP & Consensus Cluster Sizing",
                "blocks": [
                    {
                        "type": "scenario_decision",
                        "title": "Designing Two Systems Across a Multi-Region Link",
                        "scenario": "You architect (A) a **Bank Double-Entry Account Ledger** and (B) a **Shopping Cart ('Add to Cart') Service** for an international retailer experiencing intermittent cross-ocean WAN partitions.",
                        "question": "Which CAP pairings maximize safety for the Ledger AND conversion revenue for the Cart?",
                        "options": [
                            "CP (Raft/Paxos synchronous majority quorum) for the Bank Ledger; AP (Async multi-region writes + conflict-free set merge CRDTs) for the Shopping Cart",
                            "AP with Last-Write-Wins timestamps for the Bank Ledger; CP halting checkouts worldwide on any WAN hiccup for the Cart",
                            "Run single-node MySQL without replication for both services",
                            "Switch both to UDP fire-and-forget broadcasts"
                        ],
                        "answer": "CP (Raft/Paxos synchronous majority quorum) for the Bank Ledger; AP (Async multi-region writes + conflict-free set merge CRDTs) for the Shopping Cart",
                        "rationale": "Overdrafts/double-spends violate financial invariants so Ledger MUST be **CP**; Amazon famously proved losing a customer's 'Add to Cart' click directly loses revenue, whereas merging concurrent cart items (`AP + CRDTs`) almost always matches user intent!"
                    },
                    {
                        "type": "fill_in_the_blank",
                        "title": "Raft Fault Tolerance Odd-Cluster Rule",
                        "question": "To tolerate up to `F = 2` simultaneous server crashes under Raft consensus, the minimum cluster size must be `2*F + 1 =` _____ nodes.",
                        "answer": "5",
                        "alternatives": ["5", "five"],
                        "explanation": "With `5` nodes, losing `2` leaves `3 >= floor(5/2) + 1 = 3` nodes alive to maintain a majority quorum! (A `4`-node cluster also only tolerates `1` failure, so odd sizes `3, 5, 7` minimize hardware cost per fault tolerated.)"
                    }
                ]
            }
        ]
    },
    "6": {
        "title": "API Shield: Gateways & Distributed Rate Limiters",
        "episodes": [
            {
                "title": "Module 1: Rate Limiting Algorithms & Edge Boundary Spikes",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Fixed-Window 2x Boundary Stampede",
                        "content": "An API Gateway enforced a **Fixed Window (`100 req / minute`)**. A scrapers botnet learned the clock reset boundary and fired **100 requests at `12:00:59` + 100 MORE at `12:01:01`**—pushing **`200 requests` within 2 seconds** cleanly past the limiter and crashing downstream Postgres!\n\n> [!IMPORTANT]\n> **Algorithm Selection Matters:** Smooth traffic, permit intentional short bursts cleanly, or prevent boundary 2x spikes using **Token Bucket**, **Leaky Bucket**, or **Sliding Window Counter**!"
                    },
                    {
                        "type": "concept",
                        "title": "Comparing the Four Industry Rate-Limiting Algorithms",
                        "content": "1. **Token Bucket (Stripe, AWS API Gateway):** Bucket holds up to `capacity` tokens, refilling smoothly at `refill_rate` tokens/sec. Every request removes 1 token (else `429 Too Many Requests`). **Allows short bursts up to `capacity`**, steady average rate `refill_rate`, tiny $O(1)$ state `(tokens, last_ts)`!\n2. **Leaky Bucket (NGINX `limit_req`):** Requests enter a bounded FIFO queue drained at a strict **constant outflow rate**. Smooths choppy traffic spikes completely.\n3. **Sliding Window Log:** Stores every request timestamp in a Redis Sorted Set (`ZSET`), pruning timestamps `< now - window`. **Exact accuracy**, high RAM if `limit` is huge.\n4. **Sliding Window Counter (Cloudflare):** Weighted average of `prev_window` and `curr_window` counters—near-exact precision in **$O(1)$ RAM**!",
                        "technical_explanation": "**HTTP `429` Standard Response Headers:** Return `HTTP 429 Too Many Requests` along with `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and `X-RateLimit-Reset` (or `Retry-After`) so well-behaved SDK clients back off cleanly!"
                    },
                    {
                        "type": "comparison_table",
                        "title": "Rate Limiter Algorithm Selection Matrix",
                        "headers": ["Algorithm", "Handles Bursts?", "Boundary 2x Spike?", "Memory per User"],
                        "rows": [
                            ["Token Bucket", "Yes (up to capacity)", "No", "O(1) — 2 numbers!"],
                            ["Leaky Bucket", "No (queues & smooths)", "No", "O(queue size)"],
                            ["Fixed Window Counter", "Yes at start", "YES (2x spike at edges!)", "O(1) — 1 integer"],
                            ["Sliding Window Log", "Yes up to limit", "No (exact precision)", "O(limit) timestamps"]
                        ]
                    }
                ]
            },
            {
                "title": "Module 2: Distributed Redis Lua Atomicity & Gateway Architecture",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Why Check-Then-Set Fails Across 20 Stateless API Gateways",
                        "content": "If Gateway Pod A and Pod B both execute two separate Redis commands (`GET tokens` -> compute -> `SET tokens`) under concurrency, **both read `tokens = 1` simultaneously** and BOTH admit requests—breaking quota limits!\n\n- **Solution:** Execute read + refill + decrement + update inside ONE atomic **Redis Lua Script** (or `EVALSHA`)! Redis is single-threaded per shard, so the Lua block executes atomically with **1 network RTT** and zero TOCTOU race conditions!",
                        "technical_explanation": "**Fail-Open vs Fail-Closed:** If Redis Cluster briefly drops packets, critical checkout gateways often **fail-open** (allow requests briefly with local in-memory fallback limiters) rather than blocking 100% of paying customers!"
                    },
                    {
                        "type": "visual",
                        "title": "API Gateway + Redis Lua Atomic Rate Limiting Pipeline",
                        "code": """flowchart LR
    C["Client Request (API Key)"] --> GW["L7 API Gateway"]
    GW -->|EVALSHA TokenBucket Lua| R["Redis Cluster (1 RTT Atomic!)"]
    R -->|allowed=1| App["Forward to Backend Service"]
    R -->|allowed=0| R429["HTTP 429 + Retry-After Header"]"""
                    }
                ]
            },
            {
                "title": "Module 3: Distributed Race Bug Hunt & Global Quota Trade-offs",
                "blocks": [
                    {
                        "type": "debugger",
                        "title": "Bug Hunt: Non-Atomic Redis Counter Race & Leak",
                        "code": """def allow_request(user_id):
    key = f"rl:{user_id}:{int(time.time() // 60)}"
    cnt = int(redis.get(key) or 0)
    if cnt >= 100:
        return False
    redis.incr(key)
    if cnt == 0:
        redis.expire(key, 60)
    return True""",
                        "question": "Identify TWO critical concurrency flaws in this distributed Redis limiter snippet:",
                        "options": [
                            "1) Read (`GET`) -> Check -> `INCR` has a TOCTOU race admitting >100 concurrent requests; 2) If process crashes between `INCR` and `EXPIRE`, that key lives FOREVER in Redis RAM!",
                            "`time.time() // 60` cannot execute inside Python strings",
                            "Redis `INCR` decreases counters when passed an integer string",
                            "`EXPIRE 60` deletes the entire Redis database after 60 seconds"
                        ],
                        "answer": "1) Read (`GET`) -> Check -> `INCR` has a TOCTOU race admitting >100 concurrent requests; 2) If process crashes between `INCR` and `EXPIRE`, that key lives FOREVER in Redis RAM!",
                        "explanation": "Always bundle `INCR` + conditional `EXPIRE` (or Token Bucket refill math) inside a single atomic **Redis Lua script**!"
                    },
                    {
                        "type": "scenario_decision",
                        "title": "Enforcing Quotas Across US, EU, and APAC Edge Clusters",
                        "scenario": "You run independent API Gateways in `us-east`, `eu-west`, and `ap-south`. Sending every user request across oceans to one central US Redis adds `180 ms` latency per API call.",
                        "question": "How do real edge platforms enforce rate limits with `< 2 ms` local overhead?",
                        "options": [
                            "Keep a regional Redis per region (Geo-Sticky routing per user/API-key) or push periodic async quota gossip syncs with slight eventual tolerance",
                            "Block all EU and APAC traffic until US Redis responds synchronously",
                            "Disable TLS so packets travel faster than light",
                            "Store all per-request timestamps inside client browser cookies only"
                        ],
                        "answer": "Keep a regional Redis per region (Geo-Sticky routing per user/API-key) or push periodic async quota gossip syncs with slight eventual tolerance",
                        "rationale": "Users/tenants usually hit their nearest regional PoP consistently. Regional Redis enforcement guarantees `< 2 ms` check latency, while async cross-region credit leasing catches rare multi-region simultaneous bots."
                    }
                ]
            },
            {
                "title": "Module 4: Code Lab — Implement Fractional Token Bucket Rate Limiter",
                "blocks": [
                    {
                        "type": "code_lab",
                        "language": "python",
                        "title": "Implement Production Token Bucket Engine (Lazy Refill)",
                        "instruction": "Notice a production Token Bucket does NOT spawn background timer threads per user (`100M timers = instant OOM`!). Instead, it refills **lazily on request arrival** using elapsed wall/monotonic time!\n\nImplement `class TokenBucketLimiter:`:\n- `__init__(self, capacity: float, refill_rate_per_sec: float, clock)`: Stores bucket state `(tokens, last_ts)` per `user_id`, seeded at full `capacity` on first request.\n- `allow(self, user_id: str) -> bool`:\n  1. Compute `now = self.clock()`.\n  2. Refill lazily: `tokens = min(capacity, tokens + (now - last_ts) * refill_rate)`.\n  3. Update `last_ts = now`. If `tokens >= 1.0`, subtract `1.0`, save state, return `True`; else save refilled state and return `False`!",
                        "starter_code": "class TokenBucketLimiter:\n    def __init__(self, capacity: float, refill_rate: float, clock):\n        self.capacity = float(capacity)\n        self.refill_rate = float(refill_rate)\n        self.clock = clock\n        self.buckets = {}  # user_id -> [tokens, last_ts]\n\n    def allow(self, user_id: str) -> bool:\n        # TODO: lazy refill capped at self.capacity, consume 1 token if >= 1.0\n        return False\n",
                        "solution_code": "class TokenBucketLimiter:\n    def __init__(self, capacity: float, refill_rate: float, clock):\n        self.capacity = float(capacity)\n        self.refill_rate = float(refill_rate)\n        self.clock = clock\n        self.buckets = {}\n\n    def allow(self, user_id: str) -> bool:\n        now = self.clock()\n        if user_id not in self.buckets:\n            tokens = self.capacity\n        else:\n            prev_tokens, last_ts = self.buckets[user_id]\n            elapsed = max(0.0, now - last_ts)\n            tokens = min(self.capacity, prev_tokens + elapsed * self.refill_rate)\n        if tokens >= 1.0:\n            self.buckets[user_id] = [tokens - 1.0, now]\n            return True\n        self.buckets[user_id] = [tokens, now]\n        return False\n",
                        "test_code": "t = [100.0]\nlim = TokenBucketLimiter(capacity=3, refill_rate=2.0, clock=lambda: t[0])\nassert [lim.allow('u1') for _ in range(4)] == [True, True, True, False], 'Burst of 3 allowed, 4th rejected!'\nt[0] += 0.25  # +0.5 tokens (still < 1.0)\nassert lim.allow('u1') is False, 'Only 0.5 tokens accumulated so must remain rejected'\nt[0] += 0.25  # +0.5 more -> 1.0 token total!\nassert lim.allow('u1') is True, 'Full 1.0 token accumulated over 0.5s at 2/s rate'\nt[0] += 10.0  # long idle -> cap cleanly at capacity=3 (NOT 20 tokens!)\nassert [lim.allow('u1') for _ in range(4)] == [True, True, True, False], 'Must cap at capacity=3!'\nassert lim.allow('u2') is True, 'Separate tenant buckets must remain isolated'\nprint('TOKEN_BUCKET_VERIFIED: lazy refill, fractional accrual & capacity cap passed!')",
                        "expected_output": "TOKEN_BUCKET_VERIFIED: lazy refill, fractional accrual & capacity cap passed!",
                        "hint": "Store `[tokens, last_ts]` per key; guard `max(0.0, now - last_ts)` and `min(self.capacity, ...)` so an idle user cannot bank infinite burst credits beyond `capacity`!",
                        "why_it_works": "**Lazy on-demand calculation** turns millions of timers into pure $O(1)$ math per request (`2 floats` in memory—trivial to move directly into a Redis Hash or Lua script!).",
                        "complexity": "**Time:** $O(1)$ per check.\n**Space:** $O(\\text{Active Users})$ with Redis `TTL` auto-evicting idle entries.",
                        "alternatives": [
                            {"title": "Redis Cell / GCRA (Generic Cell Rate Algorithm)", "desc": "Stores just ONE timestamp (`TAT` — Theoretical Arrival Time) instead of two floats (`tokens, last_ts`) while delivering mathematically identical Leaky/Token Bucket smoothness!"}
                        ],
                        "edge_cases": [
                            {"title": "Fractional Remainder Preserved on Rejection", "desc": "Updating `last_ts = now` AND keeping the accumulated `0.5` token lets the next call `0.25s` later reach `1.0` smoothly without losing accrued credit!"},
                            {"title": "Long-Idle Burst Clamping", "desc": "`min(capacity, ...)` guarantees no user accumulates 1 million bursts after a week idle."}
                        ]
                    }
                ]
            }
        ]
    },
    "7": {
        "title": "Sequence Without Locks: Distributed Snowflake IDs",
        "episodes": [
            {
                "title": "Module 1: Why UUIDv4 Hurts Databases & Auto-Increment Bottlenecks",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The UUIDv4 B-Tree Page Thrashing Incident",
                        "content": "Switching `orders.id` from a 64-bit integer to **random 128-bit UUIDv4** solved distributed generation—until table size hit 80M rows. Write IOPS suddenly exploded **7x** and InnoDB Buffer Pool hit rate plunged!\n\n> [!IMPORTANT]\n> **Database Storage Mechanics:** Clustered B-Tree primary keys store rows physically sorted by ID! **Random UUIDv4** forces every single `INSERT` into a random cold B-Tree leaf page (causing disk page splits & dirty-page eviction), whereas **time-ordered 64-bit Snowflake / UUIDv7** appends cleanly to the warm **rightmost leaf page**!"
                    },
                    {
                        "type": "comparison_table",
                        "title": "Distributed Unique ID Generation Strategies",
                        "headers": ["Approach", "Bit Width", "K-Sortable (Time Ordered)?", "Central Bottleneck?"],
                        "rows": [
                            ["DB `AUTO_INCREMENT`", "64-bit", "Yes", "YES (Single writer / multi-master step hacks)"],
                            ["Random `UUIDv4`", "128-bit", "NO — causes random B-Tree page splits!", "None (local compute)"],
                            ["Flickr Ticket Server + Stride", "64-bit", "Mostly", "SPOF unless partitioned across odd/even"],
                            ["Twitter Snowflake / UUIDv7", "64-bit / 128-bit", "YES — sequential B-Tree inserts!", "None (worker_id assigned once via ZooKeeper/etcd)"]
                        ]
                    }
                ]
            },
            {
                "title": "Module 2: Dissecting the 64-Bit Snowflake Bit Layout & Clock Drift",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Twitter / Discord 64-Bit Snowflake Architecture",
                        "content": "Every unsigned positive 64-bit integer is partitioned cleanly with bitshifts:\n\n- **`1` bit (MSB):** Always `0` (keeps value positive signed `int64`).\n- **`41` bits:** Milliseconds since custom Epoch (e.g., `2020-01-01`) -> **$2^{41} \\text{ ms} \\approx 69.7\\text{ years}$**!\n- **`10` bits:** `5` bits Datacenter ID (`0..31`) + `5` bits Machine ID (`0..31`) = **1,024 independent generator nodes**.\n- **`12` bits:** Per-millisecond sequence counter (`0..4095`) -> **4,096 unique IDs per ms per worker = 4.096 Million IDs/sec per node**!",
                        "technical_explanation": "**What Happens If NTP Steps the System Clock Backward?** If `now_ms < last_ts`, generating IDs could **collide** with previously emitted IDs! Safe Snowflake generators either (a) **reject/raise `ClockMovedBackwardsError`** or sleep briefly if drift `< 5 ms`, or (b) allocate spare sequence bits / logical sequence bump."
                    },
                    {
                        "type": "visual",
                        "title": "64-Bit Snowflake Bitfield Packing",
                        "code": """flowchart LR
    S["1 bit: Sign (0)"] --> TS["41 bits: Delta Timestamp ms (~69 yrs)"]
    TS --> DC["5 bits: Datacenter ID (0..31)"]
    DC --> WK["5 bits: Worker ID (0..31)"]
    WK --> SQ["12 bits: Sequence Counter (0..4095/ms)"]"""
                    }
                ]
            },
            {
                "title": "Module 3: Snowflake Capacity Math & Fill-In-The-Blank",
                "blocks": [
                    {
                        "type": "calculation_challenge",
                        "title": "Snowflake Cluster Peak Throughput Bound",
                        "question": "Each Snowflake node holds **12 sequence bits** (`0..4095` per millisecond). If one datacenter operates **10 worker nodes**, what is the maximum number of unique IDs generated per **single millisecond** across those 10 nodes combined?",
                        "answer": "40960",
                        "alternatives": ["40960", "40,960"],
                        "step_by_step": "Each node generates $2^{12} = 4,096$ IDs per ms. Across `10` nodes: $10 \\times 4,096 = \\mathbf{40,960\\text{ IDs/ms}}$ (i.e., **40.96 million IDs/sec**!)."
                    },
                    {
                        "type": "fill_in_the_blank",
                        "title": "Modern 128-Bit Sequential UUID Standard",
                        "question": "Whereas `UUIDv4` places random bits in the leading positions causing B-Tree page fragmentation, the modern RFC 9562 time-ordered standard that puts a 48-bit Unix millisecond timestamp FIRST is _____.",
                        "answer": "UUIDv7",
                        "alternatives": ["UUIDv7", "uuidv7", "UUID v7"],
                        "explanation": "**UUIDv7** combines 48-bit millisecond chronological prefix ordering (great B-Tree locality!) with 74 random bits so no `worker_id` coordination service is even needed when 128 bits are acceptable."
                    }
                ]
            },
            {
                "title": "Module 4: Code Lab — Implement Bit-Packed Snowflake Generator with Clock Guards",
                "blocks": [
                    {
                        "type": "code_lab",
                        "language": "python",
                        "title": "Build a 64-Bit Snowflake ID Generator & Decoder",
                        "instruction": "Implement `class SnowflakeGenerator:` packing `(timestamp - epoch) << 22 | (dc_id << 17) | (worker_id << 12) | seq`!\n\nRequirements:\n1. Validate `0 <= dc_id <= 31` and `0 <= worker_id <= 31`.\n2. Track `last_ts` and `seq` (`0..4095`).\n3. **Clock Rollback Guard:** If `now_ms < self.last_ts`, raise `RuntimeError('Clock moved backwards')`.\n4. **Sequence Overflow Spin:** If `now_ms == self.last_ts`, increment `seq = (seq + 1) & 4095`. If `seq == 0` (exhausted 4096 IDs in this millisecond!), advance/poll `clock_fn()` until `now_ms > last_ts`.\n5. Implement `decode(snowflake_id: int) -> dict` returning `{'ts_delta', 'dc_id', 'worker_id', 'seq'}` via bitmasks!",
                        "starter_code": "class SnowflakeGenerator:\n    def __init__(self, dc_id: int, worker_id: int, epoch_ms: int = 1700000000000, clock_ms_fn=None):\n        if not (0 <= dc_id < 32 and 0 <= worker_id < 32):\n            raise ValueError('dc_id and worker_id must be 0..31')\n        self.dc_id = dc_id\n        self.worker_id = worker_id\n        self.epoch_ms = epoch_ms\n        self.clock_ms_fn = clock_ms_fn\n        self.last_ts = -1\n        self.seq = 0\n\n    def next_id(self) -> int:\n        # TODO: handle clock rollback, same-ms seq rollover, and pack 64 bits\n        return 0\n\n    def decode(self, sid: int) -> dict:\n        # TODO: extract ts_delta, dc_id, worker_id, seq using bitmasks\n        return {}\n",
                        "solution_code": "class SnowflakeGenerator:\n    def __init__(self, dc_id: int, worker_id: int, epoch_ms: int = 1700000000000, clock_ms_fn=None):\n        if not (0 <= dc_id < 32 and 0 <= worker_id < 32):\n            raise ValueError('dc_id and worker_id must be 0..31')\n        self.dc_id = dc_id\n        self.worker_id = worker_id\n        self.epoch_ms = epoch_ms\n        self.clock_ms_fn = clock_ms_fn\n        self.last_ts = -1\n        self.seq = 0\n\n    def next_id(self) -> int:\n        now = self.clock_ms_fn()\n        if now < self.last_ts:\n            raise RuntimeError('Clock moved backwards')\n        if now == self.last_ts:\n            self.seq = (self.seq + 1) & 0xFFF\n            if self.seq == 0:\n                while now <= self.last_ts:\n                    now = self.clock_ms_fn()\n        else:\n            self.seq = 0\n        self.last_ts = now\n        delta = now - self.epoch_ms\n        return (delta << 22) | (self.dc_id << 17) | (self.worker_id << 12) | self.seq\n\n    def decode(self, sid: int) -> dict:\n        seq = sid & 0xFFF\n        worker_id = (sid >> 12) & 0x1F\n        dc_id = (sid >> 17) & 0x1F\n        ts_delta = sid >> 22\n        return {'ts_delta': ts_delta, 'dc_id': dc_id, 'worker_id': worker_id, 'seq': seq}\n",
                        "test_code": "clk = [1700000005000]\ng = SnowflakeGenerator(dc_id=3, worker_id=19, epoch_ms=1700000000000, clock_ms_fn=lambda: clk[0])\nid0 = g.next_id()\nid1 = g.next_id()\nassert id1 > id0 and id1 - id0 == 1, 'Same-ms IDs must increase sequentially by 1'\nd = g.decode(id1)\nassert d == {'ts_delta': 5000, 'dc_id': 3, 'worker_id': 19, 'seq': 1}, f'Bad decode: {d}'\n# Test sequence overflow across 4096 same-ms calls using auto-advancing mock clock:\ncalls = [0]\ndef rollover_clk():\n    calls[0] += 1\n    if calls[0] <= 4098: return 1700000006000\n    return 1700000006001\ng2 = SnowflakeGenerator(dc_id=1, worker_id=2, epoch_ms=1700000000000, clock_ms_fn=rollover_clk)\nids = [g2.next_id() for _ in range(4097)]\nassert len(set(ids)) == 4097 and all(ids[i] < ids[i+1] for i in range(4096)), 'Sequence rollover must remain strictly unique & monotonic!'\n# Test clock rollback protection:\ntry:\n    clk[0] = 1700000004000\n    g.next_id()\n    assert False, 'Expected RuntimeError on clock rollback!'\nexcept RuntimeError:\n    pass\nprint('SNOWFLAKE_VERIFIED: bit-packing, 4096-seq rollover & rollback guard passed!')",
                        "expected_output": "SNOWFLAKE_VERIFIED: bit-packing, 4096-seq rollover & rollback guard passed!",
                        "hint": "Use bitmasks `0xFFF` (12 bits = 4095) and `0x1F` (5 bits = 31). On `self.seq == 0` in the same millisecond, loop `while now <= self.last_ts: now = self.clock_ms_fn()`.",
                        "why_it_works": "Zero database round-trips or locks! Every server autonomously issues monotonically increasing 64-bit K-sortable primary keys with `4,096/ms` local throughput and clean database B-Tree locality.",
                        "complexity": "**Time:** $O(1)$ bit shifts per ID.\n**Space:** $O(1)$.",
                        "alternatives": [
                            {"title": "PostgreSQL / DB Hi-Lo Sequence Batching", "desc": "Allocate blocks of 1,000 IDs at a time (`UPDATE seq SET val = val + 1000`) so the central DB only sees 1 RPC per 1,000 IDs!"}
                        ],
                        "edge_cases": [
                            {"title": "Negative Clock Delta (`now < last_ts`)", "desc": "NTP slew or VM snapshot migration stepping wall clock backward must trigger rollback protection (`CLOCK_MONOTONIC` deltas or small spin-wait) so IDs never duplicate!"}
                        ]
                    }
                ]
            }
        ]
    },
    "8": {
        "title": "HLD Case Study I: Hyperscale URL Shortener (TinyURL)",
        "episodes": [
            {
                "title": "Module 1: Requirements, 100:1 Read Funnel & 301 vs 302 Analytics",
                "blocks": [
                    {
                        "type": "story",
                        "title": "The Missing Click Analytics Mystery",
                        "content": "Marketing launched a TinyURL campaign using **`HTTP 301 Moved Permanently`**, expecting click-tracking dashboards to show regional conversion rates. Total logged clicks stopped growing after day 1—even though millions clicked the link! Why? **Chrome/Safari aggressively cached `301` permanently in browser disk cache** and skipped our redirect servers altogether!\n\n> [!IMPORTANT]\n> **Redirect Rule:** Use **`301 Permanently Moved`** ONLY when maximizing CDN/origin offload with zero per-click analytics needed. Use **`302 Found` (or `307`)** whenever servers MUST log clicks, A/B test targets, or enforce per-user expiration!"
                    },
                    {
                        "type": "concept",
                        "title": "High-Level Design: Write Path vs Ultra-Fast Read Path",
                        "content": "Assume **100M new URLs/month** (`~40 write QPS`) and a **100:1 read-to-write ratio (`~4,000 avg read QPS`, `~12,000 peak read QPS`)**:\n\n1. **Write Service:** Receives long URL, checks optional `custom_alias`, allocates a unique 7-character **Base62** code (`[0-9a-zA-Z]`) via pre-generated Key Generation Service (**KGS**) or Snowflake/Distributed Counter, stores `(short_code -> long_url, expires_at)` in **NoSQL KV / Sharded RDBMS**, and returns `https://t.ly/a9BzK2p`.\n2. **Read Service (Hot Path):** Edge/API hits **Redis Cache (`80-20` zipfian power-law -> 20% hot links drive 80% reads)** first (`< 1 ms`), falls back to DB replica on miss, emits click telemetry asynchronously to **Kafka** so analytics NEVER add latency to the `302` redirect!",
                        "technical_explanation": "**Predictable Enumeration Warning:** If you naively encode sequential integer IDs `1, 2, 3 -> '1', '2', '3'` cleanly in Base62, competitors can scrape ALL your links and read exact daily business signup volume! Fix: XOR/Feistel-permute the ID bit pattern or allocate pre-shuffled random 7-char tokens from a **Key Generation Service (KGS)**!"
                    },
                    {
                        "type": "visual",
                        "title": "Scalable URL Shortener Read & Async Click-Analytics HLD",
                        "code": """flowchart LR
    U["Client Click /a9BzK2p"] --> LB["L4/L7 Load Balancer"]
    LB --> API["Redirect Service"]
    API -->|1. Check Hot URL| Redis["Redis Cache (Zipf Top 20%)"]
    Redis -->|Cache Miss| DB["KV Store / Sharded DB"]
    API -->|2. HTTP 302 Location| U
    API -.->|3. Fire & Forget Click Event| Kafka["Kafka -> ClickHouse Analytics"]"""
                    }
                ]
            },
            {
                "title": "Module 2: Base62 vs MD5 Truncation & Key Generation Service (KGS)",
                "blocks": [
                    {
                        "type": "comparison_table",
                        "title": "Short-Code Generation Mechanisms",
                        "headers": ["Strategy", "Collision Risk?", "Requires DB Lookup Check?", "Scaling Concurrency"],
                        "rows": [
                            ["MD5 / SHA-256 first 7 chars", "Yes (birthday collisions over billions)", "YES (check + retry/salt loop!)", "High write DB read penalty"],
                            ["Distributed Counter + Feistel + Base62", "Zero (mathematically 1-to-1)", "No", "High (Redis atomic INCR / range allocator)"],
                            ["Offline KGS Pre-Generated Token Batches", "Zero (pre-deduplicated offline)", "No (each app pod caches 10k unused keys in RAM!)", "Highest! Zero cross-node contention"]
                        ]
                    },
                    {
                        "type": "concept",
                        "title": "Key Generation Service (KGS) Fault-Tolerance",
                        "content": "KGS generates billions of random 7-character Base62 tokens offline into a `unused_keys` table and hands atomic batches of **10,000 keys** in memory to each API Server (moving keys to `used_keys`). If an API pod restarts, those remaining RAM keys are discarded (tiny `0.0001%` waste among 3.5 Trillion keys) rather than risking two pods ever issuing duplicates!"
                    }
                ]
            },
            {
                "title": "Module 3: Base62 Combinatorics & Redirect Status Decision",
                "blocks": [
                    {
                        "type": "calculation_challenge",
                        "title": "Minimum Base62 Short Code Length",
                        "question": "Suppose your URL shortener must support at least **3 billion distinct short URLs** using the 62-character alphabet (`0-9`, `a-z`, `A-Z`). Given $62^5 \\approx 916\\text{ million}$ and $62^6 \\approx 56.8\\text{ billion}$, what is the **minimum short-code character length** required?",
                        "answer": "6",
                        "alternatives": ["6", "6 chars", "6 characters"],
                        "step_by_step": "$62^5 = 916,132,832 < 3\\text{ billion}$, whereas **$62^6 = 56,800,235,584 \\approx 56.8\\text{ billion} > 3\\text{ billion}$**! Using 7 characters gives $62^7 \\approx 3.52\\text{ trillion}$ (standard TinyURL/bit.ly length)."
                    },
                    {
                        "type": "scenario_decision",
                        "title": "301 Permanent vs 302 Temporary for Paid Marketing Campaigns",
                        "scenario": "A brand customer buys TinyURL Enterprise specifically to measure real-time conversion funnels by country, device OS, and hour of day—and also wants the power to hot-swap destination URLs if a landing page breaks.",
                        "question": "Which HTTP status code MUST the redirect API return?",
                        "options": [
                            "`302 Found` (or `307 Temporary Redirect`) with `Cache-Control: private, no-store` so browsers/intermediaries still notify our origin on clicks",
                            "`301 Moved Permanently` with `max-age=31536000` so mobile browsers never talk to our server again",
                            "`404 Not Found` with an HTML meta-refresh tag",
                            "`503 Service Unavailable`"
                        ],
                        "answer": "`302 Found` (or `307 Temporary Redirect`) with `Cache-Control: private, no-store` so browsers/intermediaries still notify our origin on clicks",
                        "rationale": "`302 Found` instructs browsers/CDNs not to permanently pin the target location, giving your origin telemetry + instant destination-edit flexibility."
                    }
                ]
            },
            {
                "title": "Module 4: Code Lab — Implement Non-Sequential Bijective Base62 URL Codec",
                "blocks": [
                    {
                        "type": "code_lab",
                        "language": "python",
                        "title": "Implement Obfuscated Bijective Base62 Shortener Codec",
                        "instruction": "A clean distributed shortener avoids `1, 2, 3 -> '1', '2', '3'` guessability while keeping **zero collisions**! Notice that multiplying a positive ID inside a prime/coprime ring—or XORing with a fixed 36-bit secret mask **`SECRET_MASK = 0x5A3C9F2E1` (or reversing bit/modulus within a fixed power-of-2 capacity)**—is its OWN **bijective** inverse (`encode(decode(code)) == num` and NO two distinct positive IDs ever collide)!\n\nImplement `class URLCodec:` (`ALPHABET = \"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\"`):\n- `encode_id(self, seq_id: int) -> str`: Scramble `val = seq_id ^ 0x5A3C9F2E1` (plus `0` offset safety), convert to a **minimum 6-character Base62 string** (left-padded with `'0'`).\n- `decode_code(self, code: str) -> int`: Convert Base62 back to integer and XOR un-scramble `val ^ 0x5A3C9F2E1` to recover exact `seq_id`!",
                        "starter_code": "ALPHABET = \"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\"\n\nclass URLCodec:\n    MASK = 0x5A3C9F2E1\n\n    def encode_id(self, seq_id: int) -> str:\n        # TODO: XOR scramble, base-62 convert, right-justify to min length 6 with '0'\n        return ''\n\n    def decode_code(self, code: str) -> int:\n        # TODO: parse base-62 integer and XOR un-scramble back to seq_id\n        return -1\n",
                        "solution_code": "ALPHABET = \"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\"\nCHAR_TO_VAL = {c: i for i, c in enumerate(ALPHABET)}\n\nclass URLCodec:\n    MASK = 0x5A3C9F2E1\n\n    def encode_id(self, seq_id: int) -> str:\n        val = seq_id ^ self.MASK\n        if val == 0:\n            return '0' * 6\n        chars = []\n        while val > 0:\n            chars.append(ALPHABET[val % 62])\n            val //= 62\n        res = ''.join(reversed(chars))\n        return res.rjust(6, '0')\n\n    def decode_code(self, code: str) -> int:\n        val = 0\n        for ch in code:\n            val = val * 62 + CHAR_TO_VAL[ch]\n        return val ^ self.MASK\n",
                        "test_code": "codec = URLCodec()\nc1 = codec.encode_id(1)\nc2 = codec.encode_id(2)\nc3 = codec.encode_id(987654321)\nassert len(c1) >= 6 and len(c2) >= 6 and len(c3) >= 6\nassert c1 != c2, 'Sequential IDs must map cleanly to distinct tokens'\nassert not c2.endswith('2') or c1[-2:] != c2[-2:], 'XOR scrambling hides sequential pattern'\nassert codec.decode_code(c1) == 1 and codec.decode_code(c2) == 2 and codec.decode_code(c3) == 987654321\nseen = {codec.encode_id(i) for i in range(1, 500)}\nassert len(seen) == 499, 'Zero collisions guaranteed by bijective XOR + Base62!'\nprint(f'BASE62_VERIFIED: id=1->{c1}, id=2->{c2}, 499/499 unique bijective roundtrips!')",
                        "hint": "Repeatedly take `val % 62` and `val //= 62`, reverse characters, pad `.rjust(6, '0')`. Decoding multiplies `val = val * 62 + ALPHABET.index(ch)` and applies `val ^ self.MASK` back!",
                        "why_it_works": "Because XOR (`^`) with a constant mask is strictly **bijective** (`x ^ M == y ^ M <=> x == y`) AND base-62 positional representation is **bijective**, sequential IDs `1, 2, 3` transform into completely non-obvious random-looking codes with **zero DB collision lookups**!",
                        "complexity": "**Time:** $O(\\log_{62} N) \\le 11$ ops.\n**Space:** $O(1)$.",
                        "alternatives": [
                            {"title": "Key Generation Service (KGS)", "desc": "Truly random unpredictable strings stored in dedicated unused/used DB batches if cryptographic unpredictability is mandated."}
                        ],
                        "edge_cases": [
                            {"title": "Scramble Colliding to `val == 0`", "desc": "Handle `val == 0` explicitly so `.rjust(6, '0')` returns `'000000'` cleanly instead of an empty string!"},
                            {"title": "Case-Sensitive Alphabet Collisions in Legacy URLs", "desc": "Base62 differentiates `'a'` vs `'A'`—only deploy on case-sensitive HTTP paths."}
                        ]
                    }
                ]
            }
        ]
    },
    "9": {
        "title": "HLD Case Study II: Real-Time Chat (WhatsApp & Slack)",
        "episodes": [
            {
                "title": "Module 1: Real-Time Transport Mechanics & Stateful WebSockets",
                "blocks": [
                    {
                        "type": "story",
                        "title": "Why HTTP Polling Died at 500k Users",
                        "content": "Version 1.0 of a team messenger polled `/api/messages` over REST every `1 second`. With 500,000 online laptops, servers burned **500,000 QPS of empty HTTP 200 responses** (`99.4%` empty payloads!) just from TCP/HTTP headers!\n\n> [!IMPORTANT]\n> **Transport Switch:** Upgrading to persistent bidirectional **WebSockets** slashes idle network chatter to lightweight keepalive heartbeats while pushing incoming chats to clients in **`< 30 ms`**!"
                    },
                    {
                        "type": "comparison_table",
                        "title": "Real-Time Client-Server Transport Protocols",
                        "headers": ["Transport", "Direction", "Overhead", "Best Use Case"],
                        "rows": [
                            ["Short HTTP Polling", "Client -> Server", "Massive wasted headers/QPS", "Low-scale admin status pages"],
                            ["HTTP Long Polling", "Client holds open till event", "Re-opens HTTP on every message", "Legacy browser fallback"],
                            ["Server-Sent Events (SSE)", "Server -> Client only (HTTP/2)", "Ultra-low overhead!", "Stock tickers, LLM token streaming, notifications"],
                            ["WebSockets (RFC 6455)", "Full-Duplex Bidirectional", "2-byte framing header after upgrade", "1:1 / Group Chat, multiplayer gaming"]
                        ]
                    }
                ]
            },
            {
                "title": "Module 2: Service Discovery, Message Sync & Causal Ordering",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "How User A Sends a Chat to User B Across Different WebSocket Pods",
                        "content": "1. **Sticky Stateful Gateways:** Client A holds a persistent WebSocket on `ChatServer-12`; Client B holds a socket on `ChatServer-89`.\n2. **Session Directory (`Redis Cluster`):** Maps `user_id -> gateway_pod_ip`.\n3. **Relay & Offline Durability:**\n   - `ChatServer-12` persists the message to an **append-only distributed KV store (`Cassandra` / partitioned MySQL, keyed by `(channel_id, message_id)` sorted DESC!)**.\n   - Looks up `user_B -> ChatServer-89` and forwards via gRPC/Message Queue. If B is **offline**, enqueue an **APNs / FCM Push Notification** and let B sync `WHERE message_id > last_synced_id` on reconnect!",
                        "technical_explanation": "**Message Ordering & Deduplication:** Never trust mobile client wall clocks (`sender_time`) for bubble order! Generate a **monotonic Snowflake / per-conversation sequence ID** on the server AND attach a client-generated **UUID `client_msg_id` idempotency key** so flaky 4G retries never show duplicate bubbles!"
                    },
                    {
                        "type": "visual",
                        "title": "Cross-Gateway Real-Time Chat Delivery Flow",
                        "code": """flowchart LR
    UA["Sender A"] -->|WebSocket| GW1["Chat Gateway #1"]
    GW1 -->|Persist + Seq ID| MsgDB["Messages Store (partitioned by channel_id)"]
    GW1 -->|Lookup B location| Sess["Redis Session Map"]
    GW1 -->|Forward over MQ / RPC| GW2["Chat Gateway #89"]
    GW2 -->|WebSocket Push| UB["Receiver B (Online)"]
    GW1 -.->|If B Offline| Push["APNs / FCM Push Service"]"""
                    }
                ]
            },
            {
                "title": "Module 3: Presence Fan-Out Storms & Ordering Flaws",
                "blocks": [
                    {
                        "type": "diagram_critique",
                        "title": "The Presence 'Green Dot' Heartbeat Meltdown",
                        "scenario": "A chat platform sends every user's `10-second` online heartbeat to ALL 500 of their contacts immediately via fan-out push (`50M online * 500 friends / 10s = 2.5 Billion presence pushes/sec`)!",
                        "code": """flowchart LR
    U["50M Users"] -->|Every 10s heartbeat| Pres["Presence Service"]
    Pres -->|Push IMMEDIATELY to 500 friends each!| Friends["2.5 Billion Push Events/sec -> MELTDOWN!"]""",
                        "question": "How do WhatsApp / Discord scale Presence (`Online / Last Seen`) without melting push workers?",
                        "options": [
                            "Store lightweight TTL heartbeats in Redis (`last_active = now`, TTL=30s) and lazy-fetch / subscribe ONLY for currently visible conversation partners (not all 500 offline contacts!)",
                            "Increase heartbeat frequency from 10s to every 100ms",
                            "Persist every online ping forever inside PostgreSQL ACID rows",
                            "Broadcast presence packets over unencrypted DNS queries"
                        ],
                        "answer": "Store lightweight TTL heartbeats in Redis (`last_active = now`, TTL=30s) and lazy-fetch / subscribe ONLY for currently visible conversation partners (not all 500 offline contacts!)",
                        "remedy": "Only push status transitions (`Offline -> Online` after debounced `60s` grace window) AND strictly to **currently active open-screen / subscribed viewers** (plus lazy poll when opening a contact list!)."
                    },
                    {
                        "type": "scenario_decision",
                        "title": "Preventing Duplicate Bubbles on Flaky Subway Wi-Fi",
                        "scenario": "A commuter hits Send on `'Omw!'` just as the train enters a tunnel. Their app never receives the server ACK and retries sending the exact payload 3 times when exiting the tunnel.",
                        "question": "How do we guarantee the recipient sees `'Omw!'` ONCE in the exact right order?",
                        "options": [
                            "Attach a client-generated `client_msg_id` (UUID) for server-side idempotency deduplication AND return an authoritative server-assigned `message_id` / per-chat `seq_id`",
                            "Disable client retries permanently so lost packets disappear silently",
                            "Sort all messages alphabetically by body text before rendering",
                            "Trust the phone's local GPS clock to resolve order"
                        ],
                        "answer": "Attach a client-generated `client_msg_id` (UUID) for server-side idempotency deduplication AND return an authoritative server-assigned `message_id` / per-chat `seq_id`",
                        "rationale": "`client_msg_id` stored in a short-lived Redis dedup cache / unique index guarantees at-most-once storage even across retries, while server `message_id` breaks client clock-skew ties deterministically."
                    }
                ]
            },
            {
                "title": "Module 4: WebSocket Gateway Fleet Sizing & Partition Keys",
                "blocks": [
                    {
                        "type": "calculation_challenge",
                        "title": "Stateful WebSocket Connection Fleet Sizing",
                        "question": "A tuned Linux `epoll` WebSocket gateway server safely holds **100,000 concurrent persistent TLS WebSockets** (`~30 KB` kernel + app buffer = `~3 GB` RAM per box). To serve **50 million simultaneous online users** (with zero HA extra factor for this calculation), how many gateway servers are required?",
                        "answer": "500",
                        "alternatives": ["500", "500 servers"],
                        "step_by_step": "$50,000,000\\text{ concurrent connections} \\div 100,000\\text{ conn/server} = \\mathbf{500\\text{ servers}}$ (plus ~20% headroom + rolling-deploy capacity in production!). Notice each server only holds ~3 GB RAM, completely feasible on standard 16–32 GB cloud instances!"
                    },
                    {
                        "type": "fill_in_the_blank",
                        "title": "Chat History NoSQL Partition Key",
                        "question": "In Cassandra/ScyllaDB for fast `ORDER BY message_id DESC LIMIT 50` recent-history fetches without cross-node scatter-gather, the table's Partition Key should be _____ and Clustering Key `message_id DESC`.",
                        "answer": "channel_id",
                        "alternatives": ["channel_id", "conversation_id", "chat_id"],
                        "explanation": "Partitioning by `channel_id` (or `(channel_id, month_bucket)` for huge channels) co-locates a conversation's contiguous message slice on ONE node sorted chronologically!"
                    }
                ]
            }
        ]
    }
}
