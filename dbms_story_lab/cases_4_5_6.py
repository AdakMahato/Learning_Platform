def get_case_4():
    return {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Tangled Archive & First Normal Form (1NF)",
                "blocks": [
                    {"type": "story", "title": "The Contract Archive", "text": "You enter the shadowy Hall of Records. The archivist, a frail man named Silas, points to a towering pile of scrolls. 'These are the guild contracts. Individually valid, but impossible to combine consistently. We cannot find who owes what.'"},
                    {"type": "problem", "text": "The data is a mess. We have multiple values squeezed into single cells. We need atomic data."},
                    {"type": "concept", "title": "First Normal Form (1NF)", "explanation": "A relation is in 1NF if every attribute contains only atomic (indivisible) values, and there are no repeating groups.", "analogy": "Imagine a shopping list where one line says 'Apples, Bananas, Pears'. In 1NF, you must write three separate lines.", "technical_explanation": "Each column in a row must hold a single value. There should be no multi-valued attributes.", "why_it_matters": "If values aren't atomic, querying (like finding all contracts involving 'Bananas') requires complex string manipulation.", "remember": "One cell, one value."},
                    {"type": "visual", "visual_type": "text", "data": "BAD:\n| ID | Names |\n| 1  | Alice, Bob |\n\nGOOD (1NF):\n| ID | Name  |\n| 1  | Alice |\n| 1  | Bob   |"},
                    {"type": "worked_example", "title": "Normalizing to 1NF", "steps": ["1. Identify the multi-valued attribute: 'Names'", "2. Create a new row for each value in the multi-valued attribute, repeating the primary key."]},
                    {"type": "reflection", "question": "Why would keeping multiple names in one string column make it hard to update a specific person's name?"},
                    {"type": "micro_challenge", "question": "Which of these violates 1NF?", "options": ["A column storing a single integer", "A column storing a comma-separated list of tags", "A column storing a date"], "answer": "A column storing a comma-separated list of tags", "explanation": "1NF requires atomic values. A comma-separated list is multi-valued."},
                    {"type": "sql_sandbox", "title": "Fixing the Contracts Table", "context": "We have a table `contracts_raw` with multi-valued `signatories`. Create a 1NF version `contracts_1nf`.", "init_script": "CREATE TABLE contracts_raw (contract_id INT, signatories TEXT); INSERT INTO contracts_raw VALUES (1, 'Alice, Bob');", "solution_query": "CREATE TABLE contracts_1nf (contract_id INT, signatory TEXT);\nINSERT INTO contracts_1nf VALUES (1, 'Alice'), (1, 'Bob');\nSELECT * FROM contracts_1nf;", "hint": "Create a new table with contract_id and signatory columns, then insert the split values.", "explanation": "By splitting the signatories into separate rows, our data is now in 1NF."}
                ]
            },
            {
                "title": "Module 2: Second Normal Form (2NF)",
                "blocks": [
                    {"type": "story", "title": "Partial Truths", "text": "Silas squints at the newly formatted scrolls. 'Better, but now we have duplicate information. The guild's location is repeated for every contract a guild signs!'"},
                    {"type": "problem", "text": "Data redundancy due to partial dependencies on a composite primary key."},
                    {"type": "concept", "title": "Second Normal Form (2NF)", "explanation": "A relation is in 2NF if it is in 1NF and no non-prime attribute is dependent on any proper subset of any candidate key of the table.", "analogy": "If you share a gym membership with your spouse, the gym address depends on the gym, not on you.", "technical_explanation": "All non-key attributes must depend on the ENTIRE primary key, not just part of it. Only applies if you have a composite primary key.", "why_it_matters": "Reduces redundancy and prevents update anomalies if a partially dependent value changes.", "remember": "The whole key, and nothing but the whole key."},
                    {"type": "visual", "visual_type": "text", "data": "BAD:\n| ContractID (PK) | Guild (PK) | Guild_Address |\n\nGOOD (2NF):\nTable 1: | ContractID | Guild |\nTable 2: | Guild | Guild_Address |"},
                    {"type": "worked_example", "title": "Moving to 2NF", "steps": ["1. Identify the composite key: ContractID + Guild", "2. Identify partial dependency: Guild_Address depends only on Guild.", "3. Split into two tables."]},
                    {"type": "reflection", "question": "What happens if we update the Guild's address in the BAD design but miss a row?"},
                    {"type": "debugger", "title": "Spot the Anomaly", "scenario": "A guild moves, but only some of its contract records are updated.", "options": ["Update Anomaly", "Insertion Anomaly", "Deletion Anomaly"], "answer": "Update Anomaly", "explanation": "When duplicated data is not uniformly updated, it leads to an update anomaly (inconsistency)."},
                    {"type": "sql_sandbox", "title": "Applying 2NF", "context": "Separate the guild address into its own table.", "init_script": "CREATE TABLE old_contracts (cid INT, guild TEXT, address TEXT); INSERT INTO old_contracts VALUES (1, 'Masons', 'North'), (2, 'Masons', 'North');", "solution_query": "CREATE TABLE guilds (guild TEXT, address TEXT);\nINSERT INTO guilds VALUES ('Masons', 'North');\nCREATE TABLE new_contracts (cid INT, guild TEXT);\nINSERT INTO new_contracts VALUES (1, 'Masons'), (2, 'Masons');\nSELECT * FROM guilds;", "hint": "Create two tables: one for guilds and one for the contracts linked to the guild.", "explanation": "We removed the partial dependency by creating a separate guilds table."}
                ]
            },
            {
                "title": "Module 3: Third Normal Form (3NF)",
                "blocks": [
                    {"type": "story", "title": "The Chain of Command", "text": "Silas smiles. 'Much cleaner. But wait, we store the Guild Master's name, and the Guild Master's favorite color. The color depends on the Master, not the guild itself!'"},
                    {"type": "problem", "text": "Non-key attributes depending on other non-key attributes (transitive dependency)."},
                    {"type": "concept", "title": "Third Normal Form (3NF)", "explanation": "A relation is in 3NF if it is in 2NF and no non-prime attribute is transitively dependent on the primary key.", "analogy": "A country's capital depends on the country, and the capital's population depends on the capital. Population is transitively dependent on the country.", "technical_explanation": "Every non-key attribute must depend directly on the primary key. If A->B and B->C, then C depends on A transitively.", "why_it_matters": "Further reduces redundancy. Updating the Master's favorite color shouldn't require touching the guild table.", "remember": "Nothing but the key."},
                    {"type": "visual", "visual_type": "text", "data": "BAD:\n| Guild | Master | Master_Color |\n\nGOOD (3NF):\n| Guild | Master |\n| Master | Master_Color |"},
                    {"type": "worked_example", "title": "Resolving Transitive Dependencies", "steps": ["1. Spot the non-key dependency: Master_Color depends on Master.", "2. Extract Master and Master_Color into a new table."]},
                    {"type": "reflection", "question": "Why is it bad to store the Master's color in the Guild table?"},
                    {"type": "micro_challenge", "question": "If Zip_Code -> City, and Employee_ID -> Zip_Code, is City transitively dependent on Employee_ID?", "options": ["Yes", "No"], "answer": "Yes", "explanation": "Because Employee_ID determines Zip_Code, which determines City."},
                    {"type": "sql_sandbox", "title": "Achieving 3NF", "context": "Fix the guild table so the Master's color is in a separate table.", "init_script": "CREATE TABLE guild_info (guild TEXT, master TEXT, color TEXT); INSERT INTO guild_info VALUES ('Masons', 'Bob', 'Blue');", "solution_query": "CREATE TABLE masters (master TEXT, color TEXT);\nINSERT INTO masters VALUES ('Bob', 'Blue');\nCREATE TABLE guild_clean (guild TEXT, master TEXT);\nINSERT INTO guild_clean VALUES ('Masons', 'Bob');\nSELECT * FROM masters;", "hint": "Create a `masters` table.", "explanation": "By moving the color to a masters table, we remove the transitive dependency."}
                ]
            },
            {
                "title": "Module 4: Boyce-Codd Normal Form (BCNF)",
                "blocks": [
                    {"type": "story", "title": "The Overlapping Roles", "text": "'Ah,' Silas sighs. 'We have a rare case. A contract can have multiple reviewers, but each reviewer belongs to exactly one department. The department determines the reviewer, but reviewer is part of the key!'"},
                    {"type": "problem", "text": "A dependency exists where a determinant is not a candidate key."},
                    {"type": "concept", "title": "Boyce-Codd Normal Form (BCNF)", "explanation": "A relation is in BCNF if for every non-trivial functional dependency X -> Y, X is a superkey.", "analogy": "If every student has a unique counselor, and a counselor only works for one major, the counselor determines the major. But if the key is Student + Major, Counselor is not a key, yet it determines Major.", "technical_explanation": "A stronger version of 3NF. It handles cases where there are overlapping candidate keys.", "why_it_matters": "Prevents anomalies in edge cases not covered by 3NF.", "remember": "Every determinant must be a candidate key."},
                    {"type": "visual", "visual_type": "text", "data": "BAD:\n| Contract (PK) | Dept (PK) | Reviewer |\n(Reviewer -> Dept)\n\nGOOD:\n| Reviewer | Dept |\n| Contract | Reviewer |"},
                    {"type": "worked_example", "title": "BCNF Decomposition", "steps": ["1. Identify the anomalous dependency: Reviewer -> Dept.", "2. Decompose to isolate the determinant."]},
                    {"type": "reflection", "question": "Why does BCNF only matter when there are multiple overlapping candidate keys?"},
                    {"type": "debugger", "title": "Identify the Determinant", "scenario": "In Student + Course -> Instructor, but Instructor -> Course.", "options": ["Student", "Course", "Instructor"], "answer": "Instructor", "explanation": "Instructor determines Course, making it a determinant that isn't a candidate key."},
                    {"type": "sql_sandbox", "title": "BCNF Fix", "context": "Decompose the table to BCNF.", "init_script": "CREATE TABLE rev_bad (contract INT, dept TEXT, reviewer TEXT); INSERT INTO rev_bad VALUES (1, 'Legal', 'Alice');", "solution_query": "CREATE TABLE rev_dept (reviewer TEXT, dept TEXT);\nINSERT INTO rev_dept VALUES ('Alice', 'Legal');\nCREATE TABLE rev_contract (contract INT, reviewer TEXT);\nINSERT INTO rev_contract VALUES (1, 'Alice');\nSELECT * FROM rev_dept;", "hint": "Separate into rev_dept and rev_contract tables.", "explanation": "BCNF is achieved by making sure reviewer, the determinant, is a key in its own table."}
                ]
            },
            {
                "title": "Module 5: Fourth Normal Form (4NF)",
                "blocks": [
                    {"type": "story", "title": "Independent Multi-values", "text": "'We track what weapons and what armor a guild can craft,' Silas notes. 'But weapons and armor have nothing to do with each other! We are listing every combination!'"},
                    {"type": "problem", "text": "Multi-valued dependencies causing massive redundancy when two independent 1:N relationships are in the same table."},
                    {"type": "concept", "title": "Fourth Normal Form (4NF)", "explanation": "A table is in 4NF if it is in BCNF and has no multi-valued dependencies.", "analogy": "If you like Pizza and Tacos, and you like Blue and Red, a table shouldn't force you to list (Pizza, Blue), (Pizza, Red), (Tacos, Blue), (Tacos, Red).", "technical_explanation": "If A ->> B and A ->> C, and B and C are independent, they must be in separate tables.", "why_it_matters": "Eliminates combinatorial explosions of rows.", "remember": "Separate independent multi-valued facts."},
                    {"type": "visual", "visual_type": "text", "data": "BAD:\n| Guild | Weapon | Armor |\n\nGOOD:\n| Guild | Weapon |\n| Guild | Armor |"},
                    {"type": "worked_example", "title": "Resolving MVDs", "steps": ["1. Notice the cross-product of Weapons and Armor for a Guild.", "2. Split into Guild-Weapon and Guild-Armor tables."]},
                    {"type": "reflection", "question": "How many rows would we need to add if a guild learned one new weapon but already knew 5 armors in the BAD design?"},
                    {"type": "micro_challenge", "question": "What defines a Multi-Valued Dependency (MVD)?", "options": ["One attribute depends on another", "One attribute determines a set of values for another, independent of a third", "A determinant is not a key"], "answer": "One attribute determines a set of values for another, independent of a third", "explanation": "MVDs occur when two independent 1:Many relationships are stored together."},
                    {"type": "sql_sandbox", "title": "Applying 4NF", "context": "Fix the MVD.", "init_script": "CREATE TABLE craft_bad (guild TEXT, weapon TEXT, armor TEXT);", "solution_query": "CREATE TABLE guild_weapons (guild TEXT, weapon TEXT);\nCREATE TABLE guild_armor (guild TEXT, armor TEXT);", "hint": "Create two tables, one for weapons and one for armor.", "explanation": "We separated the independent multi-valued facts."}
                ]
            },
            {
                "title": "Module 6: Fifth Normal Form (5NF)",
                "blocks": [
                    {"type": "story", "title": "The Final Constraint", "text": "Silas looks exhausted. 'Sometimes, a guild provides a specialist to a client, but only if the guild works with that client AND the guild has that specialist. It's a three-way rule.'"},
                    {"type": "problem", "text": "Cyclic dependencies that can't be represented by two tables, but require three to avoid false tuples."},
                    {"type": "concept", "title": "Fifth Normal Form (5NF)", "explanation": "A relation is in 5NF if every join dependency is implied by the candidate keys.", "analogy": "A tripod needs all three legs. You can't reconstruct the full picture with just two of the legs.", "technical_explanation": "Deals with cases where a table must be decomposed into THREE or more tables to avoid information loss.", "why_it_matters": "Extremely rare, but handles complex cyclic constraints.", "remember": "No hidden join dependencies."},
                    {"type": "visual", "visual_type": "text", "data": "Instead of 1 table (Guild, Client, Specialist), we need 3:\n(Guild, Client), (Client, Specialist), (Guild, Specialist)"},
                    {"type": "worked_example", "title": "5NF Decomposition", "steps": ["1. Identify the 3-way symmetric constraint.", "2. Decompose into three pairwise tables."]},
                    {"type": "reflection", "question": "Why is 5NF rarely used in practice?"},
                    {"type": "debugger", "title": "Join Dependency", "scenario": "Rejoining two tables produces more rows than the original table.", "options": ["Lossy Decomposition", "Lossless Decomposition", "MVD"], "answer": "Lossy Decomposition", "explanation": "If a join produces spurious tuples, the decomposition was lossy, violating 5NF principles."},
                    {"type": "sql_sandbox", "title": "5NF Tables", "context": "Create the 3 pairwise tables.", "init_script": "CREATE TABLE tri_bad (g TEXT, c TEXT, s TEXT);", "solution_query": "CREATE TABLE gc (g TEXT, c TEXT);\nCREATE TABLE cs (c TEXT, s TEXT);\nCREATE TABLE gs (g TEXT, s TEXT);", "hint": "Create gc, cs, and gs tables.", "explanation": "5NF requires all three projections to perfectly reconstruct the original relationship."}
                ]
            },
            {
                "title": "Module 7: DDL & DML Deep Dive",
                "blocks": [
                    {"type": "story", "title": "Writing the Laws", "text": "'Now that the design is perfect,' Silas says, 'we must etch it into stone (DDL) and begin copying the data (DML).'"},
                    {"type": "problem", "text": "We need to understand how to structurally define tables vs manipulate the data within them."},
                    {"type": "concept", "title": "DDL vs DML", "explanation": "Data Definition Language (DDL) defines the schema (CREATE, ALTER, DROP). Data Manipulation Language (DML) manages the data (INSERT, UPDATE, DELETE).", "analogy": "DDL is building the bookshelves. DML is putting books on the shelves.", "technical_explanation": "DDL operations are usually auto-committed and change the database structure. DML operations affect rows and can be rolled back in a transaction.", "why_it_matters": "Crucial distinction for database administration and permissions.", "remember": "DDL = Structure, DML = Data."},
                    {"type": "visual", "visual_type": "text", "data": "DDL:\nCREATE TABLE, ALTER TABLE, DROP TABLE\n\nDML:\nINSERT INTO, UPDATE, DELETE FROM"},
                    {"type": "worked_example", "title": "DDL and DML in action", "steps": ["1. DDL: CREATE TABLE employees (id INT).", "2. DML: INSERT INTO employees VALUES (1).", "3. DML: UPDATE employees SET id = 2.", "4. DDL: DROP TABLE employees."]},
                    {"type": "reflection", "question": "Why would granting DDL permissions to a regular user be dangerous?"},
                    {"type": "micro_challenge", "question": "Which of the following is a DML command?", "options": ["ALTER", "DROP", "UPDATE", "CREATE"], "answer": "UPDATE", "explanation": "UPDATE modifies data, making it DML. The others modify structure (DDL)."},
                    {"type": "sql_sandbox", "title": "Build and Populate", "context": "Use DDL to create a `test` table with an `id` column, and DML to insert `1`.", "init_script": "", "solution_query": "CREATE TABLE test (id INT);\nINSERT INTO test VALUES (1);\nSELECT * FROM test;", "hint": "CREATE TABLE test (id INT); then INSERT INTO test VALUES (1);", "explanation": "You successfully used both DDL and DML."}
                ]
            },
            {
                "title": "Module 8: The EXISTS Clause & Final Challenge",
                "blocks": [
                    {"type": "story", "title": "The Master's Verification", "text": "Silas hands you a final list. 'We need to quickly verify if any active contracts exist for a given guild. We don't need the contracts, just a Yes or No.'"},
                    {"type": "problem", "text": "Checking for existence using JOINs or IN can be slow if there are millions of rows. We need a short-circuit method."},
                    {"type": "concept", "title": "The EXISTS Clause", "explanation": "EXISTS tests for the existence of any record in a subquery. It returns TRUE if the subquery returns one or more records.", "analogy": "Looking into a room to see if *anyone* is there. As soon as you see one person, you stop looking and say 'Yes'.", "technical_explanation": "EXISTS is highly optimized. It stops scanning the subquery as soon as it finds the first match.", "why_it_matters": "Massive performance gains over using COUNT() > 0 or IN for existence checks.", "remember": "EXISTS short-circuits."},
                    {"type": "visual", "visual_type": "text", "data": "SELECT guild_name FROM guilds g\nWHERE EXISTS (\n  SELECT 1 FROM contracts c WHERE c.guild_id = g.id\n);"},
                    {"type": "worked_example", "title": "Using EXISTS", "steps": ["1. Write the main query.", "2. Add WHERE EXISTS.", "3. Write a correlated subquery linking back to the main query."]},
                    {"type": "reflection", "question": "Why is `SELECT 1` commonly used inside an EXISTS subquery?"},
                    {"type": "debugger", "title": "Performance Issue", "scenario": "A query using `IN (SELECT id...)` is timing out.", "options": ["Switch to EXISTS", "Use COUNT(*)", "Add a GROUP BY"], "answer": "Switch to EXISTS", "explanation": "EXISTS is often optimized better for large datasets because it short-circuits."},
                    {"type": "sql_sandbox", "title": "Final Challenge: Verify Guilds", "context": "Find the names of guilds that have AT LEAST one contract using EXISTS.", "init_script": "CREATE TABLE guilds (id INT, name TEXT); CREATE TABLE contracts (id INT, guild_id INT); INSERT INTO guilds VALUES (1, 'Masons'), (2, 'Thieves'); INSERT INTO contracts VALUES (101, 1);", "solution_query": "SELECT name FROM guilds g WHERE EXISTS (SELECT 1 FROM contracts c WHERE c.guild_id = g.id);", "hint": "Use WHERE EXISTS (SELECT 1 FROM contracts c WHERE c.guild_id = g.id)", "explanation": "EXISTS efficiently found the Masons guild without needing to process all their potential contracts."}
                ]
            }
        ]
    }

