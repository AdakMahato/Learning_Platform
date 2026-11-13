NEW_LEVELS = {
    "1": {
        "format": "episodic",
        "episodes": [
            {
                "title": "Module 1: The Chaos of Nexora",
                "blocks": [
                    {"type": "story", "title": "Nexora's Fragmented Mind", "text": "Nexora controls hospitals, trains, and banks. Every department keeps its own records in isolation. Train schedules don't know bank holidays, and hospitals don't know train delays. The city is grinding to a halt."},
                    {"type": "problem", "text": "You must build the database that connects all of Nexora's systems into a single, unified source of truth."},
                    {"type": "concept", "title": "What is a Relational Database?", "explanation": "A relational database organizes data into tables (relations) which can be linked—or related—based on data common to each.", "analogy": "Think of it as a meticulously organized filing cabinet where every folder has a cross-reference tag to other relevant folders, instead of just tossing papers into a box.", "technical_explanation": "Relational databases use the Relational Model introduced by E.F. Codd in 1970, which abstracts data into tuples (rows) and attributes (columns).", "why_it_matters": "Without it, Nexora suffers from data redundancy and inconsistency.", "remember": "Tables are for entities; relationships connect them."},
                    {"type": "visual", "visual_type": "text", "data": "+-----------+       +-----------+\n| Hospital  |       | Train     |\n+-----------+       +-----------+\n| PatientID |<------| Passenger |\n+-----------+       +-----------+"}
                ]
            },
            {
                "title": "Module 2: Creating the Foundation",
                "blocks": [
                    {"type": "concept", "title": "Tables and Data Types", "explanation": "To store data, you must define its structure using Data Definition Language (DDL).", "analogy": "Like pouring concrete for a building's foundation, you must specify the exact dimensions before building.", "technical_explanation": "CREATE TABLE defines the schema. Data types (INT, VARCHAR) enforce domain constraints.", "why_it_matters": "Prevents invalid data (like text in a number field) from entering the system.", "remember": "Schema first, data later."},
                    {"type": "worked_example", "title": "Defining a Hospital Record", "steps": ["Identify attributes: name, age, blood_type.", "Choose types: VARCHAR, INT, VARCHAR.", "Write the CREATE TABLE statement."]},
                    {"type": "sql_sandbox", "title": "Build the Patient Table", "context": "Nexora's Central Hospital needs a table to store patient demographics.", "init_script": "", "solution_query": "CREATE TABLE patients (id INT, name VARCHAR(100), age INT);", "hint": "Use CREATE TABLE patients (...) with id, name, and age.", "explanation": "This establishes the structure for all future patient records."}
                ]
            },
            {
                "title": "Module 3: Entering Data",
                "blocks": [
                    {"type": "concept", "title": "Inserting Records", "explanation": "Once a table exists, Data Manipulation Language (DML) is used to populate it.", "analogy": "The foundation is laid; now you are moving the furniture in.", "technical_explanation": "The INSERT statement adds new tuples to a relation.", "why_it_matters": "A database without data is just an empty shell.", "remember": "Match the column order in your INSERT statement."},
                    {"type": "micro_challenge", "question": "What happens if you omit a column during INSERT without providing a DEFAULT?", "options": ["It crashes", "It inserts NULL", "It inserts 0"], "answer": "It inserts NULL", "explanation": "Unless constrained otherwise, missing values default to NULL."},
                    {"type": "sql_sandbox", "title": "Registering the First Patient", "context": "Patient 'Ada' is 25 years old. Add her to the system.", "init_script": "CREATE TABLE patients (id INT, name VARCHAR(100), age INT);", "solution_query": "INSERT INTO patients (id, name, age) VALUES (1, 'Ada', 25);", "hint": "Use INSERT INTO ... VALUES ...", "explanation": "You've successfully added a tuple to the relation."}
                ]
            },
            {
                "title": "Module 4: Retrieving the Truth",
                "blocks": [
                    {"type": "concept", "title": "The SELECT Statement", "explanation": "Data retrieval is done via queries.", "analogy": "Like a search engine for your structured data.", "technical_explanation": "SELECT defines the projection (columns), FROM specifies the relation, and WHERE applies a selection filter (rows).", "why_it_matters": "Querying is the primary way applications interact with databases.", "remember": "SELECT filters columns, WHERE filters rows."},
                    {"type": "visual", "visual_type": "text", "data": "SELECT name -- PROJECTION\nFROM patients -- RELATION\nWHERE age > 20 -- SELECTION"},
                    {"type": "sql_sandbox", "title": "Find Adult Patients", "context": "The hospital needs a list of all patients over 18.", "init_script": "CREATE TABLE patients (id INT, name VARCHAR(100), age INT); INSERT INTO patients VALUES (1, 'Ada', 25), (2, 'Bob', 12);", "solution_query": "SELECT name FROM patients WHERE age > 18;", "hint": "Use WHERE age > 18", "explanation": "The database engine filters the rows before returning the result."}
                ]
            },
            {
                "title": "Module 5: Ensuring Identity",
                "blocks": [
                    {"type": "concept", "title": "Primary Keys", "explanation": "A primary key uniquely identifies each record.", "analogy": "Like a fingerprint or a passport number, no two rows can have the same primary key.", "technical_explanation": "A PRIMARY KEY constraint automatically implies UNIQUE and NOT NULL.", "why_it_matters": "Without it, you cannot reliably update or delete specific records.", "remember": "Every table should have a primary key."},
                    {"type": "debugger", "title": "Duplicate Identity Crisis", "scenario": "You tried to insert two patients with ID=1, and the system threw an error.", "options": ["The system is out of memory", "Primary Key violation", "Syntax error"], "answer": "Primary Key violation", "explanation": "The PRIMARY KEY constraint enforces entity integrity."},
                    {"type": "sql_sandbox", "title": "Enforce Identity", "context": "Recreate the patients table, but this time make `id` the primary key.", "init_script": "", "solution_query": "CREATE TABLE patients (id INT PRIMARY KEY, name VARCHAR(100), age INT);", "hint": "Add PRIMARY KEY next to the id definition.", "explanation": "Now Nexora can never mix up two patients with the same name."}
                ]
            },
            {
                "title": "Module 6: Connecting the Dots",
                "blocks": [
                    {"type": "concept", "title": "Foreign Keys and JOINs", "explanation": "Foreign keys link tables together, and JOINs retrieve data across these links.", "analogy": "Like a bridge between two islands, a foreign key allows you to travel from one entity to another.", "technical_explanation": "A FOREIGN KEY references the PRIMARY KEY of another table, enforcing referential integrity. An INNER JOIN computes the Cartesian product and filters by the join condition.", "why_it_matters": "This is what makes a relational database 'relational'.", "remember": "Foreign keys enforce links; JOINs traverse them."},
                    {"type": "visual", "visual_type": "text", "data": "[Patients: id] <---- (Foreign Key) ---- [Visits: patient_id]"},
                    {"type": "sql_sandbox", "title": "Cross-Department Insight", "context": "Join patients with their hospital visits.", "init_script": "CREATE TABLE patients (id INT PRIMARY KEY, name VARCHAR); CREATE TABLE visits (id INT, patient_id INT); INSERT INTO patients VALUES (1, 'Ada'); INSERT INTO visits VALUES (101, 1);", "solution_query": "SELECT patients.name, visits.id FROM patients JOIN visits ON patients.id = visits.patient_id;", "hint": "JOIN visits ON patients.id = visits.patient_id", "explanation": "You've successfully unified data across Nexora's departments."}
                ]
            },
            {
                "title": "Module 7: The Train, The Bank, The Hospital",
                "blocks": [
                    {"type": "concept", "title": "Transactions and ACID", "explanation": "Transactions ensure that complex operations succeed or fail as a single unit.", "analogy": "Buying a train ticket: money leaves your bank, AND a seat is reserved. If one fails, both must fail.", "technical_explanation": "ACID properties: Atomicity, Consistency, Isolation, Durability. BEGIN TRANSACTION and COMMIT/ROLLBACK control this.", "why_it_matters": "Prevents catastrophic partial failures in critical systems like banking.", "remember": "All or nothing."},
                    {"type": "reflection", "question": "What would happen in Nexora if a bank transfer was not Atomic?"},
                    {"type": "debugger", "title": "The Ghost Ticket", "scenario": "A passenger's bank account was deducted, but no ticket was issued. What property failed?", "options": ["Atomicity", "Isolation", "Durability"], "answer": "Atomicity", "explanation": "Atomicity guarantees that all parts of the transaction complete, or none do."}
                ]
            },
            {
                "title": "Module 8: Final Investigation",
                "blocks": [
                    {"type": "concept", "title": "Indexes and Performance", "explanation": "Indexes speed up data retrieval at the cost of slower inserts.", "analogy": "Like an index at the back of a textbook, it saves you from reading every page.", "technical_explanation": "An index creates a B-Tree or Hash data structure for logarithmic time lookups instead of linear table scans.", "why_it_matters": "Nexora's database is growing; without indexes, queries will time out.", "remember": "Index the columns you search by, not every column."},
                    {"type": "sql_sandbox", "title": "Nexora Grand Unification", "context": "Nexora is fixed. For a final test, create an index on the patient's name to optimize search.", "init_script": "CREATE TABLE patients (id INT PRIMARY KEY, name VARCHAR(100));", "solution_query": "CREATE INDEX idx_name ON patients(name);", "hint": "CREATE INDEX index_name ON table(column);", "explanation": "Your database is now structurally sound and performant. Nexora thrives."}
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
                    {"type": "story", "title": "City of Paradoxes", "text": "A city blueprint contains buildings that cannot legally exist under its own rules. Doors that lead nowhere, addresses assigned to multiple properties. You must audit the design."},
                    {"type": "problem", "text": "Model the city's rules using Entity-Relationship (ER) concepts to find the structural flaws."},
                    {"type": "concept", "title": "Introduction to ER Modeling", "explanation": "Entity-Relationship modeling is a conceptual way to design databases before writing SQL.", "analogy": "It's the architectural blueprint of the database. You draw it before you pour the concrete.", "technical_explanation": "Entities represent objects; Attributes are properties; Relationships define interactions.", "why_it_matters": "Catching logical errors in the design phase is infinitely cheaper than fixing a live database.", "remember": "Design first, code second."}
                ]
            },
            {
                "title": "Module 2: Entities and Attributes",
                "blocks": [
                    {"type": "concept", "title": "Defining Entities", "explanation": "Entities are the nouns of your database.", "analogy": "In a city, 'Building' and 'Citizen' are entities. 'Tall' is an attribute.", "technical_explanation": "Entities become tables. Attributes become columns. Composite attributes can be broken down.", "why_it_matters": "Properly defining entities ensures you capture all necessary business requirements.", "remember": "Nouns = Entities, Adjectives = Attributes."},
                    {"type": "visual", "visual_type": "text", "data": "[ Building ]\n - Address (Key)\n - Floors\n - YearBuilt"},
                    {"type": "micro_challenge", "question": "Which of the following should be an Entity rather than an Attribute?", "options": ["Color", "Employee", "Age"], "answer": "Employee", "explanation": "An Employee is an object with its own properties, making it an Entity."}
                ]
            },
            {
                "title": "Module 3: Relationships and Cardinality",
                "blocks": [
                    {"type": "concept", "title": "Cardinality Limits", "explanation": "Cardinality defines how many instances of one entity can relate to instances of another.", "analogy": "A citizen can own multiple cars (1-to-Many), but a passport belongs to exactly one citizen (1-to-1).", "technical_explanation": "Common cardinalities are 1:1, 1:N, and M:N. Minimum cardinality defines mandatory vs optional participation.", "why_it_matters": "It dictates how foreign keys are placed and whether intermediary tables are needed.", "remember": "M:N requires a junction table."}
                ]
            },
            {
                "title": "Module 4: Constraints of Reality",
                "blocks": [
                    {"type": "concept", "title": "Domain Constraints", "explanation": "Constraints enforce business logic at the database level.", "analogy": "A building cannot have a negative number of floors.", "technical_explanation": "CHECK constraints allow arbitrary boolean expressions to validate row data on insert/update.", "why_it_matters": "Prevents the application layer from inserting logically impossible states.", "remember": "Push data integrity rules to the database."},
                    {"type": "sql_sandbox", "title": "Enforce Physics", "context": "Create a `buildings` table where `floors` must be greater than 0.", "init_script": "", "solution_query": "CREATE TABLE buildings (id INT PRIMARY KEY, floors INT CHECK (floors > 0));", "hint": "Use CHECK (floors > 0)", "explanation": "Now the database mathematically prohibits impossible buildings."}
                ]
            },
            {
                "title": "Module 5: Generalization",
                "blocks": [
                    {"type": "concept", "title": "Superclasses and Subclasses", "explanation": "Entities can have hierarchies, similar to object-oriented programming.", "analogy": "A 'Vehicle' is a superclass. 'Car' and 'Bicycle' are subclasses that inherit properties.", "technical_explanation": "Generalization extracts shared attributes into a super-entity. Sub-entities hold specific attributes.", "why_it_matters": "Reduces NULL values and structures data logically.", "remember": "Is-A relationships denote specialization."},
                    {"type": "debugger", "title": "The Overloaded Table", "scenario": "A table has 50 columns, but 40 are NULL for any given row because it stores both Residential and Commercial buildings.", "options": ["Needs an index", "Needs generalization", "Needs more RAM"], "answer": "Needs generalization", "explanation": "Splitting the table based on type solves the sparse data problem."}
                ]
            },
            {
                "title": "Module 6: Translating ER to Tables",
                "blocks": [
                    {"type": "concept", "title": "Logical Design", "explanation": "Translating an ER diagram into a relational schema.", "analogy": "Turning the blueprint into a step-by-step construction manual.", "technical_explanation": "Strong entities become tables. M:N relationships become their own tables with composite keys.", "why_it_matters": "This is the bridge between conceptual design and physical implementation.", "remember": "Every relationship must be represented as either a foreign key or a new table."},
                    {"type": "worked_example", "title": "Resolving M:N", "steps": ["Identify M:N between Citizens and Properties.", "Create table citizen_property.", "Add citizen_id and property_id as foreign keys.", "Make the combination of both the Primary Key."]}
                ]
            },
            {
                "title": "Module 7: Relational Algebra Foundations",
                "blocks": [
                    {"type": "concept", "title": "The Math Behind SQL", "explanation": "Relational algebra is the mathematical foundation of SQL queries.", "analogy": "It's the physics that makes the engineering (SQL) work.", "technical_explanation": "Operators like Sigma (Selection), Pi (Projection), and Join form the basis of query execution plans.", "why_it_matters": "Understanding it helps you write more efficient queries by visualizing how the database engine processes them.", "remember": "SQL is just a syntax for relational algebra."},
                    {"type": "reflection", "question": "Why does the database engine perform selection before a join when optimizing?"}
                ]
            },
            {
                "title": "Module 8: Final Blueprint Audit",
                "blocks": [
                    {"type": "sql_sandbox", "title": "Fix the Blueprint", "context": "Create a robust schema for a building that has a required address, and floors strictly greater than zero.", "init_script": "", "solution_query": "CREATE TABLE buildings (id INT PRIMARY KEY, address VARCHAR(200) NOT NULL, floors INT CHECK (floors > 0));", "hint": "Combine PRIMARY KEY, NOT NULL, and CHECK.", "explanation": "The city can now be built safely on logical foundations."}
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
                    {"type": "story", "title": "Fractured Memories", "text": "A neural implant contains multiple contradictory versions of one person's life. Addresses don't match zip codes, job titles don't match salaries. The data is corrupting the host's mind."},
                    {"type": "problem", "text": "You must normalize the database to eliminate anomalies and restore a single consistent memory."},
                    {"type": "concept", "title": "Data Anomalies", "explanation": "Unnormalized data suffers from Insert, Update, and Delete anomalies.", "analogy": "If you write your friend's new phone number in an address book, but forget to update the sticky note on your fridge, you have contradictory data.", "technical_explanation": "Anomalies occur when facts are stored in multiple places unnecessarily.", "why_it_matters": "Data integrity is impossible if facts can contradict themselves.", "remember": "One fact, one place."}
                ]
            },
            {
                "title": "Module 2: Functional Dependencies",
                "blocks": [
                    {"type": "concept", "title": "The Core of Normalization", "explanation": "A functional dependency means if you know X, you definitively know Y.", "analogy": "If you know a car's VIN, you definitively know its color.", "technical_explanation": "Expressed as X -> Y. X is the determinant. This is the basis for all normal forms.", "why_it_matters": "Without identifying FDs, you cannot normalize a database.", "remember": "Does X uniquely determine Y?"},
                    {"type": "visual", "visual_type": "text", "data": "SSN -> Name, DOB\nZipCode -> City, State"},
                    {"type": "micro_challenge", "question": "If EmployeeID determines Department, and Department determines Manager, what type of dependency is this?", "options": ["Partial", "Transitive", "Trivial"], "answer": "Transitive", "explanation": "The dependency passes through an intermediary non-key attribute."}
                ]
            },
            {
                "title": "Module 3: First Normal Form (1NF)",
                "blocks": [
                    {"type": "concept", "title": "Atomic Values", "explanation": "1NF requires that every column holds a single, atomic value.", "analogy": "Don't stuff an entire grocery list into a single receipt line item.", "technical_explanation": "No repeating groups or arrays. Each intersection of row and column must be scalar.", "why_it_matters": "Searching inside a comma-separated string is slow and error-prone.", "remember": "Atomicity above all."},
                    {"type": "sql_sandbox", "title": "Unnesting Data", "context": "A table `logs` has a column `tags` containing comma-separated values. We won't fix it in SQL yet, just create a new table `log_tags` to represent the 1NF version.", "init_script": "", "solution_query": "CREATE TABLE log_tags (log_id INT, tag VARCHAR(50), PRIMARY KEY(log_id, tag));", "hint": "Create a table with a composite primary key of log_id and tag.", "explanation": "Data is now atomic and easily queryable."}
                ]
            },
            {
                "title": "Module 4: Second Normal Form (2NF)",
                "blocks": [
                    {"type": "concept", "title": "Removing Partial Dependencies", "explanation": "2NF requires 1NF, and no partial dependencies on a composite primary key.", "analogy": "If a key requires two locks, a fact shouldn't be accessible with just one of the keys.", "technical_explanation": "All non-key attributes must depend on the ENTIRE primary key.", "why_it_matters": "Prevents redundant data when dealing with intersection tables.", "remember": "Only relevant for composite keys."},
                    {"type": "debugger", "title": "The Composite Flaw", "scenario": "Table: OrderDetails(OrderID, ProductID, ProductName). ProductName depends only on ProductID.", "options": ["It is in 2NF", "Violates 2NF", "Violates 1NF"], "answer": "Violates 2NF", "explanation": "ProductName is partially dependent on the composite key (OrderID, ProductID)."}
                ]
            },
            {
                "title": "Module 5: Third Normal Form (3NF)",
                "blocks": [
                    {"type": "concept", "title": "Removing Transitive Dependencies", "explanation": "3NF requires 2NF, and no transitive dependencies.", "analogy": "Don't store the manager's name in the employee record. Store the department ID, and let the department table hold the manager's name.", "technical_explanation": "Every non-key attribute must depend 'the key, the whole key, and nothing but the key, so help me Codd'.", "why_it_matters": "Eliminates the risk of updating an employee's department but forgetting to update their manager.", "remember": "No non-key attribute should depend on another non-key attribute."},
                    {"type": "sql_sandbox", "title": "Normalize to 3NF", "context": "Extract the department data into its own table.", "init_script": "", "solution_query": "CREATE TABLE departments (id INT PRIMARY KEY, manager_name VARCHAR(100));", "hint": "Create a departments table with id and manager_name.", "explanation": "You've removed the transitive dependency from the employee records."}
                ]
            },
            {
                "title": "Module 6: Boyce-Codd Normal Form (BCNF)",
                "blocks": [
                    {"type": "concept", "title": "The Stricter 3NF", "explanation": "BCNF handles edge cases where overlapping candidate keys exist.", "analogy": "Closing the final loophole in the law.", "technical_explanation": "For every non-trivial dependency X -> Y, X must be a superkey.", "why_it_matters": "Resolves anomalies in complex schemas that 3NF technically allows.", "remember": "Every determinant must be a candidate key."},
                    {"type": "visual", "visual_type": "text", "data": "If Student, Course -> Professor\nAnd Professor -> Course\nThen Professor must be a key in a separated table."}
                ]
            },
            {
                "title": "Module 7: The Price of Normalization",
                "blocks": [
                    {"type": "concept", "title": "Denormalization", "explanation": "Sometimes, joining 10 perfectly normalized tables is too slow.", "analogy": "Sometimes it's better to keep a copy of a document on your desk rather than walking to the archive every time.", "technical_explanation": "Intentionally violating normal forms to improve read performance at the cost of write complexity.", "why_it_matters": "Real-world databases balance theoretical purity with practical performance.", "remember": "Normalize until it hurts, denormalize until it works."},
                    {"type": "reflection", "question": "In a heavy read-only analytical database, would you prefer 3NF or a denormalized schema?"}
                ]
            },
            {
                "title": "Module 8: Memory Reconstruction",
                "blocks": [
                    {"type": "sql_sandbox", "title": "Restore the Mind", "context": "Create a 3NF compliant schema for a person's addresses. A person can have multiple addresses. Zip codes dictate the City.", "init_script": "", "solution_query": "CREATE TABLE zip_codes (zip VARCHAR(10) PRIMARY KEY, city VARCHAR(100)); CREATE TABLE addresses (id INT PRIMARY KEY, person_id INT, street VARCHAR(200), zip VARCHAR(10));", "hint": "Create two tables: zip_codes (zip, city) and addresses (id, person_id, street, zip).", "explanation": "The implant's memories are now perfectly consistent. The host's mind is clear."}
                ]
            }
        ]
    }
}
