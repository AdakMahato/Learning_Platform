# Master Catalog for Cloud Story Lab (Syllabus Aligned)
STORIES = [
    {
        "id": 0,
        "title": "Computing Evolution: From Mainframes to the Cloud",
        "icon": "🌐",
        "genre": "Evolutionary Paradigm",
        "difficulty": "Beginner",
        "hook": "Trace the architectural shift from centralized mainframes to Cluster computing, Grid computing, and utility XaaS offerings. Understand the business drivers, key market players, and cloud's transformative impact on global education.",
        "primary": "Evolution & Paradigms"
    },
    {
        "id": 1,
        "title": "Cloud Architecture, Service Models & Deployment",
        "icon": "🏛️",
        "genre": "Architectural Foundation",
        "difficulty": "Beginner",
        "hook": "Deconstruct the NIST cloud definition, the 5 essential characteristics, the Shared Responsibility Model, and deployment topographies: Public, Private, Hybrid, and Community clouds.",
        "primary": "Cloud Architecture & NIST"
    },
    {
        "id": 2,
        "title": "AWS Core Compute & Elasticity: EC2 Architecture",
        "icon": "⚡",
        "genre": "Infrastructure Lab",
        "difficulty": "Beginner",
        "hook": "Explore Amazon Web Services' flagship compute engine: EC2 instance families, AMI bundling, Elastic IP, pricing models (On-Demand, Reserved, Spot), and Security Group packet firewalls.",
        "primary": "AWS EC2 & Compute"
    },
    {
        "id": 3,
        "title": "Cloud Storage & Object Architecture: Amazon S3",
        "icon": "🪣",
        "genre": "Storage Architecture",
        "difficulty": "Intermediate",
        "hook": "Contrast Block, File, and Object storage paradigms. Dive into Amazon S3 bucket architecture, keys, metadata, storage tiers (Standard, Intelligent-Tiering, Glacier), and strong consistency models.",
        "primary": "Object Storage & S3"
    },
    {
        "id": 4,
        "title": "Cloud Messaging, Queues & Serverless Decoupling: SQS & SNS",
        "icon": "📬",
        "genre": "Distributed Systems",
        "difficulty": "Intermediate",
        "hook": "Decouple distributed microservices using asynchronous messaging. Master Amazon SQS (Standard vs FIFO queues, visibility timeout, dead-letter queues) and Amazon SNS fan-out pub/sub.",
        "primary": "Messaging & SQS/SNS"
    },
    {
        "id": 5,
        "title": "Cloud Identity, Access Management & Security Governance",
        "icon": "🔐",
        "genre": "Security Engineering",
        "difficulty": "Intermediate",
        "hook": "Lock down cloud environments using AWS IAM: Users, Groups, Roles, Policies, and the Principle of Least Privilege. Analyze multi-tenancy isolation risks and data sovereignty laws.",
        "primary": "IAM & Cloud Security"
    },
    {
        "id": 6,
        "title": "RESTful Web Services & Cloud API Design",
        "icon": "🌐",
        "genre": "API Engineering Lab",
        "difficulty": "Intermediate",
        "hook": "Architect scalable cloud microservice APIs conforming to Roy Fielding's REST constraints. Master HTTP verbs, URI resource naming, idempotent methods, status codes, and build a live REST endpoint.",
        "primary": "REST APIs & Web Services"
    },
    {
        "id": 7,
        "title": "Virtualization Foundations & Hypervisor Architecture",
        "icon": "💻",
        "genre": "Systems Engineering",
        "difficulty": "Intermediate",
        "hook": "Demystify the engine of the cloud: Type 1 Bare-Metal vs Type 2 Hosted Hypervisors. Compare Full Virtualization (binary translation), Para-virtualization, and Hardware-Assisted VT-x/AMD-V.",
        "primary": "Virtualization & Hypervisors"
    },
    {
        "id": 8,
        "title": "Virtualized Data Centers (VDC) & Process Migration",
        "icon": "🏢",
        "genre": "Data Center Engineering",
        "difficulty": "Intermediate",
        "hook": "Step inside a Virtualized Data Center: unify compute, storage, and network pools. Master VM Live Migration mechanics (Pre-copy vs Post-copy memory iteration) and VMware vCloud IaaS high availability.",
        "primary": "VDC & VM Migration"
    },
    {
        "id": 9,
        "title": "Software-Defined Networking (SDN) & Cloud Networking",
        "icon": "🔀",
        "genre": "Network Architecture",
        "difficulty": "Intermediate",
        "hook": "Decouple the Network Control Plane from the Data Plane. Explore OpenFlow switching, overlay encapsulation (VXLAN, NVGRE), Virtual Private Clouds (VPCs), subnets, and routing tables.",
        "primary": "SDN & Network Virtualization"
    },
    {
        "id": 10,
        "title": "Data Center Energy, Cooling & Green Cloud Sustainability",
        "icon": "🌿",
        "genre": "Green Computing",
        "difficulty": "Intermediate",
        "hook": "Calculate data center energy efficiency using Power Usage Effectiveness (PUE). Master eco-cooling technologies, renewable energy integration, server consolidation ratios, and Green Software Principles.",
        "primary": "Green Cloud & Sustainability"
    },
    {
        "id": 11,
        "title": "Big Data Distributed Storage: Hadoop & HDFS Architecture",
        "icon": "🐘",
        "genre": "Distributed Storage",
        "difficulty": "Advanced",
        "hook": "Store petabytes of unstructured data across commodity hardware. Explore Apache Hadoop, the HDFS master-worker architecture (NameNode, DataNodes), 128MB block sizing, and rack-aware replication.",
        "primary": "Hadoop & HDFS Storage"
    },
    {
        "id": 12,
        "title": "Distributed Data Processing: MapReduce & The Hadoop Ecosystem",
        "icon": "🔄",
        "genre": "Big Data Analytics Lab",
        "difficulty": "Advanced",
        "hook": "Process distributed datasets in parallel: Master the Map, Shuffle & Sort, and Reduce phases. Traverse the ecosystem (Apache Pig Latin, Apache Hive HiveQL, Apache Spark RDDs) and run a MapReduce job.",
        "primary": "MapReduce & Spark"
    },
    {
        "id": 13,
        "title": "NoSQL Database Architectures & Distributed Consistency",
        "icon": "🗄️",
        "genre": "Distributed Data Stores",
        "difficulty": "Advanced",
        "hook": "Break free from relational bottlenecks. Evaluate Eric Brewer's CAP Theorem, the PACELC extension, ACID vs BASE consistency, and master Key-Value, Document, Column-Family (Cassandra ring), and Graph NoSQL.",
        "primary": "NoSQL & Distributed Data"
    },
    {
        "id": 14,
        "title": "Edge Computing, Fog Computing & PaaS Ecosystems",
        "icon": "📡",
        "genre": "Edge & IoT Architecture",
        "difficulty": "Advanced",
        "hook": "Bridge the gap between IoT sensors and centralized clouds. Differentiate Edge and Fog computing, analyze Google AppEngine and Windows Azure PaaS platforms, and audit a Smart Healthcare remote ICU system.",
        "primary": "Edge, Fog & Healthcare IoT"
    },
    {
        "id": 15,
        "title": "Capstone Investigation: Cloud Scalability, FinOps & Failure Forensics",
        "icon": "🚨",
        "genre": "Forensics & Operations",
        "difficulty": "Advanced",
        "hook": "Master cloud operations under pressure: Elasticity vs Scalability, SLA availability nines downtime math, resource scheduling heuristics, Cloud Bursting, and investigate a multi-million-dollar FinOps billing outage.",
        "primary": "Scalability, FinOps & Forensics"
    }
]


def get_page_path(sid: int, title: str) -> str:
    safe = title.lower().replace(" ", "_").replace("'", "").replace("-", "_").replace(",", "").replace(":", "").replace("(", "").replace(")", "")
    return f"pages/{sid:02d}_{safe}.py"