def get_case_5():
    return {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Ancient Ledger & Intro to JOINs",
                "blocks": [
                    {"type": "story", "title": "The Merchant's Secret", "text": "You uncover an ancient merchant ledger containing 200,000 transactions. But the ledger only has IDs. The names of the merchants are in a separate tome. We must combine them."},
                    {"type": "problem", "text": "Data is split across multiple tables based on foreign keys. We need a unified view."},
                    {"type": "concept", "title": "INNER JOIN", "explanation": "INNER JOIN combines rows from two tables based on a related column, returning only rows that have matching values in both tables.", "analogy": "Matching puzzle pieces. Only pieces that fit perfectly together make it into the final picture.", "technical_explanation": "Performs a cartesian product filtered by the ON condition. It's the intersection of the two sets.", "why_it_matters": "The fundamental way to reconstruct normalized data into readable formats.", "remember": "Matches only."},
                    {"type": "visual", "visual_type": "text", "data": "Table A (1,2) INNER JOIN Table B (2,3)\nResult: (2)"},
                    {"type": "worked_example", "title": "Writing an INNER JOIN", "steps": ["1. SELECT columns.", "2. FROM table1.", "3. INNER JOIN table2 ON table1.id = table2.fk_id."]},
                    {"type": "reflection", "question": "What happens to rows in Table A that have no match in Table B during an INNER JOIN?"},
                    {"type": "micro_challenge", "question": "If Table A has 5 rows and Table B has 5 rows, what is the maximum number of rows an INNER JOIN could return if every row matched every other row?", "options": ["5", "10", "25"], "answer": "25", "explanation": "A cartesian product (all match all) would result in 5 * 5 = 25 rows."},
                    {"type": "sql_sandbox", "title": "Reconstruct the Ledger", "context": "Join `transactions` and `merchants` on `merchant_id`.", "init_script": "CREATE TABLE merchants (id INT, name TEXT); CREATE TABLE transactions (id INT, merchant_id INT, amount INT); INSERT INTO merchants VALUES (1, 'Sal'), (2, 'Boz'); INSERT INTO transactions VALUES (101, 1, 500);", "solution_query": "SELECT m.name, t.amount FROM merchants m INNER JOIN transactions t ON m.id = t.merchant_id;", "hint": "SELECT m.name, t.amount FROM merchants m INNER JOIN transactions t ON ...", "explanation": "You've successfully joined the tables to see Sal's transaction."}
                ]
            },
            {
                "title": "Module 2: Left, Right, and Full Outer JOINs",
                "blocks": [
                    {"type": "story", "title": "The Missing Merchants", "text": "Wait. Some merchants in the tome have NO transactions in the ledger. We need a list of ALL merchants, even if they haven't traded!"},
                    {"type": "problem", "text": "INNER JOIN drops merchants without transactions. We need to preserve the left table's rows."},
                    {"type": "concept", "title": "OUTER JOINs", "explanation": "LEFT JOIN keeps all rows from the left table, padding with NULLs if there's no match. RIGHT JOIN does the same for the right table. FULL JOIN keeps all rows from both.", "analogy": "Inviting all your friends to a party. LEFT JOIN means all your friends show up, even if they don't bring a gift (the right table).", "technical_explanation": "An OUTER JOIN is an INNER JOIN plus the unmatched rows from one or both tables.", "why_it_matters": "Crucial for finding missing data (e.g., finding users who haven't made a purchase).", "remember": "LEFT keeps the LEFT."},
                    {"type": "visual", "visual_type": "text", "data": "Table A (1,2) LEFT JOIN Table B (2,3)\nResult: (1, NULL), (2, matched_data)"},
                    {"type": "worked_example", "title": "Finding Missing Data", "steps": ["1. LEFT JOIN merchants to transactions.", "2. Add WHERE transactions.id IS NULL to find merchants with no trades."]},
                    {"type": "reflection", "question": "Why do we use `IS NULL` instead of `= NULL` when checking for missing matches?"},
                    {"type": "debugger", "title": "Null Handling", "scenario": "A LEFT JOIN query is missing rows it should have.", "options": ["Used INNER JOIN by mistake", "Put a right-table condition in the WHERE clause instead of ON", "Both"], "answer": "Put a right-table condition in the WHERE clause instead of ON", "explanation": "Filtering the right table in the WHERE clause turns a LEFT JOIN into an INNER JOIN because NULLs fail the WHERE condition."},
                    {"type": "sql_sandbox", "title": "Find Idle Merchants", "context": "Use a LEFT JOIN to list ALL merchants, and their transaction amounts (which will be NULL for idle ones).", "init_script": "CREATE TABLE m (id INT, name TEXT); CREATE TABLE t (merchant_id INT, amount INT); INSERT INTO m VALUES (1, 'Sal'), (2, 'Boz'); INSERT INTO t VALUES (1, 500);", "solution_query": "SELECT m.name, t.amount FROM m LEFT JOIN t ON m.id = t.merchant_id;", "hint": "SELECT ... FROM m LEFT JOIN t ON m.id = t.merchant_id", "explanation": "Boz shows up with a NULL amount."}
                ]
            },
            {
                "title": "Module 3: GROUP BY and Aggregations",
                "blocks": [
                    {"type": "story", "title": "The Grand Totals", "text": "The ledger is too vast. 'I don't need every transaction,' the Guild Master barks. 'I need the TOTAL gold each merchant has traded!'"},
                    {"type": "problem", "text": "We need to collapse multiple rows into summary rows based on a specific category."},
                    {"type": "concept", "title": "GROUP BY", "explanation": "GROUP BY groups rows that have the same values in specified columns into summary rows, usually to perform aggregate functions (SUM, COUNT, AVG).", "analogy": "Sorting a giant jar of coins into piles of pennies, nickels, and dimes, then counting the total in each pile.", "technical_explanation": "The database engine sorts/hashes the data by the grouping column, then applies the aggregate function to each bucket.", "why_it_matters": "The foundation of all data analysis and reporting.", "remember": "Aggregate the rest, GROUP BY the best."},
                    {"type": "visual", "visual_type": "text", "data": "Rows: (A, 10), (A, 20), (B, 5)\nGROUP BY Name, SUM(Val)\nResult: (A, 30), (B, 5)"},
                    {"type": "worked_example", "title": "Summing Transactions", "steps": ["1. SELECT merchant_id, SUM(amount).", "2. FROM transactions.", "3. GROUP BY merchant_id."]},
                    {"type": "reflection", "question": "What happens if you SELECT a column that is not in the GROUP BY and not in an aggregate function?"},
                    {"type": "micro_challenge", "question": "Which function counts the number of rows in a group?", "options": ["SUM()", "COUNT()", "TOTAL()"], "answer": "COUNT()", "explanation": "COUNT() tallies the rows, SUM() adds up numeric values."},
                    {"type": "sql_sandbox", "title": "Calculate Totals", "context": "Get the `merchant_id` and the SUM of `amount` for each merchant.", "init_script": "CREATE TABLE t (merchant_id INT, amount INT); INSERT INTO t VALUES (1, 100), (1, 200), (2, 50);", "solution_query": "SELECT merchant_id, SUM(amount) FROM t GROUP BY merchant_id;", "hint": "Use SUM(amount) and GROUP BY merchant_id.", "explanation": "Merchant 1 correctly shows 300."}
                ]
            },
            {
                "title": "Module 4: HAVING vs WHERE",
                "blocks": [
                    {"type": "story", "title": "The Elite Merchants", "text": "'Excellent,' says the Master. 'Now, show me ONLY the merchants whose total trade volume exceeds 10,000 gold.'"},
                    {"type": "problem", "text": "We cannot use WHERE to filter by an aggregate sum, because WHERE filters rows *before* aggregation."},
                    {"type": "concept", "title": "HAVING Clause", "explanation": "HAVING is used to filter groups *after* the GROUP BY and aggregations have been calculated.", "analogy": "WHERE is the bouncer at the club door (filters individuals). HAVING is kicking out a VIP table if their total bill isn't high enough (filters groups).", "technical_explanation": "SQL Order of Execution: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT. Therefore, HAVING can see aggregate results.", "why_it_matters": "Essential for filtering based on totals, averages, or counts.", "remember": "WHERE before grouping, HAVING after."},
                    {"type": "visual", "visual_type": "text", "data": "WHERE amount > 100 (filters raw rows)\nHAVING SUM(amount) > 10000 (filters summary rows)"},
                    {"type": "worked_example", "title": "Filtering Groups", "steps": ["1. Write the GROUP BY query.", "2. Append HAVING SUM(amount) > 10000."]},
                    {"type": "reflection", "question": "Can you use both WHERE and HAVING in the same query?"},
                    {"type": "debugger", "title": "Execution Order Error", "scenario": "A query `WHERE SUM(amount) > 100` throws an error.", "options": ["Change WHERE to HAVING", "Remove GROUP BY", "Change SUM to COUNT"], "answer": "Change WHERE to HAVING", "explanation": "Aggregate functions cannot be evaluated in the WHERE clause."},
                    {"type": "sql_sandbox", "title": "Find the Elite", "context": "Select `merchant_id` and `SUM(amount)` where the total sum is strictly greater than 200.", "init_script": "CREATE TABLE t (merchant_id INT, amount INT); INSERT INTO t VALUES (1, 100), (1, 150), (2, 50);", "solution_query": "SELECT merchant_id, SUM(amount) FROM t GROUP BY merchant_id HAVING SUM(amount) > 200;", "hint": "Use HAVING SUM(amount) > 200 after your GROUP BY.", "explanation": "Only merchant 1 (250) is returned."}
                ]
            },
            {
                "title": "Module 5: Window Functions: OVER and PARTITION BY",
                "blocks": [
                    {"type": "story", "title": "The Running Ledger", "text": "A dark conspiracy is afoot. We need to see every transaction alongside the merchant's running total, without collapsing the rows!"},
                    {"type": "problem", "text": "GROUP BY collapses rows. We want to see aggregate data (like a total) appended to *every individual row*."},
                    {"type": "concept", "title": "Window Functions", "explanation": "Window functions perform calculations across a set of table rows related to the current row, but unlike aggregate functions, they do not cause rows to become grouped into a single output row.", "analogy": "Looking through a moving window at a specific subset of data, calculating a stat for that window, and writing it down next to the current row.", "technical_explanation": "Uses the `OVER()` clause. `PARTITION BY` defines the window (like GROUP BY). `ORDER BY` within the window defines running totals.", "why_it_matters": "Crucial for running totals, rankings, and moving averages.", "remember": "Aggregate power, row-level detail."},
                    {"type": "visual", "visual_type": "text", "data": "SELECT id, amount, SUM(amount) OVER (PARTITION BY merchant_id) as total_for_merchant"},
                    {"type": "worked_example", "title": "A Simple Window", "steps": ["1. Write a normal SELECT.", "2. Add a window function: SUM(amount) OVER (PARTITION BY merchant_id)."]},
                    {"type": "reflection", "question": "How does `PARTITION BY` differ from `GROUP BY`?"},
                    {"type": "micro_challenge", "question": "Which clause is used to define a window function?", "options": ["GROUP BY", "OVER", "WINDOW"], "answer": "OVER", "explanation": "The OVER clause dictates how the window is partitioned and ordered."},
                    {"type": "sql_sandbox", "title": "Append the Totals", "context": "Select `id`, `amount`, and the total amount for that merchant using a window function.", "init_script": "CREATE TABLE t (id INT, m_id INT, amount INT); INSERT INTO t VALUES (1, 1, 10), (2, 1, 20), (3, 2, 50);", "solution_query": "SELECT id, amount, SUM(amount) OVER (PARTITION BY m_id) FROM t;", "hint": "Use SUM(amount) OVER (PARTITION BY m_id)", "explanation": "Rows 1 and 2 now both show 30 as their partition total."}
                ]
            },
            {
                "title": "Module 6: Common Table Expressions (CTEs)",
                "blocks": [
                    {"type": "story", "title": "The Complex Web", "text": "The queries are becoming monstrous. Nested subqueries make the ledger unreadable. The ancient monks used a technique to name their intermediate steps."},
                    {"type": "problem", "text": "Complex queries with multiple subqueries are hard to read, maintain, and sometimes optimize."},
                    {"type": "concept", "title": "CTEs (WITH clause)", "explanation": "A CTE provides a temporary result set that you can reference within another SELECT, INSERT, UPDATE, or DELETE statement.", "analogy": "Defining variables at the top of a math problem before solving the final equation.", "technical_explanation": "Introduced using the `WITH` keyword. Improves readability by breaking complex logic into manageable, named blocks.", "why_it_matters": "Massively improves SQL readability and allows for recursive queries.", "remember": "WITH CTE_Name AS (...)"},
                    {"type": "visual", "visual_type": "text", "data": "WITH EliteMerchants AS (\n  SELECT id FROM merchants WHERE status='elite'\n)\nSELECT * FROM EliteMerchants;"},
                    {"type": "worked_example", "title": "Writing a CTE", "steps": ["1. Start with WITH cte_name AS (query).", "2. Follow immediately with a SELECT that uses cte_name."]},
                    {"type": "reflection", "question": "Are CTEs permanently stored in the database?"},
                    {"type": "debugger", "title": "CTE Scope", "scenario": "You define a CTE and try to use it in two separate queries separated by a semicolon.", "options": ["It works fine", "It fails on the second query"], "answer": "It fails on the second query", "explanation": "A CTE only exists for the duration of the single query statement immediately following it."},
                    {"type": "sql_sandbox", "title": "Clean up with CTE", "context": "Use a CTE named `RichMerchants` to find merchants with `amount > 100`, then SELECT * from it.", "init_script": "CREATE TABLE t (id INT, amount INT); INSERT INTO t VALUES (1, 50), (2, 500);", "solution_query": "WITH RichMerchants AS (SELECT * FROM t WHERE amount > 100) SELECT * FROM RichMerchants;", "hint": "WITH RichMerchants AS (...) SELECT * FROM RichMerchants;", "explanation": "CTEs make your intermediate steps explicit and readable."}
                ]
            },
            {
                "title": "Module 7: UNION and Set Operations",
                "blocks": [
                    {"type": "story", "title": "The Shadow Ledger", "text": "You find a second ledger, hidden beneath a floorboard! It has the same structure as the first. We must combine the rows of both ledgers into one massive list."},
                    {"type": "problem", "text": "We need to vertically stack results from two different queries, not join them horizontally."},
                    {"type": "concept", "title": "UNION", "explanation": "UNION combines the result sets of two or more SELECT statements into a single column set. It automatically removes duplicates.", "analogy": "Pouring two different bags of M&Ms into a single bowl.", "technical_explanation": "Both queries must return the same number of columns, with compatible data types in the same order. `UNION ALL` keeps duplicates.", "why_it_matters": "Essential for aggregating data spread across identical tables (e.g., archived vs active data).", "remember": "UNION stacks vertically, JOIN merges horizontally."},
                    {"type": "visual", "visual_type": "text", "data": "Query 1: (A), (B)\nUNION\nQuery 2: (B), (C)\nResult: (A), (B), (C)"},
                    {"type": "worked_example", "title": "Stacking Ledgers", "steps": ["1. SELECT col1 FROM table1", "2. UNION", "3. SELECT col1 FROM table2"]},
                    {"type": "reflection", "question": "Why is `UNION ALL` faster than `UNION`?"},
                    {"type": "micro_challenge", "question": "What is required for a UNION to work?", "options": ["Tables must have a foreign key", "Queries must have the same number of columns", "Both tables must have the same name"], "answer": "Queries must have the same number of columns", "explanation": "The columns must align perfectly for the stacking to work."},
                    {"type": "sql_sandbox", "title": "Combine Ledgers", "context": "Combine the `id` columns from `ledger1` and `ledger2` using UNION ALL.", "init_script": "CREATE TABLE ledger1 (id INT); CREATE TABLE ledger2 (id INT); INSERT INTO ledger1 VALUES (1), (2); INSERT INTO ledger2 VALUES (2), (3);", "solution_query": "SELECT id FROM ledger1 UNION ALL SELECT id FROM ledger2;", "hint": "SELECT id FROM ledger1 UNION ALL ...", "explanation": "UNION ALL kept the duplicate '2'."}
                ]
            },
            {
                "title": "Module 8: Indexing and Final Conspiracy Challenge",
                "blocks": [
                    {"type": "story", "title": "The Slow Reveal", "text": "We have 200,000 rows. Searching for the conspirator's ID (ID = 99999) takes too long. The Master demands instant results!"},
                    {"type": "problem", "text": "Sequential scanning of a massive table is slow O(N). We need O(log N) lookup."},
                    {"type": "concept", "title": "Indexes", "explanation": "An index is a data structure (usually a B-Tree) that improves the speed of data retrieval operations on a table at the cost of additional storage and slower writes.", "analogy": "The index at the back of a textbook. Instead of reading every page to find a topic, you look it up in the back and jump straight to the page.", "technical_explanation": "Creates a sorted auxiliary structure containing the indexed column and a pointer to the physical row.", "why_it_matters": "The primary tool for database performance optimization.", "remember": "Fast reads, slow writes."},
                    {"type": "visual", "visual_type": "text", "data": "Table Scan: Check row 1, row 2... row 200,000.\nIndex Seek: Root -> Branch -> Leaf (3 steps)."},
                    {"type": "worked_example", "title": "Creating an Index", "steps": ["1. CREATE INDEX idx_merchant_id ON transactions (merchant_id);"]},
                    {"type": "reflection", "question": "Why shouldn't you put an index on every single column?"},
                    {"type": "debugger", "title": "Index Choice", "scenario": "A query filters by `last_name` and `first_name`. You create an index on `first_name`.", "options": ["Perfect", "Index should be on last_name, first_name"], "answer": "Index should be on last_name, first_name", "explanation": "Composite indexes work left-to-right. If you search by last_name primarily, it must be the leading column in the index."},
                    {"type": "sql_sandbox", "title": "Final Challenge: Uncover the Conspiracy", "context": "Create an index on `amount` in the `ledger` table, then select the ID where amount is 9999.", "init_script": "CREATE TABLE ledger (id INT, amount INT); INSERT INTO ledger VALUES (1, 100), (2, 9999);", "solution_query": "CREATE INDEX idx_amount ON ledger(amount);\nSELECT id FROM ledger WHERE amount = 9999;", "hint": "CREATE INDEX name ON table(column); then run your SELECT.", "explanation": "The index allowed the database to instantly find the conspirator's transaction."}
                ]
            }
        ]
    }

