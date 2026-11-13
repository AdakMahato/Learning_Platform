NEW_LEVELS = {
  "7": {
    "format": "episodic",
    "episodes": [
      {
        "title": "Module 1: The AI's Contradiction",
        "blocks": [
          {"type": "story", "title": "The Dueling Directives", "text": "Two department heads storm into your office. 'The central AI told me to halt production because we are over budget!' yells one. 'It told ME to double production because we have surplus!' yells the other. Both present reports generated at exactly 14:00:00 by the same AI, from the same central database."},
          {"type": "problem", "text": "How can the exact same query, run at the exact same time, produce contradictory results from the same database?"},
          {"type": "concept", "title": "Database Isolation", "explanation": "When multiple users or processes access a database simultaneously, they might see data in different states if transactions are actively modifying it.", "analogy": "Imagine two people reading a whiteboard while a third person is erasing and rewriting parts of it. Depending on when they blink, they see different messages.", "technical_explanation": "Isolation is the 'I' in ACID. It defines how/when the changes made by one operation become visible to other concurrent operations.", "why_it_matters": "Without isolation, concurrent transactions interfere with each other, leading to dirty reads, non-repeatable reads, or phantom reads.", "remember": "Perfect isolation makes concurrent transactions appear as if they executed sequentially."}
        ]
      },
      {
        "title": "Module 2: The Dirty Read",
        "blocks": [
          {"type": "concept", "title": "Read Uncommitted and Dirty Reads", "explanation": "The lowest level of isolation is Read Uncommitted. It allows a transaction to read data that has been modified by another transaction, but not yet committed.", "analogy": "Reading someone's draft email before they decide to send it or delete it.", "technical_explanation": "A Dirty Read occurs when Transaction A reads data modified by Transaction B, but Transaction B then rolls back. Transaction A acted on data that 'never existed'.", "why_it_matters": "Dirty reads lead to decisions based on false or rolled-back information.", "remember": "Never trust uncommitted data for critical operations."},
          {"type": "visual", "visual_type": "text", "data": "Time | Transaction 1 (T1)       | Transaction 2 (T2)\n----------------------------------------------------\n 1   | BEGIN                    |\n 2   | UPDATE budget=500        |\n 3   |                          | BEGIN\n 4   |                          | SELECT budget -> 500 (Dirty Read!)\n 5   | ROLLBACK (budget=100)    |\n 6   |                          | -- T2 thinks budget is 500, but it's 100!"},
          {"type": "micro_challenge", "question": "If an AI decision system operates under READ UNCOMMITTED isolation, what might happen?", "options": ["It can never access data.", "It might make decisions based on transactions that are later aborted/rolled back.", "It will perfectly wait for all transactions to finish."], "answer": "It might make decisions based on transactions that are later aborted/rolled back.", "explanation": "Read Uncommitted allows reading data that is in the middle of being modified and might be rolled back."}
        ]
      },
      {
        "title": "Module 3: Non-Repeatable Reads",
        "blocks": [
          {"type": "concept", "title": "Read Committed and Non-Repeatable Reads", "explanation": "To fix dirty reads, databases use Read Committed. You only see data that has been fully committed. But a new problem arises: if you read the same row twice in your transaction, someone else might commit a change in between.", "analogy": "Checking a bank account balance, seeing $100, then trying to withdraw $100 but failing because a recurring bill cleared right after your first check.", "technical_explanation": "A Non-Repeatable Read occurs when T1 reads a row, T2 updates that row and commits, and T1 reads the row again and gets a different value.", "why_it_matters": "Calculations that rely on multiple reads of the same data within a transaction can become inconsistent.", "remember": "Read Committed only guarantees the data was committed AT THE MOMENT you read it, not that it will stay that way."}
        ]
      },
      {
        "title": "Module 4: Multi-Version Concurrency Control (MVCC)",
        "blocks": [
          {"type": "concept", "title": "The MVCC Solution", "explanation": "Instead of locking rows and making everyone wait, modern databases keep multiple versions of the data.", "analogy": "Using a version control system like Git. When you read, you look at a specific commit (snapshot), even if others are making new commits.", "technical_explanation": "MVCC (Multi-Version Concurrency Control) assigns each transaction an ID. When a row is updated, a new version is created. Transactions only 'see' versions committed before their start time.", "why_it_matters": "MVCC allows readers to read without blocking writers, and writers to write without blocking readers.", "remember": "Readers don't block writers, writers don't block readers."},
          {"type": "visual", "visual_type": "text", "data": "Row: Budget = 100\n[TxID: 10] UPDATE budget=200\n\nDatabase stores:\nVersion A (Created Tx 1): Budget=100 (Valid until Tx 10)\nVersion B (Created Tx 10): Budget=200 (Valid for Tx > 10)"},
          {"type": "debugger", "title": "MVCC Visibility", "scenario": "Transaction 15 starts. Transaction 12 is currently running and hasn't committed. Transaction 10 committed yesterday. Which version of the data does Tx 15 see?", "options": ["The version created by Tx 12", "The version created by Tx 10", "A mix of both"], "answer": "The version created by Tx 10", "explanation": "Tx 15 can only see data committed before it started. Tx 12 hasn't committed, so its changes are invisible to Tx 15."}
        ]
      },
      {
        "title": "Module 5: Snapshot Isolation",
        "blocks": [
          {"type": "concept", "title": "Snapshot Isolation", "explanation": "Building on MVCC, Snapshot Isolation guarantees that a transaction sees a consistent snapshot of the database as it existed at the start of the transaction.", "analogy": "Taking a photograph of a busy street. The photograph doesn't change, even as cars continue to move in real life.", "technical_explanation": "When a transaction starts under Snapshot Isolation (often implemented as REPEATABLE READ in some RDBMS), it gets a 'snapshot' ID. It ignores all changes made by transactions that commit after its snapshot ID.", "why_it_matters": "It prevents both Dirty Reads and Non-Repeatable Reads, providing a highly consistent view for complex reporting.", "remember": "Your transaction exists in a time capsule."}
        ]
      },
      {
        "title": "Module 6: Temporal Data and Auditing",
        "blocks": [
          {"type": "concept", "title": "Time-Travel Queries", "explanation": "If the database keeps old versions of rows (like in MVCC), what if we expose that to the user? This is temporal data.", "analogy": "Looking at the 'revision history' of a Wikipedia page to see what it looked like exactly on Jan 1st, 2020.", "technical_explanation": "System-versioned temporal tables automatically keep a history of all changes, storing valid_from and valid_to timestamps. You can query the table `AS OF` a specific timestamp.", "why_it_matters": "Essential for auditing, compliance, and recovering from accidental deletions.", "remember": "Temporal tables remember everything."}
        ]
      },
      {
        "title": "Module 7: Designing an Audit Trail",
        "blocks": [
          {"type": "worked_example", "title": "Creating an Audit Table via Triggers", "steps": ["1. Create the main table (e.g., accounts)", "2. Create the audit table (e.g., accounts_audit) with identical columns plus timestamp and operation type.", "3. Write a database TRIGGER that runs AFTER UPDATE or AFTER DELETE.", "4. Inside the trigger, insert the OLD row values into the audit table."]},
          {"type": "sql_sandbox", "title": "Implementing the Audit", "context": "We need to track every change to the budget. Create an audit trail.", "init_script": "CREATE TABLE budget (id INT, amount INT); CREATE TABLE budget_audit (id INT, amount INT, changed_at DATETIME);", "solution_query": "CREATE TRIGGER audit_budget AFTER UPDATE ON budget FOR EACH ROW BEGIN INSERT INTO budget_audit (id, amount, changed_at) VALUES (OLD.id, OLD.amount, CURRENT_TIMESTAMP); END;", "hint": "Use CREATE TRIGGER and INSERT INTO the audit table using the OLD values.", "explanation": "Triggers allow you to automatically capture historical states before modifications occur."}
        ]
      },
      {
        "title": "Module 8: Resolving the AI's Contradiction",
        "blocks": [
          {"type": "story", "title": "The Final Verdict", "text": "You realize the central AI was using READ COMMITTED, and generating the report took 5 minutes. Halfway through, a massive budget transfer was committed. The first department's data was read before the transfer, the second's after. The AI saw an inconsistent state."},
          {"type": "problem", "text": "Fix the AI's view so it sees a perfectly consistent snapshot from exactly 14:00:00."},
          {"type": "sql_sandbox", "title": "Setting Isolation Level", "context": "Change the transaction isolation level to ensure a consistent snapshot for the entire transaction in SQLite.", "init_script": "PRAGMA read_uncommitted = true;", "solution_query": "PRAGMA read_uncommitted = false; BEGIN IMMEDIATE;", "hint": "To get a snapshot in SQLite, you disable read uncommitted and start a transaction.", "explanation": "Ensuring the correct isolation level (like Serializable or Snapshot Isolation) prevents the anomalies that cause inconsistent reports."}
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
          {"type": "story", "title": "Half a Billion Bursts", "text": "Deep space sensors have recorded 500,000,000 electromagnetic radio bursts. Our analysts suspect one specific frequency pattern repeats exactly every 72 hours, but every time they run a query to find it, the database grinds to a halt and crashes."},
          {"type": "problem", "text": "How do you search through half a billion records without checking every single one?"},
          {"type": "concept", "title": "The Sequential Scan", "explanation": "Without any special structures, finding a specific record means looking at the first one, then the second, then the third, until the end.", "analogy": "Looking for a specific word in a dictionary by reading from page 1, line 1, until you find it.", "technical_explanation": "A Sequential Scan (or Full Table Scan) reads every block of the table from disk into memory and checks if it matches the WHERE clause.", "why_it_matters": "O(N) time complexity. It scales terribly. As data grows, queries become impossibly slow.", "remember": "Sequential scan is the enemy of large datasets."}
        ]
      },
      {
        "title": "Module 2: Introducing Indexing",
        "blocks": [
          {"type": "concept", "title": "Database Indexes", "explanation": "An index is a separate data structure that keeps a sorted copy of a specific column, along with pointers to the original row.", "analogy": "The index at the back of a textbook. It's sorted alphabetically, telling you exactly which page contains the topic.", "technical_explanation": "By creating an index on a column, the database can use fast lookup algorithms (like binary search) instead of a full sequential scan.", "why_it_matters": "Reduces lookup time from O(N) to O(log N).", "remember": "Indexes trade write speed and storage space for massive read speed improvements."},
          {"type": "visual", "visual_type": "text", "data": "Table: [ID: 1, Freq: 800], [ID: 2, Freq: 100], [ID: 3, Freq: 500]\n\nIndex on Freq:\n[Freq: 100 -> Pointer to Row 2]\n[Freq: 500 -> Pointer to Row 3]\n[Freq: 800 -> Pointer to Row 1]"}
        ]
      },
      {
        "title": "Module 3: B-Trees (Balanced Trees)",
        "blocks": [
          {"type": "concept", "title": "The Anatomy of a B-Tree", "explanation": "Most database indexes use a B-Tree (Balanced Tree) structure. It's a hierarchical tree designed to minimize disk reads.", "analogy": "A filing cabinet system where the top drawer tells you which floor to go to, the floor tells you which room, and the room has the exact file.", "technical_explanation": "A B-Tree keeps data sorted and allows searches, sequential access, insertions, and deletions in logarithmic time. The 'Balanced' part means all paths from root to leaf have the same length.", "why_it_matters": "Disk I/O is slow. B-Trees are wide and shallow, meaning you only need to read 3 or 4 disk blocks to find one record out of billions.", "remember": "B-Trees minimize disk hops."},
          {"type": "visual", "visual_type": "text", "data": "          [ 500 ]\n         /       \\\n  [ 100, 300 ]   [ 700, 900 ]\n   /    |    \\      |    \\\nLeaf  Leaf  Leaf  Leaf  Leaf"}
        ]
      },
      {
        "title": "Module 4: Index Scans vs. Seeks",
        "blocks": [
          {"type": "concept", "title": "How Indexes Are Used", "explanation": "Having an index doesn't guarantee it will be used efficiently.", "analogy": "Having a dictionary is useless if you're looking for 'words that end in -ing'. You still have to read the whole book.", "technical_explanation": "Index Seek: Traversing the B-Tree directly to the exact value (O(log N)). Index Scan: Reading across the bottom leaf nodes of the index (faster than full table scan, but still O(N) over the index).", "why_it_matters": "Queries with functions (e.g., `WHERE YEAR(date) = 2023`) or leading wildcards (e.g., `LIKE '%pattern'`) prevent the database from doing an Index Seek.", "remember": "Don't hide indexed columns inside functions in your WHERE clause."},
          {"type": "debugger", "title": "Sargability", "scenario": "You have an index on `frequency_hz`. Which query will use an Index Seek?", "options": ["SELECT * FROM signals WHERE frequency_hz * 2 = 1000", "SELECT * FROM signals WHERE frequency_hz = 500", "SELECT * FROM signals WHERE CAST(frequency_hz AS TEXT) LIKE '5%'"], "answer": "SELECT * FROM signals WHERE frequency_hz = 500", "explanation": "The first and third options wrap the column in operations, preventing the database from searching the B-Tree directly."}
        ]
      },
      {
        "title": "Module 5: The Cost of Indexing",
        "blocks": [
          {"type": "concept", "title": "Trade-offs of Indexes", "explanation": "If indexes make reads fast, why not index every single column?", "analogy": "If you add every single word of a book to the index at the back, the index becomes larger than the book itself.", "technical_explanation": "Every time you INSERT, UPDATE, or DELETE a row, the database must also update all corresponding B-Trees. This adds significant write latency and consumes disk space.", "why_it_matters": "Over-indexing kills database write performance.", "remember": "Indexes are not free."}
        ]
      },
      {
        "title": "Module 6: Composite Indexes",
        "blocks": [
          {"type": "concept", "title": "Multi-Column Indexes", "explanation": "Sometimes queries filter on multiple columns at once.", "analogy": "A phone book is a composite index: (Last Name, First Name). You can easily find 'Smith, John', or all 'Smiths', but you cannot use it to find all people named 'John'.", "technical_explanation": "A composite index sorts by Column A, then by Column B. The order matters! It can only be used if the query filters on a prefix of the indexed columns (e.g., A, or A and B, but NOT just B).", "why_it_matters": "Designing composite indexes requires understanding query patterns to get the order right.", "remember": "Left-to-right rule for composite indexes."}
        ]
      },
      {
        "title": "Module 7: Materialized Views and OLAP",
        "blocks": [
          {"type": "concept", "title": "Pre-computing Results", "explanation": "If millions of users run the exact same heavy analytical query (OLAP), even indexes might not be fast enough.", "analogy": "Instead of cooking a fresh meal from scratch every time someone orders, you prepare a massive batch in advance and serve portions.", "technical_explanation": "A Materialized View stores the physical result of a complex query on disk. When queried, it returns immediately. The trade-off is that it must be periodically refreshed, so data might be slightly stale.", "why_it_matters": "Crucial for dashboards and analytical workloads where massive aggregations are required instantly.", "remember": "Materialized views trade real-time freshness for blazing fast aggregations."}
        ]
      },
      {
        "title": "Module 8: Finding the Pattern",
        "blocks": [
          {"type": "story", "title": "The 72-Hour Anomaly", "text": "You realize the researchers are running a query checking both the frequency range AND the exact origin sector of the bursts. You need to build the perfect index to make this query instant."},
          {"type": "sql_sandbox", "title": "Creating the Composite Index", "context": "The table `bursts` has columns `id`, `frequency`, `sector`, `timestamp`. The query is ALWAYS `WHERE sector = ? AND frequency > ?`. Create the optimal index.", "init_script": "CREATE TABLE bursts (id INT, frequency INT, sector TEXT, timestamp DATETIME);", "solution_query": "CREATE INDEX idx_sector_freq ON bursts (sector, frequency);", "hint": "Order matters. Equality checks (sector =) should usually precede range checks (frequency >) in a composite index.", "explanation": "By putting the equality condition first, the B-Tree immediately jumps to the exact sector, and then uses the sorted frequency within that sector to quickly evaluate the range."}
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
          {"type": "story", "title": "The Cargo Dispute", "text": "Mars, Luna, and Titan colonies share a unified inventory database. A transport ship has exactly 100 Fusion Cores. Mars claims 100. Titan claims 100. Because space communication is heavily delayed and occasionally fails, both colonies saw '100 Available' and both approved the claim. Now they are at war."},
          {"type": "problem", "text": "How do you maintain a single unified truth across databases separated by vast physical distances and unreliable networks?"},
          {"type": "concept", "title": "Distributed Databases", "explanation": "A distributed database stores data across multiple physical locations.", "analogy": "A team of accountants in different cities trying to balance the exact same ledger via mail.", "technical_explanation": "Nodes (servers) must communicate to ensure data remains consistent. If Node A updates a record, it must replicate that change to Node B.", "why_it_matters": "Single servers are a single point of failure and have scale limits. Distribution provides high availability and scale, but introduces immense complexity.", "remember": "The network is never reliable."}
        ]
      },
      {
        "title": "Module 2: Replication Strategies",
        "blocks": [
          {"type": "concept", "title": "Primary-Replica vs. Multi-Primary", "explanation": "How do we decide who gets to write data?", "analogy": "A classroom where only the teacher can write on the board (Primary) vs. a shared Google Doc where anyone can type (Multi-Primary).", "technical_explanation": "Primary-Replica (Master-Slave): All writes go to one node, which streams changes to read-only replicas. Multi-Primary: Any node can accept writes, requiring complex conflict resolution.", "why_it_matters": "Primary-Replica is easy but the Primary is a bottleneck. Multi-Primary scales writes but leads to the exact conflict the Mars/Titan colonies experienced.", "remember": "Multiple writers mean inevitable conflicts."}
        ]
      },
      {
        "title": "Module 3: The CAP Theorem",
        "blocks": [
          {"type": "concept", "title": "Consistency, Availability, Partition Tolerance", "explanation": "In 2000, Eric Brewer proved you can't have it all in a distributed system.", "analogy": "You can have it Fast, Cheap, or Good. Pick two.", "technical_explanation": "CAP Theorem states a distributed system can provide only two of three: Consistency (every read receives the most recent write), Availability (every request receives a response), and Partition Tolerance (the system operates despite network failures).", "why_it_matters": "Because network partitions (P) are a physical reality you cannot avoid, you must choose between C and A when a network failure occurs.", "remember": "During a network split, you must choose: Stop responding (Consistency) or respond with stale data (Availability)."}
        ]
      },
      {
        "title": "Module 4: Applying CAP to the Colonies",
        "blocks": [
          {"type": "visual", "visual_type": "text", "data": "Network Cut between Mars & Titan\n\nTitan Node: 'Client wants 100 Cores'\n\nChoice 1 (CP - Consistency): Titan says 'I can't reach Mars to verify, so I must reject the request.'\nChoice 2 (AP - Availability): Titan says 'I have no connection, but my local data says 100, so I approve it.'"},
          {"type": "debugger", "title": "CAP Tradeoffs", "scenario": "A medical database tracking lethal drug interactions cannot ever return incorrect/stale data, even if offline. What does it prioritize?", "options": ["AP (Availability & Partition Tolerance)", "CP (Consistency & Partition Tolerance)", "CA (Consistency & Availability)"], "answer": "CP (Consistency & Partition Tolerance)", "explanation": "It must prioritize Consistency. If the network drops (Partition), it will refuse to answer (sacrificing Availability) rather than risk giving deadly wrong information."}
        ]
      },
      {
        "title": "Module 5: Eventual Consistency",
        "blocks": [
          {"type": "concept", "title": "Embracing AP", "explanation": "Many modern systems choose AP. They accept that data might be out of sync briefly, but will 'eventually' become consistent once the network heals.", "analogy": "Social media likes. If you like a post, your friend might not see the like for a few seconds. Nobody dies.", "technical_explanation": "Nodes accept writes locally and broadcast them asynchronously. Systems like DynamoDB or Cassandra often use tunable consistency models.", "why_it_matters": "Provides maximum uptime and lowest latency, critical for massive consumer apps.", "remember": "Eventual consistency means it's wrong right now, but will be right later."}
        ]
      },
      {
        "title": "Module 6: Distributed Consensus",
        "blocks": [
          {"type": "concept", "title": "Paxos and Raft", "explanation": "If we choose CP (Consistency), how do nodes agree on the truth?", "analogy": "A jury voting on a verdict. They must follow strict rules to ensure a majority agrees before deciding.", "technical_explanation": "Consensus algorithms like Raft require a majority (quorum) of nodes to acknowledge a write before it is committed. If there are 5 nodes, 3 must agree.", "why_it_matters": "This solves the Mars/Titan problem. If the network splits, only the side with the majority can process writes. The minority partition pauses, preventing split-brain.", "remember": "Consensus requires a majority vote."}
        ]
      },
      {
        "title": "Module 7: Data Partitioning (Sharding)",
        "blocks": [
          {"type": "concept", "title": "Splitting the Data", "explanation": "When data is too large for one server, we split it. This is Partitioning or Sharding.", "analogy": "Organizing a library by putting A-M on the first floor and N-Z on the second floor.", "technical_explanation": "A Shard Key determines which node holds the data. If sharded by 'colony_id', Mars data lives on Mars servers.", "why_it_matters": "Allows infinite horizontal scaling. But cross-shard queries (e.g., 'Total inventory across all colonies') become very expensive.", "remember": "Pick your shard key carefully, or one node will do all the work (a hot partition)."}
        ]
      },
      {
        "title": "Module 8: Securing the Cargo",
        "blocks": [
          {"type": "story", "title": "Implementing Two-Phase Commit", "text": "To prevent the cargo dispute from ever happening again, you implement a protocol where ALL colonies must agree before inventory is deducted."},
          {"type": "problem", "text": "Simulate the preparation phase of a distributed transaction."},
          {"type": "sql_sandbox", "title": "State Tracking for 2PC", "context": "In a Two-Phase Commit (2PC), a transaction is first 'PREPARED'. Update the transaction state.", "init_script": "CREATE TABLE distributed_tx (tx_id INT, state TEXT); INSERT INTO distributed_tx VALUES (99, 'PENDING');", "solution_query": "UPDATE distributed_tx SET state = 'PREPARED' WHERE tx_id = 99;", "hint": "Update the state string to PREPARED.", "explanation": "In 2PC, the coordinator asks all nodes to 'PREPARE'. Only if all nodes reply YES, does it then broadcast 'COMMIT'."}
        ]
      }
    ]
  }
}
