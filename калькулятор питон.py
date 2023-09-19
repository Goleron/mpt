import math

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: Введите корректное число.")

def calculate_factorial(num):
    if num < 0:
        return "Ошибка: факториал отрицательного числа не определен."
    elif num == 0:
        return 1
    else:
        return math.factorial(num)

while True:
    print("\nВыберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("11. Выход")

    choice = input("Введите номер операции (1/2/3/4/5/6/7/8/9/10/11): ")

    if choice == "11":
        print("Выход из программы.")
        break

    if choice in ["1", "2", "3", "4", "5"]:
        num1 = get_number_input("Введите первое число: ")
        num2 = get_number_input("Введите второе число: ")

        if choice == "1":
            result = num1 + num2
            print("Результат:", result)
        elif choice == "2":
            result = num1 - num2
            print("Результат:", result)
        elif choice == "3":
            result = num1 * num2
            print("Результат:", result)
        elif choice == "4":
            if num2 == 0:
                print("Ошибка: деление на ноль.")
            else:
                result = num1 / num2
                print("Результат:", result)
        elif choice == "5":
            result = num1 ** num2
            print("Результат:", result)

    elif choice == "6":
        num = get_number_input("Введите число для извлечения квадратного корня: ")
        if num < 0:
            print("Ошибка: квадратный корень отрицательного числа не определен.")
        else:
            result = math.sqrt(num)
            print("Квадратный корень:", result)

    elif choice == "7":
        num = int(input("Введите число для вычисления факториала: "))
        result = calculate_factorial(num)
        print(f"Факториал числа {num} равен: {result}")

    elif choice in ["8", "9", "10"]:
        angle_degrees = get_number_input("Введите угол в градусах: ")
        angle_radians = math.radians(angle_degrees)

        if choice == "8":
            result = math.sin(angle_radians)
            print(f"Синус угла {angle_degrees} градусов:", result)
        elif choice == "9":
            result = math.cos(angle_radians)
            print(f"Косинус угла {angle_degrees} градусов:", result)
        elif choice == "10":
            result = math.tan(angle_radians)
            print(f"Тангенс угла {angle_degrees} градусов:", result)

    else:
        print("Ошибка: Неверный выбор операции. Пожалуйста, выберите снова.")11
        