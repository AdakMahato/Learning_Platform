# Master Catalog for System Design Story Lab (HLD + LLD + Machine Coding)

STORIES = [
    {
        "id": 0,
        "title": "Back-of-the-Envelope Estimations & Latency Math",
        "icon": "🧮",
        "genre": "Capacity Engineering",
        "difficulty": "Beginner",
        "hook": "Size a 100M DAU launch in 90 seconds before a traffic spike melts your billing account. Master QPS, Peak multipliers, P99 tail latency, and storage bandwidth math.",
        "primary": "Estimations & SLOs",
        "topics": ["86,400s ~ 10^5 Shortcut", "Read/Write QPS", "Tail Latency P99", "Storage & Bandwidth"]
    },
    {
        "id": 1,
        "title": "Traffic Mesh: DNS, L4/L7 Load Balancers & CDNs",
        "icon": "🌐",
        "genre": "Edge Infrastructure",
        "difficulty": "Beginner → Intermediate",
        "hook": "Diagnose why a TLS handshake bottleneck and uncached 4K thumbnails saturated origin switches. Compare Anycast DNS, L4 vs L7 Load Balancers, and Push/Pull CDNs.",
        "primary": "Load Balancing & CDN",
        "topics": ["Anycast DNS & TTL", "L4 DSR vs L7 Reverse Proxy", "Health Checks", "Push vs Pull CDN"]
    },
    {
        "id": 2,
        "title": "Sub-Millisecond Memory: Distributed Caching & LRU Eviction",
        "icon": "⚡",
        "genre": "Performance Systems",
        "difficulty": "Intermediate",
        "hook": "Stop a Cache Stampede from crashing your primary RDS cluster at midnight. Master Cache-Aside, Write-Through/Write-Back, Singleflight, and build an O(1) LRU Cache.",
        "primary": "Caching & Eviction",
        "topics": ["Cache-Aside vs Write-Back", "Thundering Herd", "Cache Penetration", "LRU Cache Code Lab"]
    },
    {
        "id": 3,
        "title": "Scaling Stateful Data: Replication, Sharding & Hotspots",
        "icon": "🗄️",
        "genre": "Storage Architecture",
        "difficulty": "Intermediate",
        "hook": "Recover a checkout flow hit by read-your-own-writes stale lag and rebalance a skewed shard key. Contrast Sync/Async Replication, Read Replicas, and Federation.",
        "primary": "Database Scaling",
        "topics": ["Replication Lag", "Read-After-Write Consistency", "Range vs Hash Sharding", "Celebrity Key Salting"]
    },
    {
        "id": 4,
        "title": "Ring Topology: Consistent Hashing & Virtual Nodes",
        "icon": "💍",
        "genre": "Distributed Hash Tables",
        "difficulty": "Intermediate",
        "hook": "Adding one Redis server triggered a 92% cache miss storm using modulo hashing. Build a 32-bit Consistent Hash Ring with Virtual Nodes reducing remap to O(K/N).",
        "primary": "Consistent Hashing",
        "topics": ["hash(k) % N Storm", "Hash Ring Binary Search", "Virtual Nodes", "Hash Ring Code Lab"]
    },
    {
        "id": 5,
        "title": "Split-Brain Survivors: CAP, PACELC, Quorums & Raft",
        "icon": "⚖️",
        "genre": "Distributed Consensus",
        "difficulty": "Advanced",
        "hook": "A fiber cut partitioned Data Center B, causing two nodes to accept conflicting payments simultaneously. Prove Quorum R + W > N, PACELC trade-offs, and Raft Term Elections.",
        "primary": "Consensus & Consistency",
        "topics": ["CAP vs PACELC", "Quorum R + W > N", "Raft Leader Election", "Split-Brain Fencing"]
    },
    {
        "id": 6,
        "title": "API Shield: Gateways & Distributed Rate Limiters",
        "icon": "🛡️",
        "genre": "Edge Defense",
        "difficulty": "Intermediate",
        "hook": "Block a credential-stuffing botnet exploding at 00:00:59 without punishing legitimate burst traffic. Contrast Token Bucket, Leaky Bucket, Sliding Window, and Redis Lua atomicity.",
        "primary": "Rate Limiting & Gateways",
        "topics": ["Fixed Window Spike Bug", "Token vs Leaky Bucket", "Sliding Window Counter", "Token Bucket Code Lab"]
    },
    {
        "id": 7,
        "title": "Sequence Without Locks: Distributed Snowflake IDs",
        "icon": "❄️",
        "genre": "Distributed Identity",
        "difficulty": "Intermediate",
        "hook": "Why random UUIDv4 destroyed PostgreSQL B-Tree page locality at 80k inserts/sec. Engineer a 64-bit K-sortable Snowflake ID generator with NTP clock-drift guards.",
        "primary": "Unique ID Generation",
        "topics": ["UUIDv4 B-Tree Fragmentation", "DB Auto-Increment Bottleneck", "64-bit Snowflake Layout", "Snowflake Code Lab"]
    },
    {
        "id": 8,
        "title": "HLD Case Study I: Hyperscale URL Shortener (TinyURL)",
        "icon": "🔗",
        "genre": "High-Level Design",
        "difficulty": "Intermediate",
        "hook": "Architect a 100:1 read-heavy shortening service handling 10k redirects/sec with 10-year retention. Contrast Base62 Counter vs KGS Pre-Gen keys and 301 vs 302 analytics.",
        "primary": "URL Shortener HLD",
        "topics": ["Base62 Encoding", "301 vs 302 Redirects", "KGS Range Allocation", "Base62 Codec Code Lab"]
    },
    {
        "id": 9,
        "title": "HLD Case Study II: Real-Time Chat (WhatsApp & Slack)",
        "icon": "💬",
        "genre": "Real-Time Messaging",
        "difficulty": "Advanced",
        "hook": "Deliver 1-to-1 and group messages sub-100ms across flaky mobile networks without duplicate/out-of-order bubbles. Master Stateful WebSocket Gateways and Presence Heartbeats.",
        "primary": "Chat Systems HLD",
        "topics": ["WebSocket vs SSE/Poll", "Service Discovery", "Offline Sync Queue", "Sequence ID Ordering"]
    },
    {
        "id": 10,
        "title": "HLD Case Study III: Social News Feed & Push Notifications",
        "icon": "📣",
        "genre": "Social Graph Scaling",
        "difficulty": "Advanced",
        "hook": "Why pushing one celebrity tweet to 80 million followers stalled normal user timelines for 15 minutes. Design a Hybrid Push/Pull Fan-Out pipeline and Notification Worker Mesh.",
        "primary": "News Feed Fan-Out",
        "topics": ["Fan-Out on Write vs Read", "Celebrity Hybrid Split", "Feed Hydration Cache", "Dead-Letter Priority"]
    },
    {
        "id": 11,
        "title": "HLD Case Study IV: Search Typeahead, Video & Cloud Drive",
        "icon": "☁️",
        "genre": "Media & Storage HLD",
        "difficulty": "Advanced",
        "hook": "Design a Google Drive chunk-sync delta uploader, an HLS Adaptive Bitrate video transcoder, and a distributed Top-K Trie autocomplete index.",
        "primary": "Cloud Drive, Video & Search",
        "topics": ["Chunked Delta Sync", "HLS DAG Transcoding", "Trie Precomputed Top-K", "Object Storage S3"]
    },
    {
        "id": 12,
        "title": "LLD Foundations: SOLID Principles, Patterns & Concurrency",
        "icon": "🧱",
        "genre": "Low-Level Design",
        "difficulty": "Intermediate",
        "hook": "Refactor a brittle payment processor riddled with 15-branch switch chains into clean Strategy, Factory, Observer, and Lock-Safe Concurrent primitives.",
        "primary": "SOLID & Design Patterns",
        "topics": ["SOLID Violations", "Strategy vs Factory", "Observer Event Bus", "CAS vs Pessimistic Lock"]
    },
    {
        "id": 13,
        "title": "LLD Machine Coding: Parking Lot, BookMyShow, Splitwise & Elevator",
        "icon": "🅿️",
        "genre": "Machine Coding Lab",
        "difficulty": "Intermediate → Advanced",
        "hook": "Ace live LLD interviews! Architect clean state transitions, prevent double-booked cinema seats with TTL holds, simplify group debt graphs, and code a Parking Lot engine.",
        "primary": "LLD Machine Coding",
        "topics": ["Multi-Floor Spot Allocation", "Distributed Seat Lock TTL", "Min-Cash-Flow Debt Split", "Parking Lot Code Lab"]
    }
]