def get_case_6():
    return {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: Wildfire & The Need for Transactions",
                "blocks": [
                    {"type": "story", "title": "The Spreading Blaze", "text": "A massive wildfire is spreading towards the city. Fire command, police, and transit authorities are all desperately updating the central Evacuation Route database at the exact same time."},
                    {"type": "problem", "text": "Concurrent updates are corrupting data. Police mark a route 'Open' exactly when Fire marks it 'Blocked', resulting in chaotic overrides."},
                    {"type": "concept", "title": "Database Transactions", "explanation": "A transaction is a logical unit of work that contains one or more SQL statements. It must succeed completely or fail completely.", "analogy": "A bank transfer. Taking money from Account A and giving it to Account B must both happen, or neither happens. You can't just do half.", "technical_explanation": "Transactions ensure data integrity by bundling operations. Managed with BEGIN, COMMIT, and ROLLBACK.", "why_it_matters": "Prevents partial updates from leaving the database in an inconsistent state.", "remember": "All or nothing."},
                    {"type": "visual", "visual_type": "text", "data": "BEGIN;\nUPDATE Route A;\nUPDATE Route B;\nCOMMIT; (or ROLLBACK;)"},
                    {"type": "worked_example", "title": "A Safe Update", "steps": ["1. BEGIN TRANSACTION;", "2. Execute updates.", "3. COMMIT;"]},
                    {"type": "reflection", "question": "What happens if the server crashes right after the first UPDATE but before the COMMIT?"},
                    {"type": "micro_challenge", "question": "Which command cancels a transaction?", "options": ["CANCEL", "ROLLBACK", "ABORT"], "answer": "ROLLBACK", "explanation": "ROLLBACK undoes all changes made during the current transaction."},
                    {"type": "sql_sandbox", "title": "Safe Route Update", "context": "Wrap the update of route 1 to 'Blocked' in a transaction.", "init_script": "CREATE TABLE routes (id INT, status TEXT); INSERT INTO routes VALUES (1, 'Open');", "solution_query": "BEGIN;\nUPDATE routes SET status = 'Blocked' WHERE id = 1;\nCOMMIT;", "hint": "BEGIN; UPDATE ... COMMIT;", "explanation": "The transaction ensured the update was atomic."}
                ]
            },
            {
                "title": "Module 2: ACID Properties",
                "blocks": [
                    {"type": "story", "title": "The Four Pillars", "text": "The Chief Engineer arrives. 'If this system goes down during the evacuation, we lose lives. The database must be ACID compliant!'"},
                    {"type": "problem", "text": "We need a strict set of guarantees for transaction reliability."},
                    {"type": "concept", "title": "ACID", "explanation": "Atomicity (All or nothing), Consistency (Follows all rules/constraints), Isolation (Transactions don't interfere), Durability (Committed data survives crashes).", "analogy": "Atomicity = Marriage (both say yes, or it fails). Consistency = The paperwork is legal. Isolation = Private ceremony. Durability = The marriage certificate is in a fireproof safe.", "technical_explanation": "These four properties guarantee that database transactions are processed reliably.", "why_it_matters": "The core fundamental theory of relational database design.", "remember": "Atomicity, Consistency, Isolation, Durability."},
                    {"type": "visual", "visual_type": "text", "data": "A - Atomic (Indivisible)\nC - Consistent (Valid state to Valid state)\nI - Isolated (Invisible to others until commit)\nD - Durable (Saved to disk)"},
                    {"type": "worked_example", "title": "Identifying ACID Violations", "steps": ["1. A crash loses data? Durability violation.", "2. Half a transfer completes? Atomicity violation."]},
                    {"type": "reflection", "question": "If a transaction violates a FOREIGN KEY constraint and is rolled back, which ACID property caused the rollback?"},
                    {"type": "debugger", "title": "ACID Match", "scenario": "A power outage occurs, but upon reboot, the last committed transaction is still there.", "options": ["Atomicity", "Durability", "Isolation"], "answer": "Durability", "explanation": "Durability guarantees that once committed, data survives hardware or power failures."},
                    {"type": "sql_sandbox", "title": "Constraint Consistency", "context": "Try to insert a NULL into a NOT NULL column to see Consistency block the transaction.", "init_script": "CREATE TABLE safe (id INT NOT NULL);", "solution_query": "INSERT INTO safe VALUES (1);", "hint": "Just insert a valid integer to pass.", "explanation": "If you tried NULL, it would fail, protecting Consistency."}
                ]
            },
            {
                "title": "Module 3: Concurrency Issues: Dirty Reads",
                "blocks": [
                    {"type": "story", "title": "The Phantom Clear", "text": "Police checked a route and saw it marked 'Clear'. They sent civilians. But Fire Command had just marked it 'Clear' temporarily, then rolled it back to 'Blocked'! The police read uncommitted data!"},
                    {"type": "problem", "text": "Reading data from a transaction that hasn't committed yet (Dirty Read)."},
                    {"type": "concept", "title": "Dirty Reads & Non-repeatable Reads", "explanation": "Dirty Read: Reading uncommitted changes. Non-repeatable Read: Reading a row, another transaction updates it and commits, you read it again and it changed.", "analogy": "Dirty Read is reading someone's rough draft of an email before they send it. They might delete it entirely.", "technical_explanation": "Occurs when isolation levels are too low. It prioritizes speed over accuracy.", "why_it_matters": "Causes catastrophic real-world decision errors based on phantom data.", "remember": "Dirty = Uncommitted."},
                    {"type": "visual", "visual_type": "text", "data": "T1: UPDATE route (uncommitted)\nT2: SELECT route (reads new value! DIRTY)\nT1: ROLLBACK (the value T2 read never truly existed)"},
                    {"type": "worked_example", "title": "The Danger Zone", "steps": ["1. T1 starts.", "2. T1 updates X.", "3. T2 reads X.", "4. T1 rolls back. T2's data is invalid."]},
                    {"type": "reflection", "question": "Why might a database allow dirty reads at all?"},
                    {"type": "micro_challenge", "question": "What concurrency issue involves reading the same row twice in a transaction and getting two different committed values?", "options": ["Dirty Read", "Non-repeatable Read", "Phantom Read"], "answer": "Non-repeatable Read", "explanation": "Because another transaction committed an update between your two reads."},
                    {"type": "sql_sandbox", "title": "Observe the Rollback", "context": "Start a transaction, update `status` to 'Blocked', then ROLLBACK.", "init_script": "CREATE TABLE routes (id INT, status TEXT); INSERT INTO routes VALUES (1, 'Open');", "solution_query": "BEGIN;\nUPDATE routes SET status = 'Blocked';\nROLLBACK;\nSELECT * FROM routes;", "hint": "BEGIN; UPDATE ... ROLLBACK; SELECT ...", "explanation": "The status remains 'Open'. Anyone who read 'Blocked' during the transaction would have had a Dirty Read."}
                ]
            },
            {
                "title": "Module 4: Isolation Levels",
                "blocks": [
                    {"type": "story", "title": "Locking Down the Grid", "text": "'We must prevent these dirty reads!' the Chief yells. 'Adjust the database isolation level immediately!'"},
                    {"type": "problem", "text": "We need to configure the database engine's strictness regarding concurrency."},
                    {"type": "concept", "title": "Isolation Levels", "explanation": "Read Uncommitted (allows dirty reads), Read Committed (prevents dirty reads), Repeatable Read (prevents non-repeatable reads), Serializable (prevents all anomalies, including phantoms).", "analogy": "Read Uncommitted = Peeking through the window. Serializable = Waiting in line for a private room.", "technical_explanation": "Higher isolation = higher data safety but lower concurrency (slower, more locking).", "why_it_matters": "The classic tradeoff between performance and accuracy in databases.", "remember": "Serializable is safest, but slowest."},
                    {"type": "visual", "visual_type": "text", "data": "Isolation | Dirty Read | Non-Repeatable | Phantom\nUncommitted | YES | YES | YES\nCommitted   | NO  | YES | YES\nRepeatable  | NO  | NO  | YES\nSerializable| NO  | NO  | NO"},
                    {"type": "worked_example", "title": "Setting Isolation", "steps": ["1. SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;", "2. BEGIN TRANSACTION;"]},
                    {"type": "reflection", "question": "Why is 'Read Committed' the default for many modern databases?"},
                    {"type": "debugger", "title": "Select the Level", "scenario": "You need to run a financial report and ensure no data changes while you sum the columns.", "options": ["Read Uncommitted", "Serializable"], "answer": "Serializable", "explanation": "Serializable ensures a perfectly consistent snapshot with no interference."},
                    {"type": "sql_sandbox", "title": "Syntax Check", "context": "Although SQLite sandbox limits this, write a query that SELECTs everything from routes.", "init_script": "CREATE TABLE routes (id INT, status TEXT); INSERT INTO routes VALUES (1, 'Open');", "solution_query": "SELECT * FROM routes;", "hint": "SELECT * FROM routes;", "explanation": "In a real database, you'd use SET TRANSACTION ISOLATION LEVEL before this."}
                ]
            },
            {
                "title": "Module 5: Locks & 2-Phase Locking (2PL)",
                "blocks": [
                    {"type": "story", "title": "Holding the Key", "text": "To achieve isolation, the database uses locks. Fire Command locks a route record so Police can't touch it until Fire is done."},
                    {"type": "problem", "text": "How does the database physically enforce isolation?"},
                    {"type": "concept", "title": "Locks and 2PL", "explanation": "Shared (Read) Locks allow others to read but not write. Exclusive (Write) Locks prevent others from reading or writing. Two-Phase Locking (2PL) means a transaction acquires all locks it needs (Growing Phase) and then releases them (Shrinking Phase), never acquiring a lock after releasing one.", "analogy": "Exclusive Lock: Locking the bathroom door. Shared Lock: Looking at a painting in a museum (others can look, no one can alter it).", "technical_explanation": "2PL guarantees serializability by preventing conflicts.", "why_it_matters": "Understanding locks helps debug blocked queries and performance bottlenecks.", "remember": "Write locks block everything."},
                    {"type": "visual", "visual_type": "text", "data": "T1 (Write Lock on A) ---> T2 (Requests Read Lock on A) -> BLOCKED until T1 commits."},
                    {"type": "worked_example", "title": "Locking behavior", "steps": ["1. T1: UPDATE A (Exclusive Lock).", "2. T2: SELECT A (Blocked).", "3. T1: COMMIT (Lock released). T2 proceeds."]},
                    {"type": "reflection", "question": "Why does a Write lock block Read locks?"},
                    {"type": "micro_challenge", "question": "In 2PL, can a transaction acquire a new lock after it has released an old lock?", "options": ["Yes", "No"], "answer": "No", "explanation": "2PL enforces a strict growing phase (acquiring) followed by a shrinking phase (releasing)."},
                    {"type": "sql_sandbox", "title": "Simulate a Lock (Conceptual)", "context": "Just run a basic UPDATE. In the real world, this acquires an Exclusive lock.", "init_script": "CREATE TABLE routes (id INT); INSERT INTO routes VALUES (1);", "solution_query": "UPDATE routes SET id = 2;", "hint": "UPDATE routes SET id = 2;", "explanation": "The database silently locked the row to do this."}
                ]
            },
            {
                "title": "Module 6: Deadlocks",
                "blocks": [
                    {"type": "story", "title": "The Standoff", "text": "Fire Command has Route A and needs Route B. Police has Route B and needs Route A. Both are waiting. Neither will yield. The system is frozen!"},
                    {"type": "problem", "text": "Two or more transactions are permanently blocking each other."},
                    {"type": "concept", "title": "Deadlock", "explanation": "A deadlock occurs when two transactions each hold a lock that the other needs. The database engine must intervene, kill one transaction (the victim), and roll it back.", "analogy": "Two cars meet on a narrow one-lane bridge. Neither can move forward until the other backs up.", "technical_explanation": "Databases use cycle-detection algorithms in their lock manager to find deadlocks.", "why_it_matters": "A common cause of random application errors. Requires application-side retry logic.", "remember": "Circular wait."},
                    {"type": "visual", "visual_type": "text", "data": "T1 locks A, requests B.\nT2 locks B, requests A.\nDEADLOCK!"},
                    {"type": "worked_example", "title": "Deadlock Resolution", "steps": ["1. DB detects cycle.", "2. DB kills T2.", "3. T1 proceeds.", "4. App receives error for T2 and must retry."]},
                    {"type": "reflection", "question": "How can an application prevent deadlocks structurally?"},
                    {"type": "debugger", "title": "Deadlock Avoidance", "scenario": "Your code frequently deadlocks.", "options": ["Use NO LOCK", "Always update tables in the exact same order"], "answer": "Always update tables in the exact same order", "explanation": "If all transactions lock A before locking B, cycles cannot form."},
                    {"type": "sql_sandbox", "title": "Deadlock Awareness", "context": "We can't trigger a true deadlock in this sandbox. Write a query to update route A (id=1) then route B (id=2) sequentially.", "init_script": "CREATE TABLE r (id INT, val TEXT); INSERT INTO r VALUES (1, 'A'), (2, 'B');", "solution_query": "BEGIN;\nUPDATE r SET val = 'X' WHERE id = 1;\nUPDATE r SET val = 'Y' WHERE id = 2;\nCOMMIT;", "hint": "Wrap two updates in a transaction.", "explanation": "Consistent ordering prevents deadlocks."}
                ]
            },
            {
                "title": "Module 7: Recovery and Write-Ahead Logging (WAL)",
                "blocks": [
                    {"type": "story", "title": "The Power Outage", "text": "Boom! The command center loses power. When the servers reboot, the Chief panics. 'Did we lose the evacuation routes?!'"},
                    {"type": "problem", "text": "How does a database guarantee Durability and Atomicity across hardware crashes?"},
                    {"type": "concept", "title": "Write-Ahead Logging (WAL)", "explanation": "Before changing the actual database file, the database engine writes a record of the intended change to a sequential log file. If a crash occurs, the database replays the log to recover.", "analogy": "Writing down 'I am going to pay Bob $50' in a ledger BEFORE actually handing Bob the money.", "technical_explanation": "Ensures atomicity and durability. Uncommitted transactions in the log are ignored on reboot (Atomicity). Committed transactions not yet written to the main data file are replayed (Durability).", "why_it_matters": "The magic behind crash recovery.", "remember": "Log it before you do it."},
                    {"type": "visual", "visual_type": "text", "data": "1. App requests UPDATE.\n2. DB writes to WAL (disk).\n3. DB replies 'Success'.\n4. DB slowly updates actual data file."},
                    {"type": "worked_example", "title": "Crash Recovery", "steps": ["1. DB Boots.", "2. Reads WAL.", "3. Re-applies committed changes.", "4. Discards uncommitted changes."]},
                    {"type": "reflection", "question": "Why write to the log first instead of just writing directly to the data file?"},
                    {"type": "micro_challenge", "question": "What is the primary purpose of WAL?", "options": ["Faster queries", "Crash recovery and Durability", "Preventing dirty reads"], "answer": "Crash recovery and Durability", "explanation": "WAL is specifically designed to survive unexpected crashes."},
                    {"type": "sql_sandbox", "title": "Commit the Change", "context": "Commit an update. Conceptually, this is when the WAL syncs to disk.", "init_script": "CREATE TABLE t (id INT); INSERT INTO t VALUES (1);", "solution_query": "BEGIN;\nUPDATE t SET id = 2;\nCOMMIT;", "hint": "BEGIN; UPDATE; COMMIT;", "explanation": "Upon COMMIT, the WAL guarantees this change survives a crash."}
                ]
            },
            {
                "title": "Module 8: Final Coordination Challenge",
                "blocks": [
                    {"type": "story", "title": "The Final Push", "text": "The fire is contained. We need to execute one massive, safe transaction to move all 'Evacuating' sectors to 'Safe', ensuring no partial updates occur."},
                    {"type": "problem", "text": "Execute a flawless transaction integrating DML."},
                    {"type": "concept", "title": "Transaction Mastery", "explanation": "Putting it all together. A well-formed transaction guarantees ACID properties and protects the system.", "analogy": "The final synchronized movement of a symphony orchestra.", "technical_explanation": "Requires BEGIN, the correct UPDATE statement, and a COMMIT.", "why_it_matters": "This is how all modern applications interact safely with databases.", "remember": "Trust the transaction."},
                    {"type": "visual", "visual_type": "text", "data": "[BEGIN] ---> [UPDATE] ---> [COMMIT] ---> (SAFE)"},
                    {"type": "worked_example", "title": "The Final Script", "steps": ["1. Open transaction.", "2. Execute DML.", "3. Close transaction."]},
                    {"type": "reflection", "question": "How has learning about ACID changed how you will write backend code?"},
                    {"type": "debugger", "title": "Missing Keyword", "scenario": "Your code has `UPDATE...` followed by `COMMIT;` but it throws an error.", "options": ["Missing BEGIN", "Missing ROLLBACK"], "answer": "Missing BEGIN", "explanation": "You cannot commit a transaction that was never explicitly started (in explicit transaction mode)."},
                    {"type": "sql_sandbox", "title": "Secure the Sectors", "context": "Start a transaction, update all rows where status is 'Evacuating' to 'Safe', and commit.", "init_script": "CREATE TABLE sectors (id INT, status TEXT); INSERT INTO sectors VALUES (1, 'Evacuating'), (2, 'Evacuating'), (3, 'Clear');", "solution_query": "BEGIN;\nUPDATE sectors SET status = 'Safe' WHERE status = 'Evacuating';\nCOMMIT;", "hint": "BEGIN; UPDATE sectors SET status = 'Safe' WHERE status = 'Evacuating'; COMMIT;", "explanation": "You safely updated the database. The city is safe!"}
                ]
            }
        ]
    }

NEW_LEVELS = {
    "4": get_case_4(),
    "5": get_case_5(),
    "6": get_case_6()
}
