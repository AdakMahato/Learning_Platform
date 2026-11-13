NEW_LEVELS = {
  "10": {
    "format": "episodic",
    "episodes": [
      {
        "title": "Module 1: The Divergent Rulebooks",
        "blocks": [
          {
            "type": "story",
            "title": "Sector Disarray",
            "text": "In the sprawling mechanical metropolis of GearCity, twelve distinct robot sectors operate in unison—or at least they are supposed to. Recently, operations have ground to a halt. When central command asks for the current rulebook version, each sector returns a different answer."
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
            "why_it_matters": "Having a single leader simplifies the problem of agreement—there is only one source of new entries.",
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
            "options": ["3", "4", "5"],
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
            "options": ["Yes, always index everything.", "No, indexes will slow down the heavy insert workload.", "Yes, but only if they are hash indexes."],
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
  }
}
