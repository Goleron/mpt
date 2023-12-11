import sqlite3
import getpass
import sys
import time

def input_password(prompt="Введите пароль: "):
    print(prompt, end='', flush=True)
    buffer = []
    while True:
        char = sys.stdin.read(1)
        if char == '\n':
            break
        if char:
            print(char, end='', flush=True)
            buffer.append(char)
            time.sleep(0.5)
            sys.stdout.write("\b*")
            sys.stdout.flush()
    return ''.join(buffer)

def create_hr_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hr_employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            salary REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def create_tables_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tables (
            id INTEGER PRIMARY KEY,
            capacity INTEGER NOT NULL,
            preferences TEXT,
            booking_start_date TEXT,
            booking_end_date TEXT
        )
    ''')
    conn.commit()
    conn.close()

def create_employees_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def create_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()



def main_menu():
    while True:
        print("\nГлавное меню:")
        print("1. Войти")
        print("2. Зарегистрироваться")
        print("3. Выйти")

        choice = input("Выберите опцию (1-3): ")

        if choice == '1':
            login_user()
        elif choice == '2':
            register_user()
        elif choice == '3':
            print("Завершение работы программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

def initialize_default_users():
    default_users = [
        ('admin', '111', 'admin'),
        ('cash', '222', 'kash'),
        ('kadr', '333', 'kadr')
    ]

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    for username, password, role in default_users:
        cursor.execute("""
        INSERT INTO users (username, password, role) VALUES (?, ?, ?)
        ON CONFLICT(username) DO UPDATE SET password=excluded.password, role=excluded.role;
        """, (username, password, role))

    conn.commit()
    conn.close()

def login_user():
    username = input("Введите логин: ")
    password = input_password()
    
    print(f"Отладка: введенный логин: {username}")  
    print(f"Отладка: введенный пароль: {password}")  

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT role FROM users WHERE username=? AND password=?", (username, password))
        role = cursor.fetchone()
        if role:
            print(f"Вы успешно вошли в систему как {role[0]}.")
            if role[0] == 'admin':
                admin_interface()
            elif role[0] == 'kash':
                kash_interface()
            elif role[0] == 'kadr':
                kadr_interface()
        else:
            print("Неверный логин или пароль.")
    except sqlite3.Error as e:
        print(f"Произошла ошибка: {e.args[0]}")
    finally:
        conn.close()


def register_user():
    username = input("Введите логин: ")
    password = getpass.getpass("Введите пароль: ")
    role = input("Введите роль (admin/kash/kadr): ")

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
        conn.commit()
        print("Пользователь успешно зарегистрирован.")
    except sqlite3.IntegrityError:
        print("Логин уже существует.")
    finally:
        conn.close()


def admin_interface():
    while True:
        print("\nАдминистративный интерфейс:")
        print("1. Просмотр сотрудников")
        print("2. Изменение данных сотрудника")
        print("3. Выход")

        choice = input("Выберите опцию (1-3): ")

        if choice == '1':
            view_employees()
        elif choice == '2':
            modify_employee()
        elif choice == '3':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

def view_employees():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, position FROM employees")
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, Имя: {row[1]}, Должность: {row[2]}")
    conn.close()

def modify_employee():
    employee_id = input("Введите ID сотрудника для изменения: ")
    new_name = input("Введите новое имя (оставьте пустым, чтобы не изменять): ")
    new_position = input("Введите новую должность (оставьте пустым, чтобы не изменять): ")
    new_username = input("Введите новый логин (оставьте пустым, чтобы не изменять): ")
    new_password = input("Введите новый пароль (оставьте пустым, чтобы не изменять): ")

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    if new_name:
        cursor.execute("UPDATE employees SET name = ? WHERE id = ?", (new_name, employee_id))
    if new_position:
        cursor.execute("UPDATE employees SET position = ? WHERE id = ?", (new_position, employee_id))
    if new_username:
        cursor.execute("UPDATE employees SET username = ? WHERE id = ?", (new_username, employee_id))
    if new_password:
        cursor.execute("UPDATE employees SET password = ? WHERE id = ?", (new_password, employee_id))

    conn.commit()
    conn.close()
    print("Данные сотрудника обновлены.")

if __name__ == "__main__":
    create_db()
    create_employees_table()
    main_menu()

def kash_interface():
    while True:
        print("\nИнтерфейс кассира:")
        print("1. Просмотр столов")
        print("2. Изменение информации о столе")
        print("3. Выход")

        choice = input("Выберите опцию (1-3): ")

        if choice == '1':
            view_tables()
        elif choice == '2':
            modify_table()
        elif choice == '3':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

def view_tables():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, capacity, preferences, booking_start_date, booking_end_date FROM tables")
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, Вместимость: {row[1]}, Предпочтения: {row[2]}, Бронь с {row[3]} по {row[4]}")
    conn.close()

def modify_table():
    table_id = input("Введите ID стола для изменения: ")
    new_capacity = input("Введите новую вместимость (оставьте пустым, чтобы не изменять): ")
    new_preferences = input("Введите новые предпочтения (оставьте пустым, чтобы не изменять): ")
    new_booking_start = input("Введите новую дату начала брони (оставьте пустым, чтобы не изменять): ")
    new_booking_end = input("Введите новую дату окончания брони (оставьте пустым, чтобы не изменять): ")

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    if new_capacity:
        cursor.execute("UPDATE tables SET capacity = ? WHERE id = ?", (new_capacity, table_id))
    if new_preferences:
        cursor.execute("UPDATE tables SET preferences = ? WHERE id = ?", (new_preferences, table_id))
    if new_booking_start:
        cursor.execute("UPDATE tables SET booking_start_date = ? WHERE id = ?", (new_booking_start, table_id))
    if new_booking_end:
        cursor.execute("UPDATE tables SET booking_end_date = ? WHERE id = ?", (new_booking_end, table_id))

    conn.commit()
    conn.close()
    print("Информация о столе обновлена.")

if __name__ == "__main__":
    create_db()
    create_employees_table()
    create_tables_table()
    main_menu()

def kadr_interface():
    while True:
        print("\nИнтерфейс отдела кадров:")
        print("1. Изменение ФИО сотрудника")
        print("2. Изменение зарплаты сотрудника")
        print("3. Добавление нового сотрудника")
        print("4. Выход")

        choice = input("Выберите опцию (1-4): ")

        if choice == '1':
            change_employee_name()
        elif choice == '2':
            change_employee_salary()
        elif choice == '3':
            add_new_employee()
        elif choice == '4':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2, 3 или 4.")

def change_employee_name():
    employee_id = input("Введите ID сотрудника для изменения ФИО: ")
    new_name = input("Введите новое ФИО сотрудника: ")

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE hr_employees SET name = ? WHERE id = ?", (new_name, employee_id))
    conn.commit()
    conn.close()
    print("ФИО сотрудника обновлено.")

def change_employee_salary():
    employee_id = input("Введите ID сотрудника для изменения зарплаты: ")
    new_salary = float(input("Введите новую зарплату сотрудника: "))

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE hr_employees SET salary = ? WHERE id = ?", (new_salary, employee_id))
    conn.commit()
    conn.close()
    print("Зарплата сотрудника обновлена.")

def add_new_employee():
    name = input("Введите ФИО нового сотрудника: ")
    salary = float(input("Введите зарплату нового сотрудника: "))

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hr_employees (name, salary) VALUES (?, ?)", (name, salary))
    conn.commit()
    conn.close()
    print("Новый сотрудник добавлен.")




if __name__ == "__main__":
    create_db()
    create_employees_table()
    create_tables_table()
    create_hr_table()
    initialize_default_users()  
    main_menu()