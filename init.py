from connection import get_connection

@get_connection
def create_table_students(cur=None):
    cur.execute("""
                CREATE TABLE IF NOT EXISTS students
                (
                    student_id int PRIMARY KEY,
                    first_name varchar(64) NOT NULL,
                    last_name varchar(64) NOT NULL,
                    pater_name varchar(64) NOT NULL,
                    gender varchar(1) NOT NULL,
                    phone_number varchar(16) NOT NULL
                )
                """)

@get_connection
def create_table_teachers(cur=None):
    cur.execute("""
                CREATE TABLE IF NOT EXISTS teachers
                (
                    teacher_id int PRIMARY KEY,
                    first_name varchar(64) NOT NULL,
                    last_name varchar(64) NOT NULL,
                    pater_name varchar(64) NOT NULL,
                    gender varchar(1) NOT NULL,
                    phone_number varchar(16) NOT NULL
                )
                """)

@get_connection
def create_subjects(cur=None):
    cur.execute("""
                CREATE TABLE IF NOT EXISTS subjects
                (
                    subject_id int PRIMARY KEY,
                    name varchar(128) NOT NULL,
                    fk_techer_id int REFERENCES teachers(teacher_id)
                )
                """)

@get_connection
def create_schedule(cur=None):
    cur.execute("""
                CREATE TABLE IF NOT EXISTS schedule
                (
                    schedule_id int PRIMARY KEY,
                    day varchar(12) NOT NULL,
                    fk_subject_id int REFERENCES subjects(subject_id)
                )
                """)    

@get_connection
def create_table_marks(cur=None):
    cur.execute("""
                CREATE TABLE IF NOT EXISTS marks
                (
                    mark_id int PRIMARY KEY,
                    fk_student_id int REFERENCES students(student_id),
                    fk_subject_id int REFERENCES subjects(subject_id)
                )
                """)


def drop_databases(cur=None):
    cur.execute("DROP table IF EXISTS students")
    cur.execute("DROP table IF EXISTS teachers")
    cur.execute("DROP table IF EXISTS marks")
    cur.execute("DROP table IF EXISTS schedule")
    cur.execute("DROP table IF EXISTS subjects")


@get_connection
def create_all_tables(cur=None):
    drop_databases(cur)
    create_table_students(cur)
    create_table_teachers(cur)
    create_subjects(cur)
    create_schedule(cur)
    create_table_marks(cur)
    
