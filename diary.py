


from init import create_all_tables
from add_components import *

while True:
    print("Меню:")
    print("1 - Инициализировать все базы данных")
    print("2 - Добавить ученика")
    print("3 - Добавить предмет")
    print("4 - Выйти из программы")
    action = input("Ваш выбор:")
    if action == "1":
        create_all_tables()
    elif action == "2":
        add_student()
    elif action == "3":
        add_subject()
    elif action == "4":
        print("Спасибо за использование программы")
        break
    input('Нажмите Enter, чтобы продолжить')