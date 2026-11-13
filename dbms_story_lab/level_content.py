LEVEL_CONTENT = {
  "1": {
    "format": "episodic",
    "episodes": [
      {
        "title": "Module 1: The Chaos of Nexora",
        "blocks": [
          {
            "type": "story",
            "title": "Nexora's Fragmented Mind",
            "text": "Nexora controls hospitals, trains, and banks. Every department keeps its own records in isolation. Train schedules don't know bank holidays, and hospitals don't know train delays. The city is grinding to a halt."
          },
          {
            "type": "problem",
            "text": "You must build the database that connects all of Nexora's systems into a single, unified source of truth."
          },
          {
            "type": "concept",
            "title": "What is a Relational Database?",
            "explanation": "A relational database organizes data into tables (relations) which can be linked\u2014or related\u2014based on data common to each.",
            "analogy": "Think of it as a meticulously organized filing cabinet where every folder has a cross-reference tag to other relevant folders, instead of just tossing papers into a box.",
            "technical_explanation": "Relational databases use the Relational Model introduced by E.F. Codd in 1970, which abstracts data into tuples (rows) and attributes (columns).",
            "why_it_matters": "Without it, Nexora suffers from data redundancy and inconsistency.",
            "remember": "Tables are for entities; relationships connect them."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "+-----------+       +-----------+\n| Hospital  |       | Train     |\n+-----------+       +-----------+\n| PatientID |<------| Passenger |\n+-----------+       +-----------+"
          }
        ]
      },
      {
        "title": "Module 2: Creating the Foundation",
        "blocks": [
          {
            "type": "concept",
            "title": "Tables and Data Types",
            "explanation": "To store data, you must define its structure using Data Definition Language (DDL).",
            "analogy": "Like pouring concrete for a building's foundation, you must specify the exact dimensions before building.",
            "technical_explanation": "CREATE TABLE defines the schema. Data types (INT, VARCHAR) enforce domain constraints.",
            "why_it_matters": "Prevents invalid data (like text in a number field) from entering the system.",
            "remember": "Schema first, data later."
          },
          {
            "type": "worked_example",
            "title": "Defining a Hospital Record",
            "steps": [
              "Identify attributes: name, age, blood_type.",
              "Choose types: VARCHAR, INT, VARCHAR.",
              "Write the CREATE TABLE statement."
            ]
          },
          {
            "type": "sql_sandbox",
            "title": "Build the Patient Table",
            "context": "Nexora's Central Hospital needs a table to store patient demographics.",
            "init_script": "",
            "solution_query": "CREATE TABLE patients (id INT, name VARCHAR(100), age INT);",
            "hint": "Use CREATE TABLE patients (...) with id, name, and age.",
            "explanation": "This establishes the structure for all future patient records."
          }
        ]
      },
      {
        "title": "Module 3: Entering Data",
        "blocks": [
          {
            "type": "concept",
            "title": "Inserting Records",
            "explanation": "Once a table exists, Data Manipulation Language (DML) is used to populate it.",
            "analogy": "The foundation is laid; now you are moving the furniture in.",
            "technical_explanation": "The INSERT statement adds new tuples to a relation.",
            "why_it_matters": "A database without data is just an empty shell.",
            "remember": "Match the column order in your INSERT statement."
          },
          {
            "type": "micro_challenge",
            "question": "What happens if you omit a column during INSERT without providing a DEFAULT?",
            "options": [
              "It crashes",
              "It inserts NULL",
              "It inserts 0"
            ],
            "answer": "It inserts NULL",
            "explanation": "Unless constrained otherwise, missing values default to NULL."
          },
          {
            "type": "sql_sandbox",
            "title": "Registering the First Patient",
            "context": "Patient 'Ada' is 25 years old. Add her to the system.",
            "init_script": "CREATE TABLE patients (id INT, name VARCHAR(100), age INT);",
            "solution_query": "INSERT INTO patients (id, name, age) VALUES (1, 'Ada', 25);",
            "hint": "Use INSERT INTO ... VALUES ...",
            "explanation": "You've successfully added a tuple to the relation."
          }
        ]
      },
      {
        "title": "Module 4: Retrieving the Truth",
        "blocks": [
          {
            "type": "concept",
            "title": "The SELECT Statement",
            "explanation": "Data retrieval is done via queries.",
            "analogy": "Like a search engine for your structured data.",
            "technical_explanation": "SELECT defines the projection (columns), FROM specifies the relation, and WHERE applies a selection filter (rows).",
            "why_it_matters": "Querying is the primary way applications interact with databases.",
            "remember": "SELECT filters columns, WHERE filters rows."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "SELECT name -- PROJECTION\nFROM patients -- RELATION\nWHERE age > 20 -- SELECTION"
          },
          {
            "type": "sql_sandbox",
            "title": "Find Adult Patients",
            "context": "The hospital needs a list of all patients over 18.",
            "init_script": "CREATE TABLE patients (id INT, name VARCHAR(100), age INT); INSERT INTO patients VALUES (1, 'Ada', 25), (2, 'Bob', 12);",
            "solution_query": "SELECT name FROM patients WHERE age > 18;",
            "hint": "Use WHERE age > 18",
            "explanation": "The database engine filters the rows before returning the result."
          }
        ]
      },
      {
        "title": "Module 5: Ensuring Identity",
        "blocks": [
          {
            "type": "concept",
            "title": "Primary Keys",
            "explanation": "A primary key uniquely identifies each record.",
            "analogy": "Like a fingerprint or a passport number, no two rows can have the same primary key.",
            "technical_explanation": "A PRIMARY KEY constraint automatically implies UNIQUE and NOT NULL.",
            "why_it_matters": "Without it, you cannot reliably update or delete specific records.",
            "remember": "Every table should have a primary key."
          },
          {
            "type": "debugger",
            "title": "Duplicate Identity Crisis",
            "scenario": "You tried to insert two patients with ID=1, and the system threw an error.",
            "options": [
              "The system is out of memory",
              "Primary Key violation",
              "Syntax error"
            ],
            "answer": "Primary Key violation",
            "explanation": "The PRIMARY KEY constraint enforces entity integrity."
          },
          {
            "type": "sql_sandbox",
            "title": "Enforce Identity",
            "context": "Recreate the patients table, but this time make `id` the primary key.",
            "init_script": "",
            "solution_query": "CREATE TABLE patients (id INT PRIMARY KEY, name VARCHAR(100), age INT);",
            "hint": "Add PRIMARY KEY next to the id definition.",
            "explanation": "Now Nexora can never mix up two patients with the same name."
          }
        ]
      },
      {
        "title": "Module 6: Connecting the Dots",
        "blocks": [
          {
            "type": "concept",
            "title": "Foreign Keys and JOINs",
            "explanation": "Foreign keys link tables together, and JOINs retrieve data across these links.",
            "analogy": "Like a bridge between two islands, a foreign key allows you to travel from one entity to another.",
            "technical_explanation": "A FOREIGN KEY references the PRIMARY KEY of another table, enforcing referential integrity. An INNER JOIN computes the Cartesian product and filters by the join condition.",
            "why_it_matters": "This is what makes a relational database 'relational'.",
            "remember": "Foreign keys enforce links; JOINs traverse them."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "[Patients: id] <---- (Foreign Key) ---- [Visits: patient_id]"
          },
          {
            "type": "sql_sandbox",
            "title": "Cross-Department Insight",
            "context": "Join patients with their hospital visits.",
            "init_script": "CREATE TABLE patients (id INT PRIMARY KEY, name VARCHAR); CREATE TABLE visits (id INT, patient_id INT); INSERT INTO patients VALUES (1, 'Ada'); INSERT INTO visits VALUES (101, 1);",
            "solution_query": "SELECT patients.name, visits.id FROM patients JOIN visits ON patients.id = visits.patient_id;",
            "hint": "JOIN visits ON patients.id = visits.patient_id",
            "explanation": "You've successfully unified data across Nexora's departments."
          }
        ]
      },
      {
        "title": "Module 7: The Train, The Bank, The Hospital",
        "blocks": [
          {
            "type": "concept",
            "title": "Transactions and ACID",
            "explanation": "Transactions ensure that complex operations succeed or fail as a single unit.",
            "analogy": "Buying a train ticket: money leaves your bank, AND a seat is reserved. If one fails, both must fail.",
            "technical_explanation": "ACID properties: Atomicity, Consistency, Isolation, Durability. BEGIN TRANSACTION and COMMIT/ROLLBACK control this.",
            "why_it_matters": "Prevents catastrophic partial failures in critical systems like banking.",
            "remember": "All or nothing."
          },
          {
            "type": "reflection",
            "question": "What would happen in Nexora if a bank transfer was not Atomic?"
          },
          {
            "type": "debugger",
            "title": "The Ghost Ticket",
            "scenario": "A passenger's bank account was deducted, but no ticket was issued. What property failed?",
            "options": [
              "Atomicity",
              "Isolation",
              "Durability"
            ],
            "answer": "Atomicity",
            "explanation": "Atomicity guarantees that all parts of the transaction complete, or none do."
          }
        ]
      },
      {
        "title": "Module 8: Final Investigation",
        "blocks": [
          {
            "type": "concept",
            "title": "Indexes and Performance",
            "explanation": "Indexes speed up data retrieval at the cost of slower inserts.",
            "analogy": "Like an index at the back of a textbook, it saves you from reading every page.",
            "technical_explanation": "An index creates a B-Tree or Hash data structure for logarithmic time lookups instead of linear table scans.",
            "why_it_matters": "Nexora's database is growing; without indexes, queries will time out.",
            "remember": "Index the columns you search by, not every column."
          },
          {
            "type": "sql_sandbox",
            "title": "Nexora Grand Unification",
            "context": "Nexora is fixed. For a final test, create an index on the patient's name to optimize search.",
            "init_script": "CREATE TABLE patients (id INT PRIMARY KEY, name VARCHAR(100));",
            "solution_query": "CREATE INDEX idx_name ON patients(name);",
            "hint": "CREATE INDEX index_name ON table(column);",
            "explanation": "Your database is now structurally sound and performant. Nexora thrives."
          }
        ]
      }
    ]
  },
  "11": {
    "format": "episodic",
    "episodes": [
      {
        "title": "Module 1: The City That Forgets",
        "blocks": [
          {
            "type": "story",
            "title": "A Missing Hour",
            "text": "Every night, between 2:00 AM and 3:00 AM, the central registry of Neo-Veridia wipes itself. A specific hour of data simply vanishes."
          },
          {
            "type": "problem",
            "text": "How do we ensure that a database can recover from a crash without losing data, while remaining fast enough to process massive daily transactions?"
          },
          {
            "type": "concept",
            "title": "ACID and Durability",
            "explanation": "Databases must guarantee that once a transaction is committed, it remains saved even in the event of a power loss. This is the 'D' in ACID: Durability.",
            "analogy": "Taking notes in pen rather than pencil. If someone rubs a giant eraser over the notebook (a crash), the pen marks remain.",
            "technical_explanation": "Modern databases use a Write-Ahead Log (WAL). Before modifying the actual data files on disk (which is slow), they append a quick note to the WAL (which is fast).",
            "why_it_matters": "Without durability guarantees, system crashes lead to silent data corruption or permanent data loss.",
            "remember": "Durability means committed data is never lost."
          }
        ]
      },
      {
        "title": "Module 2: Normalization and Redundancy",
        "blocks": [
          {
            "type": "story",
            "title": "Bloated Records",
            "text": "Before fixing the crashes, you realize the database is writing too much data. Every citizen's record contains the full text of their neighborhood's charter, causing huge write delays."
          },
          {
            "type": "concept",
            "title": "Database Normalization",
            "explanation": "Normalization is the process of organizing data to minimize redundancy. Instead of storing the neighborhood charter in every citizen's row, we store it once and reference it.",
            "analogy": "Instead of writing your full home address on every page of a form, you write it once on the cover page and just put your name on the subsequent pages.",
            "technical_explanation": "By breaking large tables into smaller, related tables (1NF, 2NF, 3NF), we reduce storage space and eliminate update anomalies. This means writes are smaller and faster.",
            "why_it_matters": "Faster writes mean shorter transactions, reducing the window of vulnerability before data hits the disk.",
            "remember": "Normalize to reduce redundancy and speed up writes."
          },
          {
            "type": "worked_example",
            "title": "Refactoring to 3NF",
            "steps": [
              "1. Initial: Table Citizens (ID, Name, NeighborhoodName, NeighborhoodCharterText)",
              "2. Normalization: Create Table Neighborhoods (ID, Name, CharterText)",
              "3. Update: Table Citizens now becomes (ID, Name, NeighborhoodID)",
              "4. Result: The massive text is only stored once."
            ]
          }
        ]
      },
      {
        "title": "Module 3: Indexing for Speed",
        "blocks": [
          {
            "type": "concept",
            "title": "The Power of Indexes",
            "explanation": "As the city grows, finding a citizen by name takes forever. An index acts like a book's glossary, allowing the database to jump directly to the right row.",
            "analogy": "Finding a recipe in a cookbook by flipping through every page vs. looking at the index at the back.",
            "technical_explanation": "Indexes are typically implemented as B-Trees. They provide O(log N) lookup times instead of O(N) full table scans.",
            "why_it_matters": "Indexes drastically speed up read queries, but they slow down write queries because the index must be updated every time data changes.",
            "remember": "Indexes trade write performance for read performance."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "Table Data: [Row 1] [Row 2] [Row 3] ... [Row 1,000,000]\nIndex on Name: 'Alice' -> Row 842, 'Bob' -> Row 12"
          },
          {
            "type": "micro_challenge",
            "question": "If you have a table that is read from rarely but inserted into millions of times per second, should you add many indexes to it?",
            "options": [
              "Yes, always index everything.",
              "No, indexes will slow down the heavy insert workload.",
              "Yes, but only if they are hash indexes."
            ],
            "answer": "No, indexes will slow down the heavy insert workload.",
            "explanation": "Every index requires updating during an insert. Heavy insert workloads should minimize indexes to maximize throughput."
          }
        ]
      },
      {
        "title": "Module 4: Transactions and Recovery",
        "blocks": [
          {
            "type": "concept",
            "title": "The Write-Ahead Log (WAL)",
            "explanation": "To solve the 2:00 AM data wipe, we implement a WAL.",
            "analogy": "A black box flight recorder. Everything you intend to do is spoken into the recorder before you do it.",
            "technical_explanation": "When a transaction commits, the DB writes the changes to the WAL file on disk sequentially (which is very fast). The actual database tables are updated in memory and flushed to disk later asynchronously. If the power fails, upon reboot, the DB reads the WAL and replays the missing changes.",
            "why_it_matters": "WAL provides Durability without sacrificing performance, combining fast sequential disk I/O with safe recovery.",
            "remember": "Write to the log first, update the tables later."
          },
          {
            "type": "debugger",
            "title": "Analyzing a Crash",
            "scenario": "A crash occurs. Transaction A was written to the WAL and committed. Transaction B was in memory but not yet committed. What happens on reboot?",
            "options": [
              "Both A and B are recovered.",
              "A is recovered; B is rolled back and lost.",
              "Neither is recovered."
            ],
            "answer": "A is recovered; B is rolled back and lost.",
            "explanation": "Since A committed, its WAL entry is complete and can be replayed. B was uncommitted, so the database discards it to maintain consistency."
          }
        ]
      },
      {
        "title": "Module 5: Partitioning Massive Data",
        "blocks": [
          {
            "type": "story",
            "title": "The Infinite Archive",
            "text": "The city's historical records have grown to terabytes. Even with indexes, backups and maintenance are taking too long."
          },
          {
            "type": "concept",
            "title": "Database Partitioning",
            "explanation": "Partitioning divides a large table into smaller, more manageable physical pieces while treating them as one logical table.",
            "analogy": "Instead of keeping all years of tax returns in one giant filing cabinet, you put 2020 in one drawer, 2021 in another, and 2022 in a third.",
            "technical_explanation": "Common strategies include Range Partitioning (e.g., by date) or Hash Partitioning. Queries that filter by the partition key can skip irrelevant partitions entirely (Partition Pruning).",
            "why_it_matters": "Partitioning improves manageability (you can easily drop old data) and can speed up queries that target specific ranges.",
            "remember": "Divide and conquer your data."
          }
        ]
      },
      {
        "title": "Module 6: SQL Sandbox - Normalization",
        "blocks": [
          {
            "type": "sql_sandbox",
            "title": "Fix the Bloated Table",
            "context": "Extract the neighborhood data from the citizens table.",
            "init_script": "CREATE TABLE raw_citizens (id INT, name TEXT, hood_name TEXT, hood_charter TEXT); INSERT INTO raw_citizens VALUES (1, 'Eve', 'Downtown', 'Be quiet'), (2, 'Adam', 'Downtown', 'Be quiet'); CREATE TABLE neighborhoods (id INT PRIMARY KEY, hood_name TEXT, hood_charter TEXT); CREATE TABLE citizens (id INT, name TEXT, hood_id INT);",
            "solution_query": "INSERT INTO neighborhoods (id, hood_name, hood_charter) VALUES (1, 'Downtown', 'Be quiet'); INSERT INTO citizens (id, name, hood_id) VALUES (1, 'Eve', 1), (2, 'Adam', 1);",
            "hint": "Manually insert the single neighborhood, then insert the citizens referencing that neighborhood's ID.",
            "explanation": "By manually moving the data, we achieved 3NF. The repetitive charter text is stored once."
          }
        ]
      },
      {
        "title": "Module 7: SQL Sandbox - Index Creation",
        "blocks": [
          {
            "type": "sql_sandbox",
            "title": "Speed Up the Lookup",
            "context": "The security team frequently searches for citizens by name. Add an index to make this fast.",
            "init_script": "CREATE TABLE citizens (id INT, name TEXT);",
            "solution_query": "CREATE INDEX idx_citizen_name ON citizens(name);",
            "hint": "Use CREATE INDEX index_name ON table_name(column_name);",
            "explanation": "The B-Tree index will now allow the database engine to find names in logarithmic time."
          }
        ]
      },
      {
        "title": "Module 8: Final Challenge - Transactions and Recovery",
        "blocks": [
          {
            "type": "story",
            "title": "The Night Shift Check",
            "text": "The memory wiping anomaly is fixed via WAL. Now you must perform a transactional update to ensure it works."
          },
          {
            "type": "sql_sandbox",
            "title": "Secure the Transfer",
            "context": "Transfer 100 credits from Account A to Account B safely.",
            "init_script": "CREATE TABLE accounts (name TEXT, balance INT); INSERT INTO accounts VALUES ('A', 500), ('B', 500);",
            "solution_query": "BEGIN TRANSACTION; UPDATE accounts SET balance = balance - 100 WHERE name = 'A'; UPDATE accounts SET balance = balance + 100 WHERE name = 'B'; COMMIT;",
            "hint": "Use BEGIN TRANSACTION and COMMIT around your updates.",
            "explanation": "By wrapping the updates in a transaction, the WAL guarantees both operations will succeed together, or fail together, preventing money creation or destruction."
          }
        ]
      }
    ]
  },
  "9": {
    "format": "episodic",
    "episodes": [
      {
        "title": "Module 1: The Three Colonies",
        "blocks": [
          {
            "type": "story",
            "title": "The Cargo Dispute",
            "text": "Mars, Luna, and Titan colonies share a unified inventory database. A transport ship has exactly 100 Fusion Cores. Mars claims 100. Titan claims 100. Because space communication is heavily delayed and occasionally fails, both colonies saw '100 Available' and both approved the claim. Now they are at war."
          },
          {
            "type": "problem",
            "text": "How do you maintain a single unified truth across databases separated by vast physical distances and unreliable networks?"
          },
          {
            "type": "concept",
            "title": "Distributed Databases",
            "explanation": "A distributed database stores data across multiple physical locations.",
            "analogy": "A team of accountants in different cities trying to balance the exact same ledger via mail.",
            "technical_explanation": "Nodes (servers) must communicate to ensure data remains consistent. If Node A updates a record, it must replicate that change to Node B.",
            "why_it_matters": "Single servers are a single point of failure and have scale limits. Distribution provides high availability and scale, but introduces immense complexity.",
            "remember": "The network is never reliable."
          }
        ]
      },
      {
        "title": "Module 2: Replication Strategies",
        "blocks": [
          {
            "type": "concept",
            "title": "Primary-Replica vs. Multi-Primary",
            "explanation": "How do we decide who gets to write data?",
            "analogy": "A classroom where only the teacher can write on the board (Primary) vs. a shared Google Doc where anyone can type (Multi-Primary).",
            "technical_explanation": "Primary-Replica (Master-Slave): All writes go to one node, which streams changes to read-only replicas. Multi-Primary: Any node can accept writes, requiring complex conflict resolution.",
            "why_it_matters": "Primary-Replica is easy but the Primary is a bottleneck. Multi-Primary scales writes but leads to the exact conflict the Mars/Titan colonies experienced.",
            "remember": "Multiple writers mean inevitable conflicts."
          }
        ]
      },
      {
        "title": "Module 3: The CAP Theorem",
        "blocks": [
          {
            "type": "concept",
            "title": "Consistency, Availability, Partition Tolerance",
            "explanation": "In 2000, Eric Brewer proved you can't have it all in a distributed system.",
            "analogy": "You can have it Fast, Cheap, or Good. Pick two.",
            "technical_explanation": "CAP Theorem states a distributed system can provide only two of three: Consistency (every read receives the most recent write), Availability (every request receives a response), and Partition Tolerance (the system operates despite network failures).",
            "why_it_matters": "Because network partitions (P) are a physical reality you cannot avoid, you must choose between C and A when a network failure occurs.",
            "remember": "During a network split, you must choose: Stop responding (Consistency) or respond with stale data (Availability)."
          }
        ]
      },
      {
        "title": "Module 4: Applying CAP to the Colonies",
        "blocks": [
          {
            "type": "visual",
            "visual_type": "text",
            "data": "Network Cut between Mars & Titan\n\nTitan Node: 'Client wants 100 Cores'\n\nChoice 1 (CP - Consistency): Titan says 'I can't reach Mars to verify, so I must reject the request.'\nChoice 2 (AP - Availability): Titan says 'I have no connection, but my local data says 100, so I approve it.'"
          },
          {
            "type": "debugger",
            "title": "CAP Tradeoffs",
            "scenario": "A medical database tracking lethal drug interactions cannot ever return incorrect/stale data, even if offline. What does it prioritize?",
            "options": [
              "AP (Availability & Partition Tolerance)",
              "CP (Consistency & Partition Tolerance)",
              "CA (Consistency & Availability)"
            ],
            "answer": "CP (Consistency & Partition Tolerance)",
            "explanation": "It must prioritize Consistency. If the network drops (Partition), it will refuse to answer (sacrificing Availability) rather than risk giving deadly wrong information."
          }
        ]
      },
      {
        "title": "Module 5: Eventual Consistency",
        "blocks": [
          {
            "type": "concept",
            "title": "Embracing AP",
            "explanation": "Many modern systems choose AP. They accept that data might be out of sync briefly, but will 'eventually' become consistent once the network heals.",
            "analogy": "Social media likes. If you like a post, your friend might not see the like for a few seconds. Nobody dies.",
            "technical_explanation": "Nodes accept writes locally and broadcast them asynchronously. Systems like DynamoDB or Cassandra often use tunable consistency models.",
            "why_it_matters": "Provides maximum uptime and lowest latency, critical for massive consumer apps.",
            "remember": "Eventual consistency means it's wrong right now, but will be right later."
          }
        ]
      },
      {
        "title": "Module 6: Distributed Consensus",
        "blocks": [
          {
            "type": "concept",
            "title": "Paxos and Raft",
            "explanation": "If we choose CP (Consistency), how do nodes agree on the truth?",
            "analogy": "A jury voting on a verdict. They must follow strict rules to ensure a majority agrees before deciding.",
            "technical_explanation": "Consensus algorithms like Raft require a majority (quorum) of nodes to acknowledge a write before it is committed. If there are 5 nodes, 3 must agree.",
            "why_it_matters": "This solves the Mars/Titan problem. If the network splits, only the side with the majority can process writes. The minority partition pauses, preventing split-brain.",
            "remember": "Consensus requires a majority vote."
          }
        ]
      },
      {
        "title": "Module 7: Data Partitioning (Sharding)",
        "blocks": [
          {
            "type": "concept",
            "title": "Splitting the Data",
            "explanation": "When data is too large for one server, we split it. This is Partitioning or Sharding.",
            "analogy": "Organizing a library by putting A-M on the first floor and N-Z on the second floor.",
            "technical_explanation": "A Shard Key determines which node holds the data. If sharded by 'colony_id', Mars data lives on Mars servers.",
            "why_it_matters": "Allows infinite horizontal scaling. But cross-shard queries (e.g., 'Total inventory across all colonies') become very expensive.",
            "remember": "Pick your shard key carefully, or one node will do all the work (a hot partition)."
          }
        ]
      },
      {
        "title": "Module 8: Securing the Cargo",
        "blocks": [
          {
            "type": "story",
            "title": "Implementing Two-Phase Commit",
            "text": "To prevent the cargo dispute from ever happening again, you implement a protocol where ALL colonies must agree before inventory is deducted."
          },
          {
            "type": "problem",
            "text": "Simulate the preparation phase of a distributed transaction."
          },
          {
            "type": "sql_sandbox",
            "title": "State Tracking for 2PC",
            "context": "In a Two-Phase Commit (2PC), a transaction is first 'PREPARED'. Update the transaction state.",
            "init_script": "CREATE TABLE distributed_tx (tx_id INT, state TEXT); INSERT INTO distributed_tx VALUES (99, 'PENDING');",
            "solution_query": "UPDATE distributed_tx SET state = 'PREPARED' WHERE tx_id = 99;",
            "hint": "Update the state string to PREPARED.",
            "explanation": "In 2PC, the coordinator asks all nodes to 'PREPARE'. Only if all nodes reply YES, does it then broadcast 'COMMIT'."
          }
        ]
      }
    ]
  },
  "8": {
    "format": "episodic",
    "episodes": [
      {
        "title": "Module 1: The Ocean of Signals",
        "blocks": [
          {
            "type": "story",
            "title": "Half a Billion Bursts",
            "text": "Deep space sensors have recorded 500,000,000 electromagnetic radio bursts. Our analysts suspect one specific frequency pattern repeats exactly every 72 hours, but every time they run a query to find it, the database grinds to a halt and crashes."
          },
          {
            "type": "problem",
            "text": "How do you search through half a billion records without checking every single one?"
          },
          {
            "type": "concept",
            "title": "The Sequential Scan",
            "explanation": "Without any special structures, finding a specific record means looking at the first one, then the second, then the third, until the end.",
            "analogy": "Looking for a specific word in a dictionary by reading from page 1, line 1, until you find it.",
            "technical_explanation": "A Sequential Scan (or Full Table Scan) reads every block of the table from disk into memory and checks if it matches the WHERE clause.",
            "why_it_matters": "O(N) time complexity. It scales terribly. As data grows, queries become impossibly slow.",
            "remember": "Sequential scan is the enemy of large datasets."
          }
        ]
      },
      {
        "title": "Module 2: Introducing Indexing",
        "blocks": [
          {
            "type": "concept",
            "title": "Database Indexes",
            "explanation": "An index is a separate data structure that keeps a sorted copy of a specific column, along with pointers to the original row.",
            "analogy": "The index at the back of a textbook. It's sorted alphabetically, telling you exactly which page contains the topic.",
            "technical_explanation": "By creating an index on a column, the database can use fast lookup algorithms (like binary search) instead of a full sequential scan.",
            "why_it_matters": "Reduces lookup time from O(N) to O(log N).",
            "remember": "Indexes trade write speed and storage space for massive read speed improvements."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "Table: [ID: 1, Freq: 800], [ID: 2, Freq: 100], [ID: 3, Freq: 500]\n\nIndex on Freq:\n[Freq: 100 -> Pointer to Row 2]\n[Freq: 500 -> Pointer to Row 3]\n[Freq: 800 -> Pointer to Row 1]"
          }
        ]
      },
      {
        "title": "Module 3: B-Trees (Balanced Trees)",
        "blocks": [
          {
            "type": "concept",
            "title": "The Anatomy of a B-Tree",
            "explanation": "Most database indexes use a B-Tree (Balanced Tree) structure. It's a hierarchical tree designed to minimize disk reads.",
            "analogy": "A filing cabinet system where the top drawer tells you which floor to go to, the floor tells you which room, and the room has the exact file.",
            "technical_explanation": "A B-Tree keeps data sorted and allows searches, sequential access, insertions, and deletions in logarithmic time. The 'Balanced' part means all paths from root to leaf have the same length.",
            "why_it_matters": "Disk I/O is slow. B-Trees are wide and shallow, meaning you only need to read 3 or 4 disk blocks to find one record out of billions.",
            "remember": "B-Trees minimize disk hops."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "          [ 500 ]\n         /       \\\n  [ 100, 300 ]   [ 700, 900 ]\n   /    |    \\      |    \\\nLeaf  Leaf  Leaf  Leaf  Leaf"
          }
        ]
      },
      {
        "title": "Module 4: Index Scans vs. Seeks",
        "blocks": [
          {
            "type": "concept",
            "title": "How Indexes Are Used",
            "explanation": "Having an index doesn't guarantee it will be used efficiently.",
            "analogy": "Having a dictionary is useless if you're looking for 'words that end in -ing'. You still have to read the whole book.",
            "technical_explanation": "Index Seek: Traversing the B-Tree directly to the exact value (O(log N)). Index Scan: Reading across the bottom leaf nodes of the index (faster than full table scan, but still O(N) over the index).",
            "why_it_matters": "Queries with functions (e.g., `WHERE YEAR(date) = 2023`) or leading wildcards (e.g., `LIKE '%pattern'`) prevent the database from doing an Index Seek.",
            "remember": "Don't hide indexed columns inside functions in your WHERE clause."
          },
          {
            "type": "debugger",
            "title": "Sargability",
            "scenario": "You have an index on `frequency_hz`. Which query will use an Index Seek?",
            "options": [
              "SELECT * FROM signals WHERE frequency_hz * 2 = 1000",
              "SELECT * FROM signals WHERE frequency_hz = 500",
              "SELECT * FROM signals WHERE CAST(frequency_hz AS TEXT) LIKE '5%'"
            ],
            "answer": "SELECT * FROM signals WHERE frequency_hz = 500",
            "explanation": "The first and third options wrap the column in operations, preventing the database from searching the B-Tree directly."
          }
        ]
      },
      {
        "title": "Module 5: The Cost of Indexing",
        "blocks": [
          {
            "type": "concept",
            "title": "Trade-offs of Indexes",
            "explanation": "If indexes make reads fast, why not index every single column?",
            "analogy": "If you add every single word of a book to the index at the back, the index becomes larger than the book itself.",
            "technical_explanation": "Every time you INSERT, UPDATE, or DELETE a row, the database must also update all corresponding B-Trees. This adds significant write latency and consumes disk space.",
            "why_it_matters": "Over-indexing kills database write performance.",
            "remember": "Indexes are not free."
          }
        ]
      },
      {
        "title": "Module 6: Composite Indexes",
        "blocks": [
          {
            "type": "concept",
            "title": "Multi-Column Indexes",
            "explanation": "Sometimes queries filter on multiple columns at once.",
            "analogy": "A phone book is a composite index: (Last Name, First Name). You can easily find 'Smith, John', or all 'Smiths', but you cannot use it to find all people named 'John'.",
            "technical_explanation": "A composite index sorts by Column A, then by Column B. The order matters! It can only be used if the query filters on a prefix of the indexed columns (e.g., A, or A and B, but NOT just B).",
            "why_it_matters": "Designing composite indexes requires understanding query patterns to get the order right.",
            "remember": "Left-to-right rule for composite indexes."
          }
        ]
      },
      {
        "title": "Module 7: Materialized Views and OLAP",
        "blocks": [
          {
            "type": "concept",
            "title": "Pre-computing Results",
            "explanation": "If millions of users run the exact same heavy analytical query (OLAP), even indexes might not be fast enough.",
            "analogy": "Instead of cooking a fresh meal from scratch every time someone orders, you prepare a massive batch in advance and serve portions.",
            "technical_explanation": "A Materialized View stores the physical result of a complex query on disk. When queried, it returns immediately. The trade-off is that it must be periodically refreshed, so data might be slightly stale.",
            "why_it_matters": "Crucial for dashboards and analytical workloads where massive aggregations are required instantly.",
            "remember": "Materialized views trade real-time freshness for blazing fast aggregations."
          }
        ]
      },
      {
        "title": "Module 8: Finding the Pattern",
        "blocks": [
          {
            "type": "story",
            "title": "The 72-Hour Anomaly",
            "text": "You realize the researchers are running a query checking both the frequency range AND the exact origin sector of the bursts. You need to build the perfect index to make this query instant."
          },
          {
            "type": "sql_sandbox",
            "title": "Creating the Composite Index",
            "context": "The table `bursts` has columns `id`, `frequency`, `sector`, `timestamp`. The query is ALWAYS `WHERE sector = ? AND frequency > ?`. Create the optimal index.",
            "init_script": "CREATE TABLE bursts (id INT, frequency INT, sector TEXT, timestamp DATETIME);",
            "solution_query": "CREATE INDEX idx_sector_freq ON bursts (sector, frequency);",
            "hint": "Order matters. Equality checks (sector =) should usually precede range checks (frequency >) in a composite index.",
            "explanation": "By putting the equality condition first, the B-Tree immediately jumps to the exact sector, and then uses the sorted frequency within that sector to quickly evaluate the range."
          }
        ]
      }
    ]
  },
  "3": {
    "format": "episodic",
    "episodes": [
      {
        "title": "Module 1: The Contradictory Implant",
        "blocks": [
          {
            "type": "story",
            "title": "Fractured Memories",
            "text": "A neural implant contains multiple contradictory versions of one person's life. Addresses don't match zip codes, job titles don't match salaries. The data is corrupting the host's mind."
          },
          {
            "type": "problem",
            "text": "You must normalize the database to eliminate anomalies and restore a single consistent memory."
          },
          {
            "type": "concept",
            "title": "Data Anomalies",
            "explanation": "Unnormalized data suffers from Insert, Update, and Delete anomalies.",
            "analogy": "If you write your friend's new phone number in an address book, but forget to update the sticky note on your fridge, you have contradictory data.",
            "technical_explanation": "Anomalies occur when facts are stored in multiple places unnecessarily.",
            "why_it_matters": "Data integrity is impossible if facts can contradict themselves.",
            "remember": "One fact, one place."
          }
        ]
      },
      {
        "title": "Module 2: Functional Dependencies",
        "blocks": [
          {
            "type": "concept",
            "title": "The Core of Normalization",
            "explanation": "A functional dependency means if you know X, you definitively know Y.",
            "analogy": "If you know a car's VIN, you definitively know its color.",
            "technical_explanation": "Expressed as X -> Y. X is the determinant. This is the basis for all normal forms.",
            "why_it_matters": "Without identifying FDs, you cannot normalize a database.",
            "remember": "Does X uniquely determine Y?"
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "SSN -> Name, DOB\nZipCode -> City, State"
          },
          {
            "type": "micro_challenge",
            "question": "If EmployeeID determines Department, and Department determines Manager, what type of dependency is this?",
            "options": [
              "Partial",
              "Transitive",
              "Trivial"
            ],
            "answer": "Transitive",
            "explanation": "The dependency passes through an intermediary non-key attribute."
          }
        ]
      },
      {
        "title": "Module 3: First Normal Form (1NF)",
        "blocks": [
          {
            "type": "concept",
            "title": "Atomic Values",
            "explanation": "1NF requires that every column holds a single, atomic value.",
            "analogy": "Don't stuff an entire grocery list into a single receipt line item.",
            "technical_explanation": "No repeating groups or arrays. Each intersection of row and column must be scalar.",
            "why_it_matters": "Searching inside a comma-separated string is slow and error-prone.",
            "remember": "Atomicity above all."
          },
          {
            "type": "sql_sandbox",
            "title": "Unnesting Data",
            "context": "A table `logs` has a column `tags` containing comma-separated values. We won't fix it in SQL yet, just create a new table `log_tags` to represent the 1NF version.",
            "init_script": "",
            "solution_query": "CREATE TABLE log_tags (log_id INT, tag VARCHAR(50), PRIMARY KEY(log_id, tag));",
            "hint": "Create a table with a composite primary key of log_id and tag.",
            "explanation": "Data is now atomic and easily queryable."
          }
        ]
      },
      {
        "title": "Module 4: Second Normal Form (2NF)",
        "blocks": [
          {
            "type": "concept",
            "title": "Removing Partial Dependencies",
            "explanation": "2NF requires 1NF, and no partial dependencies on a composite primary key.",
            "analogy": "If a key requires two locks, a fact shouldn't be accessible with just one of the keys.",
            "technical_explanation": "All non-key attributes must depend on the ENTIRE primary key.",
            "why_it_matters": "Prevents redundant data when dealing with intersection tables.",
            "remember": "Only relevant for composite keys."
          },
          {
            "type": "debugger",
            "title": "The Composite Flaw",
            "scenario": "Table: OrderDetails(OrderID, ProductID, ProductName). ProductName depends only on ProductID.",
            "options": [
              "It is in 2NF",
              "Violates 2NF",
              "Violates 1NF"
            ],
            "answer": "Violates 2NF",
            "explanation": "ProductName is partially dependent on the composite key (OrderID, ProductID)."
          }
        ]
      },
      {
        "title": "Module 5: Third Normal Form (3NF)",
        "blocks": [
          {
            "type": "concept",
            "title": "Removing Transitive Dependencies",
            "explanation": "3NF requires 2NF, and no transitive dependencies.",
            "analogy": "Don't store the manager's name in the employee record. Store the department ID, and let the department table hold the manager's name.",
            "technical_explanation": "Every non-key attribute must depend 'the key, the whole key, and nothing but the key, so help me Codd'.",
            "why_it_matters": "Eliminates the risk of updating an employee's department but forgetting to update their manager.",
            "remember": "No non-key attribute should depend on another non-key attribute."
          },
          {
            "type": "sql_sandbox",
            "title": "Normalize to 3NF",
            "context": "Extract the department data into its own table.",
            "init_script": "",
            "solution_query": "CREATE TABLE departments (id INT PRIMARY KEY, manager_name VARCHAR(100));",
            "hint": "Create a departments table with id and manager_name.",
            "explanation": "You've removed the transitive dependency from the employee records."
          }
        ]
      },
      {
        "title": "Module 6: Boyce-Codd Normal Form (BCNF)",
        "blocks": [
          {
            "type": "concept",
            "title": "The Stricter 3NF",
            "explanation": "BCNF handles edge cases where overlapping candidate keys exist.",
            "analogy": "Closing the final loophole in the law.",
            "technical_explanation": "For every non-trivial dependency X -> Y, X must be a superkey.",
            "why_it_matters": "Resolves anomalies in complex schemas that 3NF technically allows.",
            "remember": "Every determinant must be a candidate key."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "If Student, Course -> Professor\nAnd Professor -> Course\nThen Professor must be a key in a separated table."
          }
        ]
      },
      {
        "title": "Module 7: The Price of Normalization",
        "blocks": [
          {
            "type": "concept",
            "title": "Denormalization",
            "explanation": "Sometimes, joining 10 perfectly normalized tables is too slow.",
            "analogy": "Sometimes it's better to keep a copy of a document on your desk rather than walking to the archive every time.",
            "technical_explanation": "Intentionally violating normal forms to improve read performance at the cost of write complexity.",
            "why_it_matters": "Real-world databases balance theoretical purity with practical performance.",
            "remember": "Normalize until it hurts, denormalize until it works."
          },
          {
            "type": "reflection",
            "question": "In a heavy read-only analytical database, would you prefer 3NF or a denormalized schema?"
          }
        ]
      },
      {
        "title": "Module 8: Memory Reconstruction",
        "blocks": [
          {
            "type": "sql_sandbox",
            "title": "Restore the Mind",
            "context": "Create a 3NF compliant schema for a person's addresses. A person can have multiple addresses. Zip codes dictate the City.",
            "init_script": "",
            "solution_query": "CREATE TABLE zip_codes (zip VARCHAR(10) PRIMARY KEY, city VARCHAR(100)); CREATE TABLE addresses (id INT PRIMARY KEY, person_id INT, street VARCHAR(200), zip VARCHAR(10));",
            "hint": "Create two tables: zip_codes (zip, city) and addresses (id, person_id, street, zip).",
            "explanation": "The implant's memories are now perfectly consistent. The host's mind is clear."
          }
        ]
      }
    ]
  },
  "6": {
    "format": "episodic",
    "episodes": [
      {
        "title": "Module 1: Wildfire & The Need for Transactions",
        "blocks": [
          {
            "type": "story",
            "title": "The Spreading Blaze",
            "text": "A massive wildfire is spreading towards the city. Fire command, police, and transit authorities are all desperately updating the central Evacuation Route database at the exact same time."
          },
          {
            "type": "problem",
            "text": "Concurrent updates are corrupting data. Police mark a route 'Open' exactly when Fire marks it 'Blocked', resulting in chaotic overrides."
          },
          {
            "type": "concept",
            "title": "Database Transactions",
            "explanation": "A transaction is a logical unit of work that contains one or more SQL statements. It must succeed completely or fail completely.",
            "analogy": "A bank transfer. Taking money from Account A and giving it to Account B must both happen, or neither happens. You can't just do half.",
            "technical_explanation": "Transactions ensure data integrity by bundling operations. Managed with BEGIN, COMMIT, and ROLLBACK.",
            "why_it_matters": "Prevents partial updates from leaving the database in an inconsistent state.",
            "remember": "All or nothing."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "BEGIN;\nUPDATE Route A;\nUPDATE Route B;\nCOMMIT; (or ROLLBACK;)"
          },
          {
            "type": "worked_example",
            "title": "A Safe Update",
            "steps": [
              "1. BEGIN TRANSACTION;",
              "2. Execute updates.",
              "3. COMMIT;"
            ]
          },
          {
            "type": "reflection",
            "question": "What happens if the server crashes right after the first UPDATE but before the COMMIT?"
          },
          {
            "type": "micro_challenge",
            "question": "Which command cancels a transaction?",
            "options": [
              "CANCEL",
              "ROLLBACK",
              "ABORT"
            ],
            "answer": "ROLLBACK",
            "explanation": "ROLLBACK undoes all changes made during the current transaction."
          },
          {
            "type": "sql_sandbox",
            "title": "Safe Route Update",
            "context": "Wrap the update of route 1 to 'Blocked' in a transaction.",
            "init_script": "CREATE TABLE routes (id INT, status TEXT); INSERT INTO routes VALUES (1, 'Open');",
            "solution_query": "BEGIN;\nUPDATE routes SET status = 'Blocked' WHERE id = 1;\nCOMMIT;",
            "hint": "BEGIN; UPDATE ... COMMIT;",
            "explanation": "The transaction ensured the update was atomic."
          }
        ]
      },
      {
        "title": "Module 2: ACID Properties",
        "blocks": [
          {
            "type": "story",
            "title": "The Four Pillars",
            "text": "The Chief Engineer arrives. 'If this system goes down during the evacuation, we lose lives. The database must be ACID compliant!'"
          },
          {
            "type": "problem",
            "text": "We need a strict set of guarantees for transaction reliability."
          },
          {
            "type": "concept",
            "title": "ACID",
            "explanation": "Atomicity (All or nothing), Consistency (Follows all rules/constraints), Isolation (Transactions don't interfere), Durability (Committed data survives crashes).",
            "analogy": "Atomicity = Marriage (both say yes, or it fails). Consistency = The paperwork is legal. Isolation = Private ceremony. Durability = The marriage certificate is in a fireproof safe.",
            "technical_explanation": "These four properties guarantee that database transactions are processed reliably.",
            "why_it_matters": "The core fundamental theory of relational database design.",
            "remember": "Atomicity, Consistency, Isolation, Durability."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "A - Atomic (Indivisible)\nC - Consistent (Valid state to Valid state)\nI - Isolated (Invisible to others until commit)\nD - Durable (Saved to disk)"
          },
          {
            "type": "worked_example",
            "title": "Identifying ACID Violations",
            "steps": [
              "1. A crash loses data? Durability violation.",
              "2. Half a transfer completes? Atomicity violation."
            ]
          },
          {
            "type": "reflection",
            "question": "If a transaction violates a FOREIGN KEY constraint and is rolled back, which ACID property caused the rollback?"
          },
          {
            "type": "debugger",
            "title": "ACID Match",
            "scenario": "A power outage occurs, but upon reboot, the last committed transaction is still there.",
            "options": [
              "Atomicity",
              "Durability",
              "Isolation"
            ],
            "answer": "Durability",
            "explanation": "Durability guarantees that once committed, data survives hardware or power failures."
          },
          {
            "type": "sql_sandbox",
            "title": "Constraint Consistency",
            "context": "Try to insert a NULL into a NOT NULL column to see Consistency block the transaction.",
            "init_script": "CREATE TABLE safe (id INT NOT NULL);",
            "solution_query": "INSERT INTO safe VALUES (1);",
            "hint": "Just insert a valid integer to pass.",
            "explanation": "If you tried NULL, it would fail, protecting Consistency."
          }
        ]
      },
      {
        "title": "Module 3: Concurrency Issues: Dirty Reads",
        "blocks": [
          {
            "type": "story",
            "title": "The Phantom Clear",
            "text": "Police checked a route and saw it marked 'Clear'. They sent civilians. But Fire Command had just marked it 'Clear' temporarily, then rolled it back to 'Blocked'! The police read uncommitted data!"
          },
          {
            "type": "problem",
            "text": "Reading data from a transaction that hasn't committed yet (Dirty Read)."
          },
          {
            "type": "concept",
            "title": "Dirty Reads & Non-repeatable Reads",
            "explanation": "Dirty Read: Reading uncommitted changes. Non-repeatable Read: Reading a row, another transaction updates it and commits, you read it again and it changed.",
            "analogy": "Dirty Read is reading someone's rough draft of an email before they send it. They might delete it entirely.",
            "technical_explanation": "Occurs when isolation levels are too low. It prioritizes speed over accuracy.",
            "why_it_matters": "Causes catastrophic real-world decision errors based on phantom data.",
            "remember": "Dirty = Uncommitted."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "T1: UPDATE route (uncommitted)\nT2: SELECT route (reads new value! DIRTY)\nT1: ROLLBACK (the value T2 read never truly existed)"
          },
          {
            "type": "worked_example",
            "title": "The Danger Zone",
            "steps": [
              "1. T1 starts.",
              "2. T1 updates X.",
              "3. T2 reads X.",
              "4. T1 rolls back. T2's data is invalid."
            ]
          },
          {
            "type": "reflection",
            "question": "Why might a database allow dirty reads at all?"
          },
          {
            "type": "micro_challenge",
            "question": "What concurrency issue involves reading the same row twice in a transaction and getting two different committed values?",
            "options": [
              "Dirty Read",
              "Non-repeatable Read",
              "Phantom Read"
            ],
            "answer": "Non-repeatable Read",
            "explanation": "Because another transaction committed an update between your two reads."
          },
          {
            "type": "sql_sandbox",
            "title": "Observe the Rollback",
            "context": "Start a transaction, update `status` to 'Blocked', then ROLLBACK.",
            "init_script": "CREATE TABLE routes (id INT, status TEXT); INSERT INTO routes VALUES (1, 'Open');",
            "solution_query": "BEGIN;\nUPDATE routes SET status = 'Blocked';\nROLLBACK;\nSELECT * FROM routes;",
            "hint": "BEGIN; UPDATE ... ROLLBACK; SELECT ...",
            "explanation": "The status remains 'Open'. Anyone who read 'Blocked' during the transaction would have had a Dirty Read."
          }
        ]
      },
      {
        "title": "Module 4: Isolation Levels",
        "blocks": [
          {
            "type": "story",
            "title": "Locking Down the Grid",
            "text": "'We must prevent these dirty reads!' the Chief yells. 'Adjust the database isolation level immediately!'"
          },
          {
            "type": "problem",
            "text": "We need to configure the database engine's strictness regarding concurrency."
          },
          {
            "type": "concept",
            "title": "Isolation Levels",
            "explanation": "Read Uncommitted (allows dirty reads), Read Committed (prevents dirty reads), Repeatable Read (prevents non-repeatable reads), Serializable (prevents all anomalies, including phantoms).",
            "analogy": "Read Uncommitted = Peeking through the window. Serializable = Waiting in line for a private room.",
            "technical_explanation": "Higher isolation = higher data safety but lower concurrency (slower, more locking).",
            "why_it_matters": "The classic tradeoff between performance and accuracy in databases.",
            "remember": "Serializable is safest, but slowest."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "Isolation | Dirty Read | Non-Repeatable | Phantom\nUncommitted | YES | YES | YES\nCommitted   | NO  | YES | YES\nRepeatable  | NO  | NO  | YES\nSerializable| NO  | NO  | NO"
          },
          {
            "type": "worked_example",
            "title": "Setting Isolation",
            "steps": [
              "1. SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;",
              "2. BEGIN TRANSACTION;"
            ]
          },
          {
            "type": "reflection",
            "question": "Why is 'Read Committed' the default for many modern databases?"
          },
          {
            "type": "debugger",
            "title": "Select the Level",
            "scenario": "You need to run a financial report and ensure no data changes while you sum the columns.",
            "options": [
              "Read Uncommitted",
              "Serializable"
            ],
            "answer": "Serializable",
            "explanation": "Serializable ensures a perfectly consistent snapshot with no interference."
          },
          {
            "type": "sql_sandbox",
            "title": "Syntax Check",
            "context": "Although SQLite sandbox limits this, write a query that SELECTs everything from routes.",
            "init_script": "CREATE TABLE routes (id INT, status TEXT); INSERT INTO routes VALUES (1, 'Open');",
            "solution_query": "SELECT * FROM routes;",
            "hint": "SELECT * FROM routes;",
            "explanation": "In a real database, you'd use SET TRANSACTION ISOLATION LEVEL before this."
          }
        ]
      },
      {
        "title": "Module 5: Locks & 2-Phase Locking (2PL)",
        "blocks": [
          {
            "type": "story",
            "title": "Holding the Key",
            "text": "To achieve isolation, the database uses locks. Fire Command locks a route record so Police can't touch it until Fire is done."
          },
          {
            "type": "problem",
            "text": "How does the database physically enforce isolation?"
          },
          {
            "type": "concept",
            "title": "Locks and 2PL",
            "explanation": "Shared (Read) Locks allow others to read but not write. Exclusive (Write) Locks prevent others from reading or writing. Two-Phase Locking (2PL) means a transaction acquires all locks it needs (Growing Phase) and then releases them (Shrinking Phase), never acquiring a lock after releasing one.",
            "analogy": "Exclusive Lock: Locking the bathroom door. Shared Lock: Looking at a painting in a museum (others can look, no one can alter it).",
            "technical_explanation": "2PL guarantees serializability by preventing conflicts.",
            "why_it_matters": "Understanding locks helps debug blocked queries and performance bottlenecks.",
            "remember": "Write locks block everything."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "T1 (Write Lock on A) ---> T2 (Requests Read Lock on A) -> BLOCKED until T1 commits."
          },
          {
            "type": "worked_example",
            "title": "Locking behavior",
            "steps": [
              "1. T1: UPDATE A (Exclusive Lock).",
              "2. T2: SELECT A (Blocked).",
              "3. T1: COMMIT (Lock released). T2 proceeds."
            ]
          },
          {
            "type": "reflection",
            "question": "Why does a Write lock block Read locks?"
          },
          {
            "type": "micro_challenge",
            "question": "In 2PL, can a transaction acquire a new lock after it has released an old lock?",
            "options": [
              "Yes",
              "No"
            ],
            "answer": "No",
            "explanation": "2PL enforces a strict growing phase (acquiring) followed by a shrinking phase (releasing)."
          },
          {
            "type": "sql_sandbox",
            "title": "Simulate a Lock (Conceptual)",
            "context": "Just run a basic UPDATE. In the real world, this acquires an Exclusive lock.",
            "init_script": "CREATE TABLE routes (id INT); INSERT INTO routes VALUES (1);",
            "solution_query": "UPDATE routes SET id = 2;",
            "hint": "UPDATE routes SET id = 2;",
            "explanation": "The database silently locked the row to do this."
          }
        ]
      },
      {
        "title": "Module 6: Deadlocks",
        "blocks": [
          {
            "type": "story",
            "title": "The Standoff",
            "text": "Fire Command has Route A and needs Route B. Police has Route B and needs Route A. Both are waiting. Neither will yield. The system is frozen!"
          },
          {
            "type": "problem",
            "text": "Two or more transactions are permanently blocking each other."
          },
          {
            "type": "concept",
            "title": "Deadlock",
            "explanation": "A deadlock occurs when two transactions each hold a lock that the other needs. The database engine must intervene, kill one transaction (the victim), and roll it back.",
            "analogy": "Two cars meet on a narrow one-lane bridge. Neither can move forward until the other backs up.",
            "technical_explanation": "Databases use cycle-detection algorithms in their lock manager to find deadlocks.",
            "why_it_matters": "A common cause of random application errors. Requires application-side retry logic.",
            "remember": "Circular wait."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "T1 locks A, requests B.\nT2 locks B, requests A.\nDEADLOCK!"
          },
          {
            "type": "worked_example",
            "title": "Deadlock Resolution",
            "steps": [
              "1. DB detects cycle.",
              "2. DB kills T2.",
              "3. T1 proceeds.",
              "4. App receives error for T2 and must retry."
            ]
          },
          {
            "type": "reflection",
            "question": "How can an application prevent deadlocks structurally?"
          },
          {
            "type": "debugger",
            "title": "Deadlock Avoidance",
            "scenario": "Your code frequently deadlocks.",
            "options": [
              "Use NO LOCK",
              "Always update tables in the exact same order"
            ],
            "answer": "Always update tables in the exact same order",
            "explanation": "If all transactions lock A before locking B, cycles cannot form."
          },
          {
            "type": "sql_sandbox",
            "title": "Deadlock Awareness",
            "context": "We can't trigger a true deadlock in this sandbox. Write a query to update route A (id=1) then route B (id=2) sequentially.",
            "init_script": "CREATE TABLE r (id INT, val TEXT); INSERT INTO r VALUES (1, 'A'), (2, 'B');",
            "solution_query": "BEGIN;\nUPDATE r SET val = 'X' WHERE id = 1;\nUPDATE r SET val = 'Y' WHERE id = 2;\nCOMMIT;",
            "hint": "Wrap two updates in a transaction.",
            "explanation": "Consistent ordering prevents deadlocks."
          }
        ]
      },
      {
        "title": "Module 7: Recovery and Write-Ahead Logging (WAL)",
        "blocks": [
          {
            "type": "story",
            "title": "The Power Outage",
            "text": "Boom! The command center loses power. When the servers reboot, the Chief panics. 'Did we lose the evacuation routes?!'"
          },
          {
            "type": "problem",
            "text": "How does a database guarantee Durability and Atomicity across hardware crashes?"
          },
          {
            "type": "concept",
            "title": "Write-Ahead Logging (WAL)",
            "explanation": "Before changing the actual database file, the database engine writes a record of the intended change to a sequential log file. If a crash occurs, the database replays the log to recover.",
            "analogy": "Writing down 'I am going to pay Bob $50' in a ledger BEFORE actually handing Bob the money.",
            "technical_explanation": "Ensures atomicity and durability. Uncommitted transactions in the log are ignored on reboot (Atomicity). Committed transactions not yet written to the main data file are replayed (Durability).",
            "why_it_matters": "The magic behind crash recovery.",
            "remember": "Log it before you do it."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "1. App requests UPDATE.\n2. DB writes to WAL (disk).\n3. DB replies 'Success'.\n4. DB slowly updates actual data file."
          },
          {
            "type": "worked_example",
            "title": "Crash Recovery",
            "steps": [
              "1. DB Boots.",
              "2. Reads WAL.",
              "3. Re-applies committed changes.",
              "4. Discards uncommitted changes."
            ]
          },
          {
            "type": "reflection",
            "question": "Why write to the log first instead of just writing directly to the data file?"
          },
          {
            "type": "micro_challenge",
            "question": "What is the primary purpose of WAL?",
            "options": [
              "Faster queries",
              "Crash recovery and Durability",
              "Preventing dirty reads"
            ],
            "answer": "Crash recovery and Durability",
            "explanation": "WAL is specifically designed to survive unexpected crashes."
          },
          {
            "type": "sql_sandbox",
            "title": "Commit the Change",
            "context": "Commit an update. Conceptually, this is when the WAL syncs to disk.",
            "init_script": "CREATE TABLE t (id INT); INSERT INTO t VALUES (1);",
            "solution_query": "BEGIN;\nUPDATE t SET id = 2;\nCOMMIT;",
            "hint": "BEGIN; UPDATE; COMMIT;",
            "explanation": "Upon COMMIT, the WAL guarantees this change survives a crash."
          }
        ]
      },
      {
        "title": "Module 8: Final Coordination Challenge",
        "blocks": [
          {
            "type": "story",
            "title": "The Final Push",
            "text": "The fire is contained. We need to execute one massive, safe transaction to move all 'Evacuating' sectors to 'Safe', ensuring no partial updates occur."
          },
          {
            "type": "problem",
            "text": "Execute a flawless transaction integrating DML."
          },
          {
            "type": "concept",
            "title": "Transaction Mastery",
            "explanation": "Putting it all together. A well-formed transaction guarantees ACID properties and protects the system.",
            "analogy": "The final synchronized movement of a symphony orchestra.",
            "technical_explanation": "Requires BEGIN, the correct UPDATE statement, and a COMMIT.",
            "why_it_matters": "This is how all modern applications interact safely with databases.",
            "remember": "Trust the transaction."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "[BEGIN] ---> [UPDATE] ---> [COMMIT] ---> (SAFE)"
          },
          {
            "type": "worked_example",
            "title": "The Final Script",
            "steps": [
              "1. Open transaction.",
              "2. Execute DML.",
              "3. Close transaction."
            ]
          },
          {
            "type": "reflection",
            "question": "How has learning about ACID changed how you will write backend code?"
          },
          {
            "type": "debugger",
            "title": "Missing Keyword",
            "scenario": "Your code has `UPDATE...` followed by `COMMIT;` but it throws an error.",
            "options": [
              "Missing BEGIN",
              "Missing ROLLBACK"
            ],
            "answer": "Missing BEGIN",
            "explanation": "You cannot commit a transaction that was never explicitly started (in explicit transaction mode)."
          },
          {
            "type": "sql_sandbox",
            "title": "Secure the Sectors",
            "context": "Start a transaction, update all rows where status is 'Evacuating' to 'Safe', and commit.",
            "init_script": "CREATE TABLE sectors (id INT, status TEXT); INSERT INTO sectors VALUES (1, 'Evacuating'), (2, 'Evacuating'), (3, 'Clear');",
            "solution_query": "BEGIN;\nUPDATE sectors SET status = 'Safe' WHERE status = 'Evacuating';\nCOMMIT;",
            "hint": "BEGIN; UPDATE sectors SET status = 'Safe' WHERE status = 'Evacuating'; COMMIT;",
            "explanation": "You safely updated the database. The city is safe!"
          }
        ]
      }
    ]
  },
  "5": {
    "format": "episodic",
    "episodes": [
      {
        "title": "Module 1: The Ancient Ledger & Intro to JOINs",
        "blocks": [
          {
            "type": "story",
            "title": "The Merchant's Secret",
            "text": "You uncover an ancient merchant ledger containing 200,000 transactions. But the ledger only has IDs. The names of the merchants are in a separate tome. We must combine them."
          },
          {
            "type": "problem",
            "text": "Data is split across multiple tables based on foreign keys. We need a unified view."
          },
          {
            "type": "concept",
            "title": "INNER JOIN",
            "explanation": "INNER JOIN combines rows from two tables based on a related column, returning only rows that have matching values in both tables.",
            "analogy": "Matching puzzle pieces. Only pieces that fit perfectly together make it into the final picture.",
            "technical_explanation": "Performs a cartesian product filtered by the ON condition. It's the intersection of the two sets.",
            "why_it_matters": "The fundamental way to reconstruct normalized data into readable formats.",
            "remember": "Matches only."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "Table A (1,2) INNER JOIN Table B (2,3)\nResult: (2)"
          },
          {
            "type": "worked_example",
            "title": "Writing an INNER JOIN",
            "steps": [
              "1. SELECT columns.",
              "2. FROM table1.",
              "3. INNER JOIN table2 ON table1.id = table2.fk_id."
            ]
          },
          {
            "type": "reflection",
            "question": "What happens to rows in Table A that have no match in Table B during an INNER JOIN?"
          },
          {
            "type": "micro_challenge",
            "question": "If Table A has 5 rows and Table B has 5 rows, what is the maximum number of rows an INNER JOIN could return if every row matched every other row?",
            "options": [
              "5",
              "10",
              "25"
            ],
            "answer": "25",
            "explanation": "A cartesian product (all match all) would result in 5 * 5 = 25 rows."
          },
          {
            "type": "sql_sandbox",
            "title": "Reconstruct the Ledger",
            "context": "Join `transactions` and `merchants` on `merchant_id`.",
            "init_script": "CREATE TABLE merchants (id INT, name TEXT); CREATE TABLE transactions (id INT, merchant_id INT, amount INT); INSERT INTO merchants VALUES (1, 'Sal'), (2, 'Boz'); INSERT INTO transactions VALUES (101, 1, 500);",
            "solution_query": "SELECT m.name, t.amount FROM merchants m INNER JOIN transactions t ON m.id = t.merchant_id;",
            "hint": "SELECT m.name, t.amount FROM merchants m INNER JOIN transactions t ON ...",
            "explanation": "You've successfully joined the tables to see Sal's transaction."
          }
        ]
      },
      {
        "title": "Module 2: Left, Right, and Full Outer JOINs",
        "blocks": [
          {
            "type": "story",
            "title": "The Missing Merchants",
            "text": "Wait. Some merchants in the tome have NO transactions in the ledger. We need a list of ALL merchants, even if they haven't traded!"
          },
          {
            "type": "problem",
            "text": "INNER JOIN drops merchants without transactions. We need to preserve the left table's rows."
          },
          {
            "type": "concept",
            "title": "OUTER JOINs",
            "explanation": "LEFT JOIN keeps all rows from the left table, padding with NULLs if there's no match. RIGHT JOIN does the same for the right table. FULL JOIN keeps all rows from both.",
            "analogy": "Inviting all your friends to a party. LEFT JOIN means all your friends show up, even if they don't bring a gift (the right table).",
            "technical_explanation": "An OUTER JOIN is an INNER JOIN plus the unmatched rows from one or both tables.",
            "why_it_matters": "Crucial for finding missing data (e.g., finding users who haven't made a purchase).",
            "remember": "LEFT keeps the LEFT."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "Table A (1,2) LEFT JOIN Table B (2,3)\nResult: (1, NULL), (2, matched_data)"
          },
          {
            "type": "worked_example",
            "title": "Finding Missing Data",
            "steps": [
              "1. LEFT JOIN merchants to transactions.",
              "2. Add WHERE transactions.id IS NULL to find merchants with no trades."
            ]
          },
          {
            "type": "reflection",
            "question": "Why do we use `IS NULL` instead of `= NULL` when checking for missing matches?"
          },
          {
            "type": "debugger",
            "title": "Null Handling",
            "scenario": "A LEFT JOIN query is missing rows it should have.",
            "options": [
              "Used INNER JOIN by mistake",
              "Put a right-table condition in the WHERE clause instead of ON",
              "Both"
            ],
            "answer": "Put a right-table condition in the WHERE clause instead of ON",
            "explanation": "Filtering the right table in the WHERE clause turns a LEFT JOIN into an INNER JOIN because NULLs fail the WHERE condition."
          },
          {
            "type": "sql_sandbox",
            "title": "Find Idle Merchants",
            "context": "Use a LEFT JOIN to list ALL merchants, and their transaction amounts (which will be NULL for idle ones).",
            "init_script": "CREATE TABLE m (id INT, name TEXT); CREATE TABLE t (merchant_id INT, amount INT); INSERT INTO m VALUES (1, 'Sal'), (2, 'Boz'); INSERT INTO t VALUES (1, 500);",
            "solution_query": "SELECT m.name, t.amount FROM m LEFT JOIN t ON m.id = t.merchant_id;",
            "hint": "SELECT ... FROM m LEFT JOIN t ON m.id = t.merchant_id",
            "explanation": "Boz shows up with a NULL amount."
          }
        ]
      },
      {
        "title": "Module 3: GROUP BY and Aggregations",
        "blocks": [
          {
            "type": "story",
            "title": "The Grand Totals",
            "text": "The ledger is too vast. 'I don't need every transaction,' the Guild Master barks. 'I need the TOTAL gold each merchant has traded!'"
          },
          {
            "type": "problem",
            "text": "We need to collapse multiple rows into summary rows based on a specific category."
          },
          {
            "type": "concept",
            "title": "GROUP BY",
            "explanation": "GROUP BY groups rows that have the same values in specified columns into summary rows, usually to perform aggregate functions (SUM, COUNT, AVG).",
            "analogy": "Sorting a giant jar of coins into piles of pennies, nickels, and dimes, then counting the total in each pile.",
            "technical_explanation": "The database engine sorts/hashes the data by the grouping column, then applies the aggregate function to each bucket.",
            "why_it_matters": "The foundation of all data analysis and reporting.",
            "remember": "Aggregate the rest, GROUP BY the best."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "Rows: (A, 10), (A, 20), (B, 5)\nGROUP BY Name, SUM(Val)\nResult: (A, 30), (B, 5)"
          },
          {
            "type": "worked_example",
            "title": "Summing Transactions",
            "steps": [
              "1. SELECT merchant_id, SUM(amount).",
              "2. FROM transactions.",
              "3. GROUP BY merchant_id."
            ]
          },
          {
            "type": "reflection",
            "question": "What happens if you SELECT a column that is not in the GROUP BY and not in an aggregate function?"
          },
          {
            "type": "micro_challenge",
            "question": "Which function counts the number of rows in a group?",
            "options": [
              "SUM()",
              "COUNT()",
              "TOTAL()"
            ],
            "answer": "COUNT()",
            "explanation": "COUNT() tallies the rows, SUM() adds up numeric values."
          },
          {
            "type": "sql_sandbox",
            "title": "Calculate Totals",
            "context": "Get the `merchant_id` and the SUM of `amount` for each merchant.",
            "init_script": "CREATE TABLE t (merchant_id INT, amount INT); INSERT INTO t VALUES (1, 100), (1, 200), (2, 50);",
            "solution_query": "SELECT merchant_id, SUM(amount) FROM t GROUP BY merchant_id;",
            "hint": "Use SUM(amount) and GROUP BY merchant_id.",
            "explanation": "Merchant 1 correctly shows 300."
          }
        ]
      },
      {
        "title": "Module 4: HAVING vs WHERE",
        "blocks": [
          {
            "type": "story",
            "title": "The Elite Merchants",
            "text": "'Excellent,' says the Master. 'Now, show me ONLY the merchants whose total trade volume exceeds 10,000 gold.'"
          },
          {
            "type": "problem",
            "text": "We cannot use WHERE to filter by an aggregate sum, because WHERE filters rows *before* aggregation."
          },
          {
            "type": "concept",
            "title": "HAVING Clause",
            "explanation": "HAVING is used to filter groups *after* the GROUP BY and aggregations have been calculated.",
            "analogy": "WHERE is the bouncer at the club door (filters individuals). HAVING is kicking out a VIP table if their total bill isn't high enough (filters groups).",
            "technical_explanation": "SQL Order of Execution: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT. Therefore, HAVING can see aggregate results.",
            "why_it_matters": "Essential for filtering based on totals, averages, or counts.",
            "remember": "WHERE before grouping, HAVING after."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "WHERE amount > 100 (filters raw rows)\nHAVING SUM(amount) > 10000 (filters summary rows)"
          },
          {
            "type": "worked_example",
            "title": "Filtering Groups",
            "steps": [
              "1. Write the GROUP BY query.",
              "2. Append HAVING SUM(amount) > 10000."
            ]
          },
          {
            "type": "reflection",
            "question": "Can you use both WHERE and HAVING in the same query?"
          },
          {
            "type": "debugger",
            "title": "Execution Order Error",
            "scenario": "A query `WHERE SUM(amount) > 100` throws an error.",
            "options": [
              "Change WHERE to HAVING",
              "Remove GROUP BY",
              "Change SUM to COUNT"
            ],
            "answer": "Change WHERE to HAVING",
            "explanation": "Aggregate functions cannot be evaluated in the WHERE clause."
          },
          {
            "type": "sql_sandbox",
            "title": "Find the Elite",
            "context": "Select `merchant_id` and `SUM(amount)` where the total sum is strictly greater than 200.",
            "init_script": "CREATE TABLE t (merchant_id INT, amount INT); INSERT INTO t VALUES (1, 100), (1, 150), (2, 50);",
            "solution_query": "SELECT merchant_id, SUM(amount) FROM t GROUP BY merchant_id HAVING SUM(amount) > 200;",
            "hint": "Use HAVING SUM(amount) > 200 after your GROUP BY.",
            "explanation": "Only merchant 1 (250) is returned."
          }
        ]
      },
      {
        "title": "Module 5: Window Functions: OVER and PARTITION BY",
        "blocks": [
          {
            "type": "story",
            "title": "The Running Ledger",
            "text": "A dark conspiracy is afoot. We need to see every transaction alongside the merchant's running total, without collapsing the rows!"
          },
          {
            "type": "problem",
            "text": "GROUP BY collapses rows. We want to see aggregate data (like a total) appended to *every individual row*."
          },
          {
            "type": "concept",
            "title": "Window Functions",
            "explanation": "Window functions perform calculations across a set of table rows related to the current row, but unlike aggregate functions, they do not cause rows to become grouped into a single output row.",
            "analogy": "Looking through a moving window at a specific subset of data, calculating a stat for that window, and writing it down next to the current row.",
            "technical_explanation": "Uses the `OVER()` clause. `PARTITION BY` defines the window (like GROUP BY). `ORDER BY` within the window defines running totals.",
            "why_it_matters": "Crucial for running totals, rankings, and moving averages.",
            "remember": "Aggregate power, row-level detail."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "SELECT id, amount, SUM(amount) OVER (PARTITION BY merchant_id) as total_for_merchant"
          },
          {
            "type": "worked_example",
            "title": "A Simple Window",
            "steps": [
              "1. Write a normal SELECT.",
              "2. Add a window function: SUM(amount) OVER (PARTITION BY merchant_id)."
            ]
          },
          {
            "type": "reflection",
            "question": "How does `PARTITION BY` differ from `GROUP BY`?"
          },
          {
            "type": "micro_challenge",
            "question": "Which clause is used to define a window function?",
            "options": [
              "GROUP BY",
              "OVER",
              "WINDOW"
            ],
            "answer": "OVER",
            "explanation": "The OVER clause dictates how the window is partitioned and ordered."
          },
          {
            "type": "sql_sandbox",
            "title": "Append the Totals",
            "context": "Select `id`, `amount`, and the total amount for that merchant using a window function.",
            "init_script": "CREATE TABLE t (id INT, m_id INT, amount INT); INSERT INTO t VALUES (1, 1, 10), (2, 1, 20), (3, 2, 50);",
            "solution_query": "SELECT id, amount, SUM(amount) OVER (PARTITION BY m_id) FROM t;",
            "hint": "Use SUM(amount) OVER (PARTITION BY m_id)",
            "explanation": "Rows 1 and 2 now both show 30 as their partition total."
          }
        ]
      },
      {
        "title": "Module 6: Common Table Expressions (CTEs)",
        "blocks": [
          {
            "type": "story",
            "title": "The Complex Web",
            "text": "The queries are becoming monstrous. Nested subqueries make the ledger unreadable. The ancient monks used a technique to name their intermediate steps."
          },
          {
            "type": "problem",
            "text": "Complex queries with multiple subqueries are hard to read, maintain, and sometimes optimize."
          },
          {
            "type": "concept",
            "title": "CTEs (WITH clause)",
            "explanation": "A CTE provides a temporary result set that you can reference within another SELECT, INSERT, UPDATE, or DELETE statement.",
            "analogy": "Defining variables at the top of a math problem before solving the final equation.",
            "technical_explanation": "Introduced using the `WITH` keyword. Improves readability by breaking complex logic into manageable, named blocks.",
            "why_it_matters": "Massively improves SQL readability and allows for recursive queries.",
            "remember": "WITH CTE_Name AS (...)"
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "WITH EliteMerchants AS (\n  SELECT id FROM merchants WHERE status='elite'\n)\nSELECT * FROM EliteMerchants;"
          },
          {
            "type": "worked_example",
            "title": "Writing a CTE",
            "steps": [
              "1. Start with WITH cte_name AS (query).",
              "2. Follow immediately with a SELECT that uses cte_name."
            ]
          },
          {
            "type": "reflection",
            "question": "Are CTEs permanently stored in the database?"
          },
          {
            "type": "debugger",
            "title": "CTE Scope",
            "scenario": "You define a CTE and try to use it in two separate queries separated by a semicolon.",
            "options": [
              "It works fine",
              "It fails on the second query"
            ],
            "answer": "It fails on the second query",
            "explanation": "A CTE only exists for the duration of the single query statement immediately following it."
          },
          {
            "type": "sql_sandbox",
            "title": "Clean up with CTE",
            "context": "Use a CTE named `RichMerchants` to find merchants with `amount > 100`, then SELECT * from it.",
            "init_script": "CREATE TABLE t (id INT, amount INT); INSERT INTO t VALUES (1, 50), (2, 500);",
            "solution_query": "WITH RichMerchants AS (SELECT * FROM t WHERE amount > 100) SELECT * FROM RichMerchants;",
            "hint": "WITH RichMerchants AS (...) SELECT * FROM RichMerchants;",
            "explanation": "CTEs make your intermediate steps explicit and readable."
          }
        ]
      },
      {
        "title": "Module 7: UNION and Set Operations",
        "blocks": [
          {
            "type": "story",
            "title": "The Shadow Ledger",
            "text": "You find a second ledger, hidden beneath a floorboard! It has the same structure as the first. We must combine the rows of both ledgers into one massive list."
          },
          {
            "type": "problem",
            "text": "We need to vertically stack results from two different queries, not join them horizontally."
          },
          {
            "type": "concept",
            "title": "UNION",
            "explanation": "UNION combines the result sets of two or more SELECT statements into a single column set. It automatically removes duplicates.",
            "analogy": "Pouring two different bags of M&Ms into a single bowl.",
            "technical_explanation": "Both queries must return the same number of columns, with compatible data types in the same order. `UNION ALL` keeps duplicates.",
            "why_it_matters": "Essential for aggregating data spread across identical tables (e.g., archived vs active data).",
            "remember": "UNION stacks vertically, JOIN merges horizontally."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "Query 1: (A), (B)\nUNION\nQuery 2: (B), (C)\nResult: (A), (B), (C)"
          },
          {
            "type": "worked_example",
            "title": "Stacking Ledgers",
            "steps": [
              "1. SELECT col1 FROM table1",
              "2. UNION",
              "3. SELECT col1 FROM table2"
            ]
          },
          {
            "type": "reflection",
            "question": "Why is `UNION ALL` faster than `UNION`?"
          },
          {
            "type": "micro_challenge",
            "question": "What is required for a UNION to work?",
            "options": [
              "Tables must have a foreign key",
              "Queries must have the same number of columns",
              "Both tables must have the same name"
            ],
            "answer": "Queries must have the same number of columns",
            "explanation": "The columns must align perfectly for the stacking to work."
          },
          {
            "type": "sql_sandbox",
            "title": "Combine Ledgers",
            "context": "Combine the `id` columns from `ledger1` and `ledger2` using UNION ALL.",
            "init_script": "CREATE TABLE ledger1 (id INT); CREATE TABLE ledger2 (id INT); INSERT INTO ledger1 VALUES (1), (2); INSERT INTO ledger2 VALUES (2), (3);",
            "solution_query": "SELECT id FROM ledger1 UNION ALL SELECT id FROM ledger2;",
            "hint": "SELECT id FROM ledger1 UNION ALL ...",
            "explanation": "UNION ALL kept the duplicate '2'."
          }
        ]
      },
      {
        "title": "Module 8: Indexing and Final Conspiracy Challenge",
        "blocks": [
          {
            "type": "story",
            "title": "The Slow Reveal",
            "text": "We have 200,000 rows. Searching for the conspirator's ID (ID = 99999) takes too long. The Master demands instant results!"
          },
          {
            "type": "problem",
            "text": "Sequential scanning of a massive table is slow O(N). We need O(log N) lookup."
          },
          {
            "type": "concept",
            "title": "Indexes",
            "explanation": "An index is a data structure (usually a B-Tree) that improves the speed of data retrieval operations on a table at the cost of additional storage and slower writes.",
            "analogy": "The index at the back of a textbook. Instead of reading every page to find a topic, you look it up in the back and jump straight to the page.",
            "technical_explanation": "Creates a sorted auxiliary structure containing the indexed column and a pointer to the physical row.",
            "why_it_matters": "The primary tool for database performance optimization.",
            "remember": "Fast reads, slow writes."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "Table Scan: Check row 1, row 2... row 200,000.\nIndex Seek: Root -> Branch -> Leaf (3 steps)."
          },
          {
            "type": "worked_example",
            "title": "Creating an Index",
            "steps": [
              "1. CREATE INDEX idx_merchant_id ON transactions (merchant_id);"
            ]
          },
          {
            "type": "reflection",
            "question": "Why shouldn't you put an index on every single column?"
          },
          {
            "type": "debugger",
            "title": "Index Choice",
            "scenario": "A query filters by `last_name` and `first_name`. You create an index on `first_name`.",
            "options": [
              "Perfect",
              "Index should be on last_name, first_name"
            ],
            "answer": "Index should be on last_name, first_name",
            "explanation": "Composite indexes work left-to-right. If you search by last_name primarily, it must be the leading column in the index."
          },
          {
            "type": "sql_sandbox",
            "title": "Final Challenge: Uncover the Conspiracy",
            "context": "Create an index on `amount` in the `ledger` table, then select the ID where amount is 9999.",
            "init_script": "CREATE TABLE ledger (id INT, amount INT); INSERT INTO ledger VALUES (1, 100), (2, 9999);",
            "solution_query": "CREATE INDEX idx_amount ON ledger(amount);\nSELECT id FROM ledger WHERE amount = 9999;",
            "hint": "CREATE INDEX name ON table(column); then run your SELECT.",
            "explanation": "The index allowed the database to instantly find the conspirator's transaction."
          }
        ]
      }
    ]
  },
  "10": {
    "format": "episodic",
    "episodes": [
      {
        "title": "Module 1: The Divergent Rulebooks",
        "blocks": [
          {
            "type": "story",
            "title": "Sector Disarray",
            "text": "In the sprawling mechanical metropolis of GearCity, twelve distinct robot sectors operate in unison\u2014or at least they are supposed to. Recently, operations have ground to a halt. When central command asks for the current rulebook version, each sector returns a different answer."
          },
          {
            "type": "problem",
            "text": "How do distributed nodes agree on a single source of truth when any node could be disconnected or crash?"
          },
          {
            "type": "concept",
            "title": "The Core Issue of Distributed Systems",
            "explanation": "In a single database system, there is only one place to check for the truth. In a distributed system, data is copied across multiple nodes to ensure reliability. However, this introduces the problem of synchronization.",
            "analogy": "Imagine twelve generals surrounding a city. They must attack at the exact same time, but they can only communicate via messengers who might be captured. If they don't agree on the time, the attack fails.",
            "technical_explanation": "This is known as the Consensus Problem. We need algorithms (like Paxos or Raft) to guarantee that all non-faulty nodes agree on the same value, even in the presence of network partitions or node crashes.",
            "why_it_matters": "Without consensus, distributed databases would serve contradictory data, leading to catastrophic failures like double-spending in financial systems.",
            "remember": "Consensus means agreeing on a single state across multiple independent entities."
          }
        ]
      },
      {
        "title": "Module 2: Electing a Leader",
        "blocks": [
          {
            "type": "story",
            "title": "The Need for a Commander",
            "text": "The robots realize that arguing simultaneously solves nothing. They decide that one robot must be in charge of deciding the rulebook version, while the others listen."
          },
          {
            "type": "concept",
            "title": "Leader-Based Consensus",
            "explanation": "Many consensus algorithms use a Leader-Follower model. One node is elected as the leader, and all changes must go through it.",
            "analogy": "A classroom without a teacher is chaos. When a teacher (leader) speaks, students (followers) take notes. If the teacher leaves, a substitute must be appointed.",
            "technical_explanation": "In protocols like Raft, time is divided into terms. Each term begins with an election. If a node wins the election, it acts as the leader. Followers only accept updates from the valid leader of the current term.",
            "why_it_matters": "Having a single leader simplifies the problem of agreement\u2014there is only one source of new entries.",
            "remember": "Only one leader can exist per term."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "  [Follower] <--- (Heartbeat) --- [Leader]\n     ^                              |\n     |                              v\n     +------- (Heartbeat) --------> [Follower]"
          },
          {
            "type": "worked_example",
            "title": "A Simple Election",
            "steps": [
              "1. Node A's heartbeat timer expires because it hasn't heard from a leader.",
              "2. Node A transitions to 'Candidate' state and requests votes.",
              "3. Nodes B and C receive the request and grant their votes.",
              "4. Node A receives a majority of votes and becomes the Leader.",
              "5. Node A sends out heartbeats to suppress further elections."
            ]
          }
        ]
      },
      {
        "title": "Module 3: Understanding Quorum",
        "blocks": [
          {
            "type": "concept",
            "title": "What is a Quorum?",
            "explanation": "A quorum is the minimum number of nodes that must agree for an operation to be considered successful.",
            "analogy": "In a board meeting of 5 directors, you need at least 3 present (a majority) to pass a binding resolution.",
            "technical_explanation": "Usually, a quorum requires strict majority: (N/2) + 1. For a 5-node cluster, the quorum is 3. This ensures that any two quorums must overlap by at least one node, preventing split-brain scenarios.",
            "why_it_matters": "Quorum allows a system to make progress even if a minority of nodes are down or disconnected.",
            "remember": "Quorum = (N/2) + 1. It guarantees overlap."
          },
          {
            "type": "micro_challenge",
            "question": "If you have a cluster of 7 nodes, what is the minimum quorum size required to ensure consistency?",
            "options": [
              "3",
              "4",
              "5"
            ],
            "answer": "4",
            "explanation": "The formula is Floor(7/2) + 1 = 3 + 1 = 4. Four nodes form a strict majority."
          }
        ]
      },
      {
        "title": "Module 4: Failover and Fault Tolerance",
        "blocks": [
          {
            "type": "story",
            "title": "The Leader Crashes",
            "text": "Disaster! Sector 1, the newly elected leader, suffers a sudden power failure. The other sectors wait in silence."
          },
          {
            "type": "concept",
            "title": "Failover Mechanisms",
            "explanation": "When a leader crashes, the system must automatically detect the failure and elect a new leader. This process is called Failover.",
            "analogy": "If the captain of a ship falls overboard, the first mate immediately takes command to keep the ship on course.",
            "technical_explanation": "Nodes rely on timeouts. If a follower doesn't receive a heartbeat from the leader within a randomized timeout window, it assumes the leader is dead and starts an election.",
            "why_it_matters": "Automatic failover provides High Availability (HA). The system heals itself without human intervention.",
            "remember": "Timeouts are the heartbeat of distributed fault tolerance."
          },
          {
            "type": "debugger",
            "title": "Debugging a Split-Brain",
            "scenario": "A network partition splits a 5-node cluster into two groups: [A, B] and [C, D, E]. Node A was the leader.",
            "options": [
              "[C, D, E] will elect a new leader; [A, B] will continue operating independently.",
              "[C, D, E] will elect a new leader; [A, B] will halt operations because they lack a quorum.",
              "The entire cluster will crash."
            ],
            "answer": "[C, D, E] will elect a new leader; [A, B] will halt operations because they lack a quorum.",
            "explanation": "[C,D,E] has 3 nodes (a quorum) and can elect a leader. [A,B] only has 2 nodes (less than quorum) and cannot commit new entries, preventing data divergence."
          }
        ]
      },
      {
        "title": "Module 5: Modeling State in a Database",
        "blocks": [
          {
            "type": "concept",
            "title": "The Replicated State Machine",
            "explanation": "Consensus algorithms often manage a Replicated State Machine. We log every command, and every node executes the log in the exact same order.",
            "analogy": "A shared bank ledger. If every branch records deposits and withdrawals in the exact same sequence, every branch will calculate the exact same final balance.",
            "technical_explanation": "A log entry is first 'appended' to the leader's log. The leader replicates it to followers. Once a quorum of followers acknowledges the append, the entry is 'committed'.",
            "why_it_matters": "The log ensures order. Even if a node reboots, it can replay the log to reconstruct the correct state.",
            "remember": "Log first, commit second, execute third."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "Log Index: 1 | 2 | 3\nCommand: SET X=1 | ADD Y=2 | DEL X\nCommitted: [YES] | [YES] | [NO]"
          }
        ]
      },
      {
        "title": "Module 6: SQL Sandbox - Building a Node Registry",
        "blocks": [
          {
            "type": "story",
            "title": "Tracking the Nodes",
            "text": "Before we simulate a leader election, we need to track the status of all twelve sectors in our central metadata database."
          },
          {
            "type": "sql_sandbox",
            "title": "Initialize the Cluster",
            "context": "Create a table to track nodes and insert the first three nodes. We need a way to mark one as the leader.",
            "init_script": "CREATE TABLE nodes (id INT PRIMARY KEY, name TEXT, is_leader BOOLEAN, status TEXT);",
            "solution_query": "INSERT INTO nodes (id, name, is_leader, status) VALUES (1, 'Sector 1', true, 'ONLINE'), (2, 'Sector 2', false, 'ONLINE'), (3, 'Sector 3', false, 'ONLINE');",
            "hint": "Use standard INSERT INTO syntax.",
            "explanation": "This simple table allows us to query which node is currently believed to be the leader and whether nodes are online."
          }
        ]
      },
      {
        "title": "Module 7: Simulating the Failover in SQL",
        "blocks": [
          {
            "type": "story",
            "title": "The SQL Failover",
            "text": "Sector 1 just went offline. We must update the database to reflect the failure and promote Sector 2 to leader."
          },
          {
            "type": "sql_sandbox",
            "title": "Promote the Follower",
            "context": "Sector 1 crashed. Write a transaction (using multiple statements if supported, or just update statements) to mark Sector 1 as 'OFFLINE' and 'is_leader = false', and make Sector 2 the new leader.",
            "init_script": "CREATE TABLE nodes (id INT PRIMARY KEY, name TEXT, is_leader BOOLEAN, status TEXT); INSERT INTO nodes VALUES (1, 'Sector 1', true, 'ONLINE'), (2, 'Sector 2', false, 'ONLINE'), (3, 'Sector 3', false, 'ONLINE');",
            "solution_query": "UPDATE nodes SET is_leader = false, status = 'OFFLINE' WHERE id = 1; UPDATE nodes SET is_leader = true WHERE id = 2;",
            "hint": "You'll need two UPDATE statements.",
            "explanation": "In a real distributed system, this state change is determined by the consensus algorithm itself. Here, we are modeling the outcome in a metadata store."
          }
        ]
      },
      {
        "title": "Module 8: Final Investigation - The Consensus Audit",
        "blocks": [
          {
            "type": "story",
            "title": "Auditing the Logs",
            "text": "The sectors are back in sync. Now command wants an audit. Which log entries were successfully committed by a quorum of at least 3 nodes?"
          },
          {
            "type": "sql_sandbox",
            "title": "Identify Committed Entries",
            "context": "You have a `logs` table and a `log_acknowledgments` table. Find the `log_id`s that have 3 or more acknowledgments.",
            "init_script": "CREATE TABLE logs (log_id INT, command TEXT); CREATE TABLE log_acknowledgments (log_id INT, node_id INT); INSERT INTO logs VALUES (101, 'Update Rule 1'), (102, 'Update Rule 2'); INSERT INTO log_acknowledgments VALUES (101, 1), (101, 2), (101, 3), (102, 1), (102, 2);",
            "solution_query": "SELECT log_id FROM log_acknowledgments GROUP BY log_id HAVING COUNT(node_id) >= 3;",
            "hint": "Use GROUP BY and HAVING COUNT(...).",
            "explanation": "Log 101 has 3 acks (quorum reached), so it is committed. Log 102 only has 2 acks, so it is still pending."
          }
        ]
      }
    ]
  },
  "7": {
    "format": "episodic",
    "episodes": [
      {
        "title": "Module 1: The AI's Contradiction",
        "blocks": [
          {
            "type": "story",
            "title": "The Dueling Directives",
            "text": "Two department heads storm into your office. 'The central AI told me to halt production because we are over budget!' yells one. 'It told ME to double production because we have surplus!' yells the other. Both present reports generated at exactly 14:00:00 by the same AI, from the same central database."
          },
          {
            "type": "problem",
            "text": "How can the exact same query, run at the exact same time, produce contradictory results from the same database?"
          },
          {
            "type": "concept",
            "title": "Database Isolation",
            "explanation": "When multiple users or processes access a database simultaneously, they might see data in different states if transactions are actively modifying it.",
            "analogy": "Imagine two people reading a whiteboard while a third person is erasing and rewriting parts of it. Depending on when they blink, they see different messages.",
            "technical_explanation": "Isolation is the 'I' in ACID. It defines how/when the changes made by one operation become visible to other concurrent operations.",
            "why_it_matters": "Without isolation, concurrent transactions interfere with each other, leading to dirty reads, non-repeatable reads, or phantom reads.",
            "remember": "Perfect isolation makes concurrent transactions appear as if they executed sequentially."
          }
        ]
      },
      {
        "title": "Module 2: The Dirty Read",
        "blocks": [
          {
            "type": "concept",
            "title": "Read Uncommitted and Dirty Reads",
            "explanation": "The lowest level of isolation is Read Uncommitted. It allows a transaction to read data that has been modified by another transaction, but not yet committed.",
            "analogy": "Reading someone's draft email before they decide to send it or delete it.",
            "technical_explanation": "A Dirty Read occurs when Transaction A reads data modified by Transaction B, but Transaction B then rolls back. Transaction A acted on data that 'never existed'.",
            "why_it_matters": "Dirty reads lead to decisions based on false or rolled-back information.",
            "remember": "Never trust uncommitted data for critical operations."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "Time | Transaction 1 (T1)       | Transaction 2 (T2)\n----------------------------------------------------\n 1   | BEGIN                    |\n 2   | UPDATE budget=500        |\n 3   |                          | BEGIN\n 4   |                          | SELECT budget -> 500 (Dirty Read!)\n 5   | ROLLBACK (budget=100)    |\n 6   |                          | -- T2 thinks budget is 500, but it's 100!"
          },
          {
            "type": "micro_challenge",
            "question": "If an AI decision system operates under READ UNCOMMITTED isolation, what might happen?",
            "options": [
              "It can never access data.",
              "It might make decisions based on transactions that are later aborted/rolled back.",
              "It will perfectly wait for all transactions to finish."
            ],
            "answer": "It might make decisions based on transactions that are later aborted/rolled back.",
            "explanation": "Read Uncommitted allows reading data that is in the middle of being modified and might be rolled back."
          }
        ]
      },
      {
        "title": "Module 3: Non-Repeatable Reads",
        "blocks": [
          {
            "type": "concept",
            "title": "Read Committed and Non-Repeatable Reads",
            "explanation": "To fix dirty reads, databases use Read Committed. You only see data that has been fully committed. But a new problem arises: if you read the same row twice in your transaction, someone else might commit a change in between.",
            "analogy": "Checking a bank account balance, seeing $100, then trying to withdraw $100 but failing because a recurring bill cleared right after your first check.",
            "technical_explanation": "A Non-Repeatable Read occurs when T1 reads a row, T2 updates that row and commits, and T1 reads the row again and gets a different value.",
            "why_it_matters": "Calculations that rely on multiple reads of the same data within a transaction can become inconsistent.",
            "remember": "Read Committed only guarantees the data was committed AT THE MOMENT you read it, not that it will stay that way."
          }
        ]
      },
      {
        "title": "Module 4: Multi-Version Concurrency Control (MVCC)",
        "blocks": [
          {
            "type": "concept",
            "title": "The MVCC Solution",
            "explanation": "Instead of locking rows and making everyone wait, modern databases keep multiple versions of the data.",
            "analogy": "Using a version control system like Git. When you read, you look at a specific commit (snapshot), even if others are making new commits.",
            "technical_explanation": "MVCC (Multi-Version Concurrency Control) assigns each transaction an ID. When a row is updated, a new version is created. Transactions only 'see' versions committed before their start time.",
            "why_it_matters": "MVCC allows readers to read without blocking writers, and writers to write without blocking readers.",
            "remember": "Readers don't block writers, writers don't block readers."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "Row: Budget = 100\n[TxID: 10] UPDATE budget=200\n\nDatabase stores:\nVersion A (Created Tx 1): Budget=100 (Valid until Tx 10)\nVersion B (Created Tx 10): Budget=200 (Valid for Tx > 10)"
          },
          {
            "type": "debugger",
            "title": "MVCC Visibility",
            "scenario": "Transaction 15 starts. Transaction 12 is currently running and hasn't committed. Transaction 10 committed yesterday. Which version of the data does Tx 15 see?",
            "options": [
              "The version created by Tx 12",
              "The version created by Tx 10",
              "A mix of both"
            ],
            "answer": "The version created by Tx 10",
            "explanation": "Tx 15 can only see data committed before it started. Tx 12 hasn't committed, so its changes are invisible to Tx 15."
          }
        ]
      },
      {
        "title": "Module 5: Snapshot Isolation",
        "blocks": [
          {
            "type": "concept",
            "title": "Snapshot Isolation",
            "explanation": "Building on MVCC, Snapshot Isolation guarantees that a transaction sees a consistent snapshot of the database as it existed at the start of the transaction.",
            "analogy": "Taking a photograph of a busy street. The photograph doesn't change, even as cars continue to move in real life.",
            "technical_explanation": "When a transaction starts under Snapshot Isolation (often implemented as REPEATABLE READ in some RDBMS), it gets a 'snapshot' ID. It ignores all changes made by transactions that commit after its snapshot ID.",
            "why_it_matters": "It prevents both Dirty Reads and Non-Repeatable Reads, providing a highly consistent view for complex reporting.",
            "remember": "Your transaction exists in a time capsule."
          }
        ]
      },
      {
        "title": "Module 6: Temporal Data and Auditing",
        "blocks": [
          {
            "type": "concept",
            "title": "Time-Travel Queries",
            "explanation": "If the database keeps old versions of rows (like in MVCC), what if we expose that to the user? This is temporal data.",
            "analogy": "Looking at the 'revision history' of a Wikipedia page to see what it looked like exactly on Jan 1st, 2020.",
            "technical_explanation": "System-versioned temporal tables automatically keep a history of all changes, storing valid_from and valid_to timestamps. You can query the table `AS OF` a specific timestamp.",
            "why_it_matters": "Essential for auditing, compliance, and recovering from accidental deletions.",
            "remember": "Temporal tables remember everything."
          }
        ]
      },
      {
        "title": "Module 7: Designing an Audit Trail",
        "blocks": [
          {
            "type": "worked_example",
            "title": "Creating an Audit Table via Triggers",
            "steps": [
              "1. Create the main table (e.g., accounts)",
              "2. Create the audit table (e.g., accounts_audit) with identical columns plus timestamp and operation type.",
              "3. Write a database TRIGGER that runs AFTER UPDATE or AFTER DELETE.",
              "4. Inside the trigger, insert the OLD row values into the audit table."
            ]
          },
          {
            "type": "sql_sandbox",
            "title": "Implementing the Audit",
            "context": "We need to track every change to the budget. Create an audit trail.",
            "init_script": "CREATE TABLE budget (id INT, amount INT); CREATE TABLE budget_audit (id INT, amount INT, changed_at DATETIME);",
            "solution_query": "CREATE TRIGGER audit_budget AFTER UPDATE ON budget FOR EACH ROW BEGIN INSERT INTO budget_audit (id, amount, changed_at) VALUES (OLD.id, OLD.amount, CURRENT_TIMESTAMP); END;",
            "hint": "Use CREATE TRIGGER and INSERT INTO the audit table using the OLD values.",
            "explanation": "Triggers allow you to automatically capture historical states before modifications occur."
          }
        ]
      },
      {
        "title": "Module 8: Resolving the AI's Contradiction",
        "blocks": [
          {
            "type": "story",
            "title": "The Final Verdict",
            "text": "You realize the central AI was using READ COMMITTED, and generating the report took 5 minutes. Halfway through, a massive budget transfer was committed. The first department's data was read before the transfer, the second's after. The AI saw an inconsistent state."
          },
          {
            "type": "problem",
            "text": "Fix the AI's view so it sees a perfectly consistent snapshot from exactly 14:00:00."
          },
          {
            "type": "sql_sandbox",
            "title": "Setting Isolation Level",
            "context": "Change the transaction isolation level to ensure a consistent snapshot for the entire transaction in SQLite.",
            "init_script": "PRAGMA read_uncommitted = true;",
            "solution_query": "PRAGMA read_uncommitted = false; BEGIN IMMEDIATE;",
            "hint": "To get a snapshot in SQLite, you disable read uncommitted and start a transaction.",
            "explanation": "Ensuring the correct isolation level (like Serializable or Snapshot Isolation) prevents the anomalies that cause inconsistent reports."
          }
        ]
      }
    ]
  },
  "0": {
    "format": "episodic",
    "episodes": [
      {
        "title": "Module 1: What Is Data?",
        "blocks": [
          {
            "type": "story",
            "title": "The Dust Settles",
            "text": "You push open the heavy blast doors of Sector 4. Inside, the pre-collapse records office is exactly as they left it. Mountains of paper folders stretch to the ceiling. The Payroll department and the Housing department kept their own separate records. Nothing is digitized."
          },
          {
            "type": "concept",
            "title": "Data vs Information",
            "explanation": "Data consists of raw, unorganized facts. Information is data that has been processed, organized, and given context to make it useful.",
            "analogy": "A list of numbers like '42, 17, 8' is just raw data. But if you label them 'Temperatures this week in Celsius', they become information you can use to decide whether to wear a coat.",
            "why_it_matters": "Computers only store raw data. It is the structure we impose on it that turns it into actionable information."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "[ RAW DATA ] -> 1984, Smith, 45000\n\n[ INFORMATION ] -> Year Hired: 1984 | Name: Smith | Salary: $45000"
          },
          {
            "type": "reflection",
            "question": "If you found a drawer labeled 'Project X' filled with random dates and names, what is missing for it to be considered useful information?"
          }
        ]
      },
      {
        "title": "Module 2: The File-Based Nightmare",
        "blocks": [
          {
            "type": "problem",
            "text": "You find a folder for 'John Smith' in the Payroll cabinet showing his address as 'Sector A'. You find another folder for 'John Smith' in the Housing cabinet showing his address as 'Sector B'. Which one is correct?"
          },
          {
            "type": "concept",
            "title": "File-Based Systems & Data Redundancy",
            "explanation": "Before databases, applications stored data in separate flat files. This led to Data Redundancy\u2014storing the exact same fact in multiple places.",
            "analogy": "Imagine every teacher in a school keeping their own separate list of student phone numbers. If a student moves, every single teacher must update their personal list independently.",
            "technical_explanation": "Redundancy inevitably leads to Update Anomalies (forgetting to update one copy, resulting in inconsistent data) and Wasted Storage space."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "PAYROLL SYSTEM\n| Name       | Address  | Salary |\n|------------|----------|--------|\n| John Smith | Sector A | 50000  |\n\nHOUSING SYSTEM\n| Name       | Address  | Rent   |\n|------------|----------|--------|\n| John Smith | Sector B | 1200   |\n\n(INCONSISTENCY DETECTED)"
          },
          {
            "type": "data_explorer",
            "title": "The Update Anomaly",
            "context": "Simulate what happens when you only update the Housing file. Observe how the Payroll file remains dangerously out of date.",
            "scenario": "update_anomaly"
          }
        ]
      },
      {
        "title": "Module 3: Why Databases Were Invented",
        "blocks": [
          {
            "type": "story",
            "title": "A Better Way",
            "text": "The archivists realized that having 50 different copies of the same citizen's address was causing chaos. They needed a single source of truth."
          },
          {
            "type": "concept",
            "title": "The Solution: A Centralized Database",
            "explanation": "A Database centralizes data logically so it can be shared by multiple applications without redundancy.",
            "analogy": "Instead of every teacher keeping a phonebook, the school puts one master phonebook in the front office. Teachers just look it up there.",
            "technical_explanation": "By centralizing data, we solve the redundancy problem (only one place to update), enable concurrent access (multiple people can read it), and enforce security (one door to guard)."
          },
          {
            "type": "micro_challenge",
            "question": "If two archivists try to write a new address on the same physical paper file at the exact same time, their pens will clash. In a digital system, this is called a Concurrency Issue. How does a centralized database approach this?",
            "options": [
              "It deletes the file to prevent conflicts.",
              "It uses transaction locks to ensure one person writes at a time.",
              "It forces users to keep separate copies of the file again."
            ],
            "answer": "It uses transaction locks to ensure one person writes at a time.",
            "explanation": "Centralization creates a chokepoint where a system can safely organize who gets to read and write at what exact millisecond."
          }
        ]
      },
      {
        "title": "Module 4: What is a DBMS?",
        "blocks": [
          {
            "type": "concept",
            "title": "Database vs DBMS",
            "explanation": "The 'Database' is just the collection of data itself. The 'Database Management System' (DBMS) is the software engine that controls access to it.",
            "analogy": "The Database is the vault of gold. The DBMS is the heavily armed bank teller who verifies your ID, opens the vault, and ensures you don't take someone else's gold.",
            "why_it_matters": "When people say 'I use MySQL or PostgreSQL', they are talking about the DBMS software, not the data itself."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "[ USER / APP ] <---> [ DBMS (Software) ] <---> [ DATABASE (Storage) ]"
          },
          {
            "type": "debugger",
            "title": "Diagnose the Architecture",
            "scenario": "A developer wrote a script that bypasses the DBMS software and directly modifies the raw binary data files on the hard drive. Why is this a catastrophic idea?",
            "options": [
              "It is perfectly fine and faster.",
              "It bypasses all security, concurrency, and integrity checks enforced by the DBMS.",
              "The hard drive will explode."
            ],
            "answer": "It bypasses all security, concurrency, and integrity checks enforced by the DBMS.",
            "explanation": "The DBMS is the sole guardian of data integrity. Bypassing it guarantees corruption."
          }
        ]
      },
      {
        "title": "Module 5: Schema vs Instance",
        "blocks": [
          {
            "type": "story",
            "title": "The Master Blueprint",
            "text": "You find a poster on the wall detailing exactly what fields are required for a new employee. 'ID, First Name, Last Name, Department'. Underneath is a massive stack of actual filled-out employee forms."
          },
          {
            "type": "concept",
            "title": "Schema vs Instance",
            "explanation": "The Schema is the blueprint or structure of the database (e.g., what tables and columns exist). The Instance is the actual data stored in the database at a specific moment in time.",
            "analogy": "The Schema is the blank cookie cutter. The Instance is the actual batch of cookies sitting on the tray right now."
          },
          {
            "type": "micro_challenge",
            "question": "If you add a new column called 'Email_Address' to a table, what have you modified?",
            "options": [
              "The Schema",
              "The Instance",
              "Neither"
            ],
            "answer": "The Schema",
            "explanation": "You altered the blueprint. The instance will also be affected (as existing rows will now have an empty email space), but the action was a Schema modification."
          }
        ]
      },
      {
        "title": "Module 6: Who Uses a Database?",
        "blocks": [
          {
            "type": "concept",
            "title": "The Roles",
            "explanation": "Different people interact with the DBMS in completely different ways.",
            "technical_explanation": "1. Database Administrator (DBA): Designs schema, manages security, tunes performance.\n2. Application Developer: Writes code that queries the DBMS.\n3. End User: Clicks buttons on a UI that under-the-hood triggers the developer's code."
          },
          {
            "type": "micro_challenge",
            "question": "Who is responsible for ensuring that the hard drives have enough space and the system is backed up nightly?",
            "options": [
              "The Application Developer",
              "The End User",
              "The Database Administrator (DBA)"
            ],
            "answer": "The Database Administrator (DBA)",
            "explanation": "The DBA is responsible for the health, performance, and architecture of the database system itself."
          }
        ]
      },
      {
        "title": "Module 7: Three-Schema Architecture",
        "blocks": [
          {
            "type": "problem",
            "text": "The Housing Department only wants to see addresses. The Payroll Department only wants to see salaries. But you only want to store the data once. How do you satisfy both without duplicating data?"
          },
          {
            "type": "concept",
            "title": "The ANSI/SPARC Architecture",
            "explanation": "Databases use a 3-level architecture to separate how data is stored from how users see it.",
            "technical_explanation": "1. Internal Level: How the data is physically stored on disk (bytes, B-trees).\n2. Conceptual Level: The logical master blueprint (tables, relations).\n3. External Level: The specific 'views' tailored for individual users."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "EXTERNAL LEVEL (Views)\n[ Payroll View ]    [ Housing View ]\n        \\                 /\n         \\               /\n       CONCEPTUAL LEVEL (Tables)\n        [ Employee Table ]\n                 |\n        INTERNAL LEVEL (Storage)\n      [ Disk Blocks / B-Trees ]"
          }
        ]
      },
      {
        "title": "Module 8: Data Independence",
        "blocks": [
          {
            "type": "concept",
            "title": "The Power of Abstraction",
            "explanation": "Data Independence is the ability to change one layer of the architecture without breaking the layer above it.",
            "analogy": "Physical Data Independence is like upgrading your car's engine (Internal Level) without having to replace the steering wheel (Conceptual Level). Logical Data Independence is like adding a sunroof (Conceptual Level) without affecting the passengers who don't use it (External Level)."
          },
          {
            "type": "debugger",
            "title": "Diagnose the Failure",
            "scenario": "A DBA moves a table from a slow HDD to a fast SSD. Suddenly, all application code crashes because it can't find the data. What DBMS principle has failed here?",
            "options": [
              "Logical Data Independence",
              "Physical Data Independence",
              "Schema Instantiation"
            ],
            "answer": "Physical Data Independence",
            "explanation": "Physical Data Independence guarantees that changing the underlying storage mechanism (Internal level) should NOT break the logical structure (Conceptual level) or the apps that rely on it."
          }
        ]
      },
      {
        "title": "Module 9: Basic SQL",
        "blocks": [
          {
            "type": "story",
            "title": "The Terminal",
            "text": "You find a working terminal connected to the central archive. It asks for a query. You realize you need a standard language to instruct the DBMS."
          },
          {
            "type": "concept",
            "title": "Structured Query Language (SQL)",
            "explanation": "SQL is a declarative language used to manage relational databases. 'Declarative' means you describe WHAT you want, not exactly HOW to get it.",
            "analogy": "Imperative is telling a chef: 'Take bread, put cheese, toast for 2 mins.' Declarative is telling a waiter: 'I want a grilled cheese sandwich.' SQL is declarative. The DBMS query optimizer figures out the recipe."
          },
          {
            "type": "sql_sandbox",
            "title": "Your First Query",
            "context": "The archive has a table named 'archive_logs'. Let's ask the DBMS to give us everything inside it.",
            "init_script": "CREATE TABLE archive_logs (id INT, entry TEXT); INSERT INTO archive_logs VALUES (1, 'System initialized'), (2, 'Error in sector 4');",
            "solution_query": "SELECT * FROM archive_logs;",
            "hint": "Use SELECT * FROM archive_logs;",
            "explanation": "The SELECT * statement asks the DBMS to retrieve every column for every row in the specified table."
          }
        ]
      },
      {
        "title": "Module 10: Final Investigation",
        "blocks": [
          {
            "type": "story",
            "title": "The Single Source of Truth",
            "text": "The archivists have finally agreed to use the central DBMS. They want you to prove that it can securely hold John Smith's singular address without the need for redundant files."
          },
          {
            "type": "sql_sandbox",
            "title": "Querying the Master Record",
            "context": "The central table is called 'citizens'. Retrieve only the 'name' and 'address' of everyone in the system. Notice how there is only one definitive address for John Smith now.",
            "init_script": "CREATE TABLE citizens (id INT, name TEXT, address TEXT, salary INT, rent INT); INSERT INTO citizens VALUES (1, 'John Smith', 'Sector A', 50000, 1200), (2, 'Jane Doe', 'Sector C', 60000, 1500);",
            "solution_query": "SELECT name, address FROM citizens;",
            "hint": "Use SELECT followed by name, address FROM citizens;",
            "explanation": "By projecting just the name and address from a single unified table, we demonstrate the Conceptual layer acting as a single source of truth."
          }
        ]
      }
    ]
  },
  "2": {
    "format": "episodic",
    "episodes": [
      {
        "title": "Module 1: The Impossible Blueprint",
        "blocks": [
          {
            "type": "story",
            "title": "City of Paradoxes",
            "text": "A city blueprint contains buildings that cannot legally exist under its own rules. Doors that lead nowhere, addresses assigned to multiple properties. You must audit the design."
          },
          {
            "type": "problem",
            "text": "Model the city's rules using Entity-Relationship (ER) concepts to find the structural flaws."
          },
          {
            "type": "concept",
            "title": "Introduction to ER Modeling",
            "explanation": "Entity-Relationship modeling is a conceptual way to design databases before writing SQL.",
            "analogy": "It's the architectural blueprint of the database. You draw it before you pour the concrete.",
            "technical_explanation": "Entities represent objects; Attributes are properties; Relationships define interactions.",
            "why_it_matters": "Catching logical errors in the design phase is infinitely cheaper than fixing a live database.",
            "remember": "Design first, code second."
          }
        ]
      },
      {
        "title": "Module 2: Entities and Attributes",
        "blocks": [
          {
            "type": "concept",
            "title": "Defining Entities",
            "explanation": "Entities are the nouns of your database.",
            "analogy": "In a city, 'Building' and 'Citizen' are entities. 'Tall' is an attribute.",
            "technical_explanation": "Entities become tables. Attributes become columns. Composite attributes can be broken down.",
            "why_it_matters": "Properly defining entities ensures you capture all necessary business requirements.",
            "remember": "Nouns = Entities, Adjectives = Attributes."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "[ Building ]\n - Address (Key)\n - Floors\n - YearBuilt"
          },
          {
            "type": "micro_challenge",
            "question": "Which of the following should be an Entity rather than an Attribute?",
            "options": [
              "Color",
              "Employee",
              "Age"
            ],
            "answer": "Employee",
            "explanation": "An Employee is an object with its own properties, making it an Entity."
          }
        ]
      },
      {
        "title": "Module 3: Relationships and Cardinality",
        "blocks": [
          {
            "type": "concept",
            "title": "Cardinality Limits",
            "explanation": "Cardinality defines how many instances of one entity can relate to instances of another.",
            "analogy": "A citizen can own multiple cars (1-to-Many), but a passport belongs to exactly one citizen (1-to-1).",
            "technical_explanation": "Common cardinalities are 1:1, 1:N, and M:N. Minimum cardinality defines mandatory vs optional participation.",
            "why_it_matters": "It dictates how foreign keys are placed and whether intermediary tables are needed.",
            "remember": "M:N requires a junction table."
          }
        ]
      },
      {
        "title": "Module 4: Constraints of Reality",
        "blocks": [
          {
            "type": "concept",
            "title": "Domain Constraints",
            "explanation": "Constraints enforce business logic at the database level.",
            "analogy": "A building cannot have a negative number of floors.",
            "technical_explanation": "CHECK constraints allow arbitrary boolean expressions to validate row data on insert/update.",
            "why_it_matters": "Prevents the application layer from inserting logically impossible states.",
            "remember": "Push data integrity rules to the database."
          },
          {
            "type": "sql_sandbox",
            "title": "Enforce Physics",
            "context": "Create a `buildings` table where `floors` must be greater than 0.",
            "init_script": "",
            "solution_query": "CREATE TABLE buildings (id INT PRIMARY KEY, floors INT CHECK (floors > 0));",
            "hint": "Use CHECK (floors > 0)",
            "explanation": "Now the database mathematically prohibits impossible buildings."
          }
        ]
      },
      {
        "title": "Module 5: Generalization",
        "blocks": [
          {
            "type": "concept",
            "title": "Superclasses and Subclasses",
            "explanation": "Entities can have hierarchies, similar to object-oriented programming.",
            "analogy": "A 'Vehicle' is a superclass. 'Car' and 'Bicycle' are subclasses that inherit properties.",
            "technical_explanation": "Generalization extracts shared attributes into a super-entity. Sub-entities hold specific attributes.",
            "why_it_matters": "Reduces NULL values and structures data logically.",
            "remember": "Is-A relationships denote specialization."
          },
          {
            "type": "debugger",
            "title": "The Overloaded Table",
            "scenario": "A table has 50 columns, but 40 are NULL for any given row because it stores both Residential and Commercial buildings.",
            "options": [
              "Needs an index",
              "Needs generalization",
              "Needs more RAM"
            ],
            "answer": "Needs generalization",
            "explanation": "Splitting the table based on type solves the sparse data problem."
          }
        ]
      },
      {
        "title": "Module 6: Translating ER to Tables",
        "blocks": [
          {
            "type": "concept",
            "title": "Logical Design",
            "explanation": "Translating an ER diagram into a relational schema.",
            "analogy": "Turning the blueprint into a step-by-step construction manual.",
            "technical_explanation": "Strong entities become tables. M:N relationships become their own tables with composite keys.",
            "why_it_matters": "This is the bridge between conceptual design and physical implementation.",
            "remember": "Every relationship must be represented as either a foreign key or a new table."
          },
          {
            "type": "worked_example",
            "title": "Resolving M:N",
            "steps": [
              "Identify M:N between Citizens and Properties.",
              "Create table citizen_property.",
              "Add citizen_id and property_id as foreign keys.",
              "Make the combination of both the Primary Key."
            ]
          }
        ]
      },
      {
        "title": "Module 7: Relational Algebra Foundations",
        "blocks": [
          {
            "type": "concept",
            "title": "The Math Behind SQL",
            "explanation": "Relational algebra is the mathematical foundation of SQL queries.",
            "analogy": "It's the physics that makes the engineering (SQL) work.",
            "technical_explanation": "Operators like Sigma (Selection), Pi (Projection), and Join form the basis of query execution plans.",
            "why_it_matters": "Understanding it helps you write more efficient queries by visualizing how the database engine processes them.",
            "remember": "SQL is just a syntax for relational algebra."
          },
          {
            "type": "reflection",
            "question": "Why does the database engine perform selection before a join when optimizing?"
          }
        ]
      },
      {
        "title": "Module 8: Final Blueprint Audit",
        "blocks": [
          {
            "type": "sql_sandbox",
            "title": "Fix the Blueprint",
            "context": "Create a robust schema for a building that has a required address, and floors strictly greater than zero.",
            "init_script": "",
            "solution_query": "CREATE TABLE buildings (id INT PRIMARY KEY, address VARCHAR(200) NOT NULL, floors INT CHECK (floors > 0));",
            "hint": "Combine PRIMARY KEY, NOT NULL, and CHECK.",
            "explanation": "The city can now be built safely on logical foundations."
          }
        ]
      }
    ]
  },
  "4": {
    "format": "episodic",
    "episodes": [
      {
        "title": "Module 1: The Tangled Archive & First Normal Form (1NF)",
        "blocks": [
          {
            "type": "story",
            "title": "The Contract Archive",
            "text": "You enter the shadowy Hall of Records. The archivist, a frail man named Silas, points to a towering pile of scrolls. 'These are the guild contracts. Individually valid, but impossible to combine consistently. We cannot find who owes what.'"
          },
          {
            "type": "problem",
            "text": "The data is a mess. We have multiple values squeezed into single cells. We need atomic data."
          },
          {
            "type": "concept",
            "title": "First Normal Form (1NF)",
            "explanation": "A relation is in 1NF if every attribute contains only atomic (indivisible) values, and there are no repeating groups.",
            "analogy": "Imagine a shopping list where one line says 'Apples, Bananas, Pears'. In 1NF, you must write three separate lines.",
            "technical_explanation": "Each column in a row must hold a single value. There should be no multi-valued attributes.",
            "why_it_matters": "If values aren't atomic, querying (like finding all contracts involving 'Bananas') requires complex string manipulation.",
            "remember": "One cell, one value."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "BAD:\n| ID | Names |\n| 1  | Alice, Bob |\n\nGOOD (1NF):\n| ID | Name  |\n| 1  | Alice |\n| 1  | Bob   |"
          },
          {
            "type": "worked_example",
            "title": "Normalizing to 1NF",
            "steps": [
              "1. Identify the multi-valued attribute: 'Names'",
              "2. Create a new row for each value in the multi-valued attribute, repeating the primary key."
            ]
          },
          {
            "type": "reflection",
            "question": "Why would keeping multiple names in one string column make it hard to update a specific person's name?"
          },
          {
            "type": "micro_challenge",
            "question": "Which of these violates 1NF?",
            "options": [
              "A column storing a single integer",
              "A column storing a comma-separated list of tags",
              "A column storing a date"
            ],
            "answer": "A column storing a comma-separated list of tags",
            "explanation": "1NF requires atomic values. A comma-separated list is multi-valued."
          },
          {
            "type": "sql_sandbox",
            "title": "Fixing the Contracts Table",
            "context": "We have a table `contracts_raw` with multi-valued `signatories`. Create a 1NF version `contracts_1nf`.",
            "init_script": "CREATE TABLE contracts_raw (contract_id INT, signatories TEXT); INSERT INTO contracts_raw VALUES (1, 'Alice, Bob');",
            "solution_query": "CREATE TABLE contracts_1nf (contract_id INT, signatory TEXT);\nINSERT INTO contracts_1nf VALUES (1, 'Alice'), (1, 'Bob');\nSELECT * FROM contracts_1nf;",
            "hint": "Create a new table with contract_id and signatory columns, then insert the split values.",
            "explanation": "By splitting the signatories into separate rows, our data is now in 1NF."
          }
        ]
      },
      {
        "title": "Module 2: Second Normal Form (2NF)",
        "blocks": [
          {
            "type": "story",
            "title": "Partial Truths",
            "text": "Silas squints at the newly formatted scrolls. 'Better, but now we have duplicate information. The guild's location is repeated for every contract a guild signs!'"
          },
          {
            "type": "problem",
            "text": "Data redundancy due to partial dependencies on a composite primary key."
          },
          {
            "type": "concept",
            "title": "Second Normal Form (2NF)",
            "explanation": "A relation is in 2NF if it is in 1NF and no non-prime attribute is dependent on any proper subset of any candidate key of the table.",
            "analogy": "If you share a gym membership with your spouse, the gym address depends on the gym, not on you.",
            "technical_explanation": "All non-key attributes must depend on the ENTIRE primary key, not just part of it. Only applies if you have a composite primary key.",
            "why_it_matters": "Reduces redundancy and prevents update anomalies if a partially dependent value changes.",
            "remember": "The whole key, and nothing but the whole key."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "BAD:\n| ContractID (PK) | Guild (PK) | Guild_Address |\n\nGOOD (2NF):\nTable 1: | ContractID | Guild |\nTable 2: | Guild | Guild_Address |"
          },
          {
            "type": "worked_example",
            "title": "Moving to 2NF",
            "steps": [
              "1. Identify the composite key: ContractID + Guild",
              "2. Identify partial dependency: Guild_Address depends only on Guild.",
              "3. Split into two tables."
            ]
          },
          {
            "type": "reflection",
            "question": "What happens if we update the Guild's address in the BAD design but miss a row?"
          },
          {
            "type": "debugger",
            "title": "Spot the Anomaly",
            "scenario": "A guild moves, but only some of its contract records are updated.",
            "options": [
              "Update Anomaly",
              "Insertion Anomaly",
              "Deletion Anomaly"
            ],
            "answer": "Update Anomaly",
            "explanation": "When duplicated data is not uniformly updated, it leads to an update anomaly (inconsistency)."
          },
          {
            "type": "sql_sandbox",
            "title": "Applying 2NF",
            "context": "Separate the guild address into its own table.",
            "init_script": "CREATE TABLE old_contracts (cid INT, guild TEXT, address TEXT); INSERT INTO old_contracts VALUES (1, 'Masons', 'North'), (2, 'Masons', 'North');",
            "solution_query": "CREATE TABLE guilds (guild TEXT, address TEXT);\nINSERT INTO guilds VALUES ('Masons', 'North');\nCREATE TABLE new_contracts (cid INT, guild TEXT);\nINSERT INTO new_contracts VALUES (1, 'Masons'), (2, 'Masons');\nSELECT * FROM guilds;",
            "hint": "Create two tables: one for guilds and one for the contracts linked to the guild.",
            "explanation": "We removed the partial dependency by creating a separate guilds table."
          }
        ]
      },
      {
        "title": "Module 3: Third Normal Form (3NF)",
        "blocks": [
          {
            "type": "story",
            "title": "The Chain of Command",
            "text": "Silas smiles. 'Much cleaner. But wait, we store the Guild Master's name, and the Guild Master's favorite color. The color depends on the Master, not the guild itself!'"
          },
          {
            "type": "problem",
            "text": "Non-key attributes depending on other non-key attributes (transitive dependency)."
          },
          {
            "type": "concept",
            "title": "Third Normal Form (3NF)",
            "explanation": "A relation is in 3NF if it is in 2NF and no non-prime attribute is transitively dependent on the primary key.",
            "analogy": "A country's capital depends on the country, and the capital's population depends on the capital. Population is transitively dependent on the country.",
            "technical_explanation": "Every non-key attribute must depend directly on the primary key. If A->B and B->C, then C depends on A transitively.",
            "why_it_matters": "Further reduces redundancy. Updating the Master's favorite color shouldn't require touching the guild table.",
            "remember": "Nothing but the key."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "BAD:\n| Guild | Master | Master_Color |\n\nGOOD (3NF):\n| Guild | Master |\n| Master | Master_Color |"
          },
          {
            "type": "worked_example",
            "title": "Resolving Transitive Dependencies",
            "steps": [
              "1. Spot the non-key dependency: Master_Color depends on Master.",
              "2. Extract Master and Master_Color into a new table."
            ]
          },
          {
            "type": "reflection",
            "question": "Why is it bad to store the Master's color in the Guild table?"
          },
          {
            "type": "micro_challenge",
            "question": "If Zip_Code -> City, and Employee_ID -> Zip_Code, is City transitively dependent on Employee_ID?",
            "options": [
              "Yes",
              "No"
            ],
            "answer": "Yes",
            "explanation": "Because Employee_ID determines Zip_Code, which determines City."
          },
          {
            "type": "sql_sandbox",
            "title": "Achieving 3NF",
            "context": "Fix the guild table so the Master's color is in a separate table.",
            "init_script": "CREATE TABLE guild_info (guild TEXT, master TEXT, color TEXT); INSERT INTO guild_info VALUES ('Masons', 'Bob', 'Blue');",
            "solution_query": "CREATE TABLE masters (master TEXT, color TEXT);\nINSERT INTO masters VALUES ('Bob', 'Blue');\nCREATE TABLE guild_clean (guild TEXT, master TEXT);\nINSERT INTO guild_clean VALUES ('Masons', 'Bob');\nSELECT * FROM masters;",
            "hint": "Create a `masters` table.",
            "explanation": "By moving the color to a masters table, we remove the transitive dependency."
          }
        ]
      },
      {
        "title": "Module 4: Boyce-Codd Normal Form (BCNF)",
        "blocks": [
          {
            "type": "story",
            "title": "The Overlapping Roles",
            "text": "'Ah,' Silas sighs. 'We have a rare case. A contract can have multiple reviewers, but each reviewer belongs to exactly one department. The department determines the reviewer, but reviewer is part of the key!'"
          },
          {
            "type": "problem",
            "text": "A dependency exists where a determinant is not a candidate key."
          },
          {
            "type": "concept",
            "title": "Boyce-Codd Normal Form (BCNF)",
            "explanation": "A relation is in BCNF if for every non-trivial functional dependency X -> Y, X is a superkey.",
            "analogy": "If every student has a unique counselor, and a counselor only works for one major, the counselor determines the major. But if the key is Student + Major, Counselor is not a key, yet it determines Major.",
            "technical_explanation": "A stronger version of 3NF. It handles cases where there are overlapping candidate keys.",
            "why_it_matters": "Prevents anomalies in edge cases not covered by 3NF.",
            "remember": "Every determinant must be a candidate key."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "BAD:\n| Contract (PK) | Dept (PK) | Reviewer |\n(Reviewer -> Dept)\n\nGOOD:\n| Reviewer | Dept |\n| Contract | Reviewer |"
          },
          {
            "type": "worked_example",
            "title": "BCNF Decomposition",
            "steps": [
              "1. Identify the anomalous dependency: Reviewer -> Dept.",
              "2. Decompose to isolate the determinant."
            ]
          },
          {
            "type": "reflection",
            "question": "Why does BCNF only matter when there are multiple overlapping candidate keys?"
          },
          {
            "type": "debugger",
            "title": "Identify the Determinant",
            "scenario": "In Student + Course -> Instructor, but Instructor -> Course.",
            "options": [
              "Student",
              "Course",
              "Instructor"
            ],
            "answer": "Instructor",
            "explanation": "Instructor determines Course, making it a determinant that isn't a candidate key."
          },
          {
            "type": "sql_sandbox",
            "title": "BCNF Fix",
            "context": "Decompose the table to BCNF.",
            "init_script": "CREATE TABLE rev_bad (contract INT, dept TEXT, reviewer TEXT); INSERT INTO rev_bad VALUES (1, 'Legal', 'Alice');",
            "solution_query": "CREATE TABLE rev_dept (reviewer TEXT, dept TEXT);\nINSERT INTO rev_dept VALUES ('Alice', 'Legal');\nCREATE TABLE rev_contract (contract INT, reviewer TEXT);\nINSERT INTO rev_contract VALUES (1, 'Alice');\nSELECT * FROM rev_dept;",
            "hint": "Separate into rev_dept and rev_contract tables.",
            "explanation": "BCNF is achieved by making sure reviewer, the determinant, is a key in its own table."
          }
        ]
      },
      {
        "title": "Module 5: Fourth Normal Form (4NF)",
        "blocks": [
          {
            "type": "story",
            "title": "Independent Multi-values",
            "text": "'We track what weapons and what armor a guild can craft,' Silas notes. 'But weapons and armor have nothing to do with each other! We are listing every combination!'"
          },
          {
            "type": "problem",
            "text": "Multi-valued dependencies causing massive redundancy when two independent 1:N relationships are in the same table."
          },
          {
            "type": "concept",
            "title": "Fourth Normal Form (4NF)",
            "explanation": "A table is in 4NF if it is in BCNF and has no multi-valued dependencies.",
            "analogy": "If you like Pizza and Tacos, and you like Blue and Red, a table shouldn't force you to list (Pizza, Blue), (Pizza, Red), (Tacos, Blue), (Tacos, Red).",
            "technical_explanation": "If A ->> B and A ->> C, and B and C are independent, they must be in separate tables.",
            "why_it_matters": "Eliminates combinatorial explosions of rows.",
            "remember": "Separate independent multi-valued facts."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "BAD:\n| Guild | Weapon | Armor |\n\nGOOD:\n| Guild | Weapon |\n| Guild | Armor |"
          },
          {
            "type": "worked_example",
            "title": "Resolving MVDs",
            "steps": [
              "1. Notice the cross-product of Weapons and Armor for a Guild.",
              "2. Split into Guild-Weapon and Guild-Armor tables."
            ]
          },
          {
            "type": "reflection",
            "question": "How many rows would we need to add if a guild learned one new weapon but already knew 5 armors in the BAD design?"
          },
          {
            "type": "micro_challenge",
            "question": "What defines a Multi-Valued Dependency (MVD)?",
            "options": [
              "One attribute depends on another",
              "One attribute determines a set of values for another, independent of a third",
              "A determinant is not a key"
            ],
            "answer": "One attribute determines a set of values for another, independent of a third",
            "explanation": "MVDs occur when two independent 1:Many relationships are stored together."
          },
          {
            "type": "sql_sandbox",
            "title": "Applying 4NF",
            "context": "Fix the MVD.",
            "init_script": "CREATE TABLE craft_bad (guild TEXT, weapon TEXT, armor TEXT);",
            "solution_query": "CREATE TABLE guild_weapons (guild TEXT, weapon TEXT);\nCREATE TABLE guild_armor (guild TEXT, armor TEXT);",
            "hint": "Create two tables, one for weapons and one for armor.",
            "explanation": "We separated the independent multi-valued facts."
          }
        ]
      },
      {
        "title": "Module 6: Fifth Normal Form (5NF)",
        "blocks": [
          {
            "type": "story",
            "title": "The Final Constraint",
            "text": "Silas looks exhausted. 'Sometimes, a guild provides a specialist to a client, but only if the guild works with that client AND the guild has that specialist. It's a three-way rule.'"
          },
          {
            "type": "problem",
            "text": "Cyclic dependencies that can't be represented by two tables, but require three to avoid false tuples."
          },
          {
            "type": "concept",
            "title": "Fifth Normal Form (5NF)",
            "explanation": "A relation is in 5NF if every join dependency is implied by the candidate keys.",
            "analogy": "A tripod needs all three legs. You can't reconstruct the full picture with just two of the legs.",
            "technical_explanation": "Deals with cases where a table must be decomposed into THREE or more tables to avoid information loss.",
            "why_it_matters": "Extremely rare, but handles complex cyclic constraints.",
            "remember": "No hidden join dependencies."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "Instead of 1 table (Guild, Client, Specialist), we need 3:\n(Guild, Client), (Client, Specialist), (Guild, Specialist)"
          },
          {
            "type": "worked_example",
            "title": "5NF Decomposition",
            "steps": [
              "1. Identify the 3-way symmetric constraint.",
              "2. Decompose into three pairwise tables."
            ]
          },
          {
            "type": "reflection",
            "question": "Why is 5NF rarely used in practice?"
          },
          {
            "type": "debugger",
            "title": "Join Dependency",
            "scenario": "Rejoining two tables produces more rows than the original table.",
            "options": [
              "Lossy Decomposition",
              "Lossless Decomposition",
              "MVD"
            ],
            "answer": "Lossy Decomposition",
            "explanation": "If a join produces spurious tuples, the decomposition was lossy, violating 5NF principles."
          },
          {
            "type": "sql_sandbox",
            "title": "5NF Tables",
            "context": "Create the 3 pairwise tables.",
            "init_script": "CREATE TABLE tri_bad (g TEXT, c TEXT, s TEXT);",
            "solution_query": "CREATE TABLE gc (g TEXT, c TEXT);\nCREATE TABLE cs (c TEXT, s TEXT);\nCREATE TABLE gs (g TEXT, s TEXT);",
            "hint": "Create gc, cs, and gs tables.",
            "explanation": "5NF requires all three projections to perfectly reconstruct the original relationship."
          }
        ]
      },
      {
        "title": "Module 7: DDL & DML Deep Dive",
        "blocks": [
          {
            "type": "story",
            "title": "Writing the Laws",
            "text": "'Now that the design is perfect,' Silas says, 'we must etch it into stone (DDL) and begin copying the data (DML).'"
          },
          {
            "type": "problem",
            "text": "We need to understand how to structurally define tables vs manipulate the data within them."
          },
          {
            "type": "concept",
            "title": "DDL vs DML",
            "explanation": "Data Definition Language (DDL) defines the schema (CREATE, ALTER, DROP). Data Manipulation Language (DML) manages the data (INSERT, UPDATE, DELETE).",
            "analogy": "DDL is building the bookshelves. DML is putting books on the shelves.",
            "technical_explanation": "DDL operations are usually auto-committed and change the database structure. DML operations affect rows and can be rolled back in a transaction.",
            "why_it_matters": "Crucial distinction for database administration and permissions.",
            "remember": "DDL = Structure, DML = Data."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "DDL:\nCREATE TABLE, ALTER TABLE, DROP TABLE\n\nDML:\nINSERT INTO, UPDATE, DELETE FROM"
          },
          {
            "type": "worked_example",
            "title": "DDL and DML in action",
            "steps": [
              "1. DDL: CREATE TABLE employees (id INT).",
              "2. DML: INSERT INTO employees VALUES (1).",
              "3. DML: UPDATE employees SET id = 2.",
              "4. DDL: DROP TABLE employees."
            ]
          },
          {
            "type": "reflection",
            "question": "Why would granting DDL permissions to a regular user be dangerous?"
          },
          {
            "type": "micro_challenge",
            "question": "Which of the following is a DML command?",
            "options": [
              "ALTER",
              "DROP",
              "UPDATE",
              "CREATE"
            ],
            "answer": "UPDATE",
            "explanation": "UPDATE modifies data, making it DML. The others modify structure (DDL)."
          },
          {
            "type": "sql_sandbox",
            "title": "Build and Populate",
            "context": "Use DDL to create a `test` table with an `id` column, and DML to insert `1`.",
            "init_script": "",
            "solution_query": "CREATE TABLE test (id INT);\nINSERT INTO test VALUES (1);\nSELECT * FROM test;",
            "hint": "CREATE TABLE test (id INT); then INSERT INTO test VALUES (1);",
            "explanation": "You successfully used both DDL and DML."
          }
        ]
      },
      {
        "title": "Module 8: The EXISTS Clause & Final Challenge",
        "blocks": [
          {
            "type": "story",
            "title": "The Master's Verification",
            "text": "Silas hands you a final list. 'We need to quickly verify if any active contracts exist for a given guild. We don't need the contracts, just a Yes or No.'"
          },
          {
            "type": "problem",
            "text": "Checking for existence using JOINs or IN can be slow if there are millions of rows. We need a short-circuit method."
          },
          {
            "type": "concept",
            "title": "The EXISTS Clause",
            "explanation": "EXISTS tests for the existence of any record in a subquery. It returns TRUE if the subquery returns one or more records.",
            "analogy": "Looking into a room to see if *anyone* is there. As soon as you see one person, you stop looking and say 'Yes'.",
            "technical_explanation": "EXISTS is highly optimized. It stops scanning the subquery as soon as it finds the first match.",
            "why_it_matters": "Massive performance gains over using COUNT() > 0 or IN for existence checks.",
            "remember": "EXISTS short-circuits."
          },
          {
            "type": "visual",
            "visual_type": "text",
            "data": "SELECT guild_name FROM guilds g\nWHERE EXISTS (\n  SELECT 1 FROM contracts c WHERE c.guild_id = g.id\n);"
          },
          {
            "type": "worked_example",
            "title": "Using EXISTS",
            "steps": [
              "1. Write the main query.",
              "2. Add WHERE EXISTS.",
              "3. Write a correlated subquery linking back to the main query."
            ]
          },
          {
            "type": "reflection",
            "question": "Why is `SELECT 1` commonly used inside an EXISTS subquery?"
          },
          {
            "type": "debugger",
            "title": "Performance Issue",
            "scenario": "A query using `IN (SELECT id...)` is timing out.",
            "options": [
              "Switch to EXISTS",
              "Use COUNT(*)",
              "Add a GROUP BY"
            ],
            "answer": "Switch to EXISTS",
            "explanation": "EXISTS is often optimized better for large datasets because it short-circuits."
          },
          {
            "type": "sql_sandbox",
            "title": "Final Challenge: Verify Guilds",
            "context": "Find the names of guilds that have AT LEAST one contract using EXISTS.",
            "init_script": "CREATE TABLE guilds (id INT, name TEXT); CREATE TABLE contracts (id INT, guild_id INT); INSERT INTO guilds VALUES (1, 'Masons'), (2, 'Thieves'); INSERT INTO contracts VALUES (101, 1);",
            "solution_query": "SELECT name FROM guilds g WHERE EXISTS (SELECT 1 FROM contracts c WHERE c.guild_id = g.id);",
            "hint": "Use WHERE EXISTS (SELECT 1 FROM contracts c WHERE c.guild_id = g.id)",
            "explanation": "EXISTS efficiently found the Masons guild without needing to process all their potential contracts."
          }
        ]
      }
    ]
  }
}
