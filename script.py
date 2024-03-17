import psycopg2

database_info = {
    'dbname':   'Assignment3_Question1',
    'user':     'postgres',
    'password': 'postgres',
    'host':     'localhost',
    'port':     '5432'
}

def initialize_database():                                          #this function initilaizes the database, students table, and inserts some initial value into the table
    try:
        conn = psycopg2.connect(**database_info)                    #connect to the database with the given name
        cur = conn.cursor()

        cur.execute('DROP TABLE IF EXISTS students')                #for my testing purposes, drop the table if it already exists

        #create a script to create the student table
        create_script = '''CREATE TABLE IF NOT EXISTS students (    
                                student_id SERIAL PRIMARY KEY,
                                first_name TEXT NOT NULL,
                                last_name TEXT NOT NULL,
                                email TEXT NOT NULL UNIQUE,
                                enrollment_date DATE
                            );'''
        cur.execute(create_script)                                  #executes the script

        #create a 2nd script to insert data into the student table
        insert_script = '''INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
                                ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
                                ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
                                ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');'''
        cur.execute(insert_script)                                  #execute this script

        conn.commit()                                               #commit all the previous executions (after making modifications to the database)

    except Exception as error:                                      #catch block in case the given database info is incorrect
        print(error)

    finally:                                                        #finally block to close conn and cur if they were initialized
        if conn is not None:
            conn.close()
        if cur is not None:
            cur.close()

def getAllStudents():
    with psycopg2.connect(**database_info) as conn:                 #connect to the database
        with conn.cursor() as cursor:                               #use with clause (no need to close cursor using this)
            cursor.execute("SELECT * FROM students;")               #execute script
            students = cursor.fetchall()                            #get all the students
            for student in students:                                #print each students' info in a loop
                print(student)

def addStudent(first_name, last_name, email, enrollment_date):      #similar process as in getAllStudents function
    with psycopg2.connect(**database_info) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
                (first_name, last_name, email, enrollment_date)
            )

def updateStudentEmail(student_id, new_email):                      #similar process as in getAllStudents function
    with psycopg2.connect(**database_info) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE students SET email = %s WHERE student_id = %s;",
                (new_email, student_id)
            )

def deleteStudent(student_id):                                      #similar process as in getAllStudents function
    with psycopg2.connect(**database_info) as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))

# initialize_database()

# print("All Students:")                                      #print all
# getAllStudents()

#print("Added new student:")
# addStudent('New1', 'Student1', '1new.student@example.com', '2023-09-03')
# addStudent('New2', 'Student2', '2new.student@example.com', '2023-09-04')
# addStudent('New3', 'Student3', '3new.student@example.com', '2023-09-05')
# addStudent('New4', 'Student4', '4new.student@example.com', '2023-09-06')
# addStudent('New5', 'Student5', '5new.student@example.com', '2023-09-07')

# print("\nAll students after the modification above:")       #print all
#getAllStudents()

# print("Updated email of a student with ID of 1:")
# updateStudentEmail(1, 'john.doe.updated@example.com')
# updateStudentEmail(2, 'SECONDchanged@gmail.com')
# updateStudentEmail(3, 'THIRDchanged@gmail.com')
# updateStudentEmail(4, 'FOURTHchanged@gmail.com')
# updateStudentEmail(5, 'FIFTHchanged@gmail.com')


# print("\nAll students after the modification above:")       #print all
# getAllStudents()

print("Deleted student wth ID of 2:")
deleteStudent(2)
deleteStudent(3)
deleteStudent(4)
deleteStudent(5)
deleteStudent(6)


# print("\nAll students after the modification above:")       #print all
getAllStudents()