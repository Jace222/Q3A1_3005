COMP 3005 A1 Q3

Jason Shao
101 219 526

Demonstration Video:                        https://youtu.be/xQigxnNnq1g


Steps to compile and run my application:
    Setup PostgreSQL Database: 
        Ensure PostgreSQL is installed and running on your system.
        (done in the python script) Create a new database and execute the provided schema to create the 'students' table.

    OR YOU CAN directly run the code for creating table and inserting the initial values with the following into Postgres

        CREATE TABLE IF NOT EXISTS students (    
                                        student_id SERIAL PRIMARY KEY,
                                        first_name TEXT NOT NULL,
                                        last_name TEXT NOT NULL,
                                        email TEXT NOT NULL UNIQUE,
                                        enrollment_date DATE
                                    );

        INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
                                        ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
                                        ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
                                        ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

    Make sure that the following information matches the database so that connection will be valid:

        database_info = {
            'dbname':   'Assignment3_Question1',
            'user':     'postgres',
            'password': 'postgres',
            'host':     'localhost',
            'port':     '5432'
        }

    Populate the Database:
        (done in the python script) Execute the provided initial data script to populate the 'students' table.

    Install Dependencies:
        Ensure you have the required Python libraries installed. You may need to install psycopg2 for PostgreSQL database connectivity.

    Run the Application:
        Execute the Python script in your terminal or IDE.
        Make sure to provide necessary database connection details within the script (e.g., database name, username, password).