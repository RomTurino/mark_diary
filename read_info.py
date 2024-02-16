from connection import get_connection


@get_connection
def read_students_table(cur=None):
    cur.execute("SELECT * FROM STUDENTS")
    students = cur.fetchall()
    headers = "№\tИмя\tФамилия\tОтчество\tПол\tНомер телефона"
    print(headers)
    for student in students:
        print(*student, sep="\t")
        
        
@get_connection
def read_teachers_table(cur=None):
    cur.execute("SELECT * FROM teachers")
    teachers = cur.fetchall()
    headers = "№\tИмя\tФамилия\tОтчество\tПол\tНомер телефона"
    print(headers)
    for teacher in teachers:
        print(*teacher, sep="\t")

@get_connection
def read_subjects_table(cur=None):
    cur.execute("SELECT subject_id, name FROM subjects")
    subjects = cur.fetchall()
    headers = "№\tНазвание предмета"
    print(headers)
    for subject in subjects:
        print(*subject, sep="\t")





if __name__ == "__main__":
    print(__name__)
