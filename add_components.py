from connection import get_connection
from read_info import *


def check_field(field):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    if not field:
        return False
    elif field.isdigit():
        print("Вы ввели число, а так нельзя")
        return False
    elif all([letter in alphabet for letter in field]):
        print("Вы ввели английские буквы")
        return False
    return True


def add_student_or_teacher(who, tablename, cur=None):
    first_name = ""
    while not check_field(first_name):
        first_name = input(f"Введите имя {who}: ").capitalize()
    last_name = ""
    while not check_field(last_name):
        last_name = input(f"Введите фамилию {who}: ").capitalize()
    pater_name = ""
    while not check_field(pater_name):
        pater_name = input(f"Введите отчество {who}: ").capitalize()

    gender = ""
    while gender not in ["м", "ж"]:
        gender = input("Выберите пол (м/ж): ")

    phone_number = ""
    while len(phone_number) < 5 and not phone_number.isdigit():
        phone_number = input("Введите номер телефона без пробелов: ")

    cur.execute(f"SELECT COUNT(*) FROM {tablename}")
    iden = cur.fetchone()[0] + 1
    try:
        cur.execute(f"INSERT into {tablename} values(%d, '%s','%s','%s','%s','%s')" % (
            iden, first_name, last_name, pater_name, gender, phone_number
        ))
        print("Операция добавления успешно завершена!")
        return iden, first_name, last_name, pater_name, gender, phone_number
    except:
        print("Что-то не получилось")


@get_connection
def add_student(cur=None):
    add_student_or_teacher("ученика", "students", cur)


@get_connection
def add_teacher(cur=None):
    iden, first_name, last_name, pater_name, gender, phone_number = add_student_or_teacher(
        "учителя", "teachers", cur)


@get_connection
def add_subject(cur=None):
    name = ""
    while not check_field(name):
        name = input('Введите название предмета: ')
    cur.execute('SELECT COUNT(*) FROM subjects')
    id = cur.fetchone()[0] + 1
    try:
        cur.execute("INSERT INTO subjects VALUES (%d, '%s');" % (
            id, name
        ))
        print('Успешно добавлена новая запись!')
    except:
        print('Что-то не получилось')


@get_connection
def add_mark(cur=None):
    read_students_table(cur)
    iden = ""
    while not iden.isdigit():
        iden = input("У какого ученика ставим оценку? ")
    iden = int(iden)
    try:
        cur.execute("""
                    SELECT *
                    FROM students
                    WHERE student_id=%s
                    """%(iden))
    except:
        print("Нет такого ученика")
        return None
    

if __name__ == "__main__":
    add_mark()
