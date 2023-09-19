import math

while True:
    print("Выберите операцию:")
    print("1. Умножение")
    print("2. Деление")
    print("3. Сложение")
    print("4. Вычитание")
    print("5. Факториал")
    print("6. Возведение в степень")
    print("7. Найти 1% числа")
    print("8. Выход")

    choice = input("Введите номер операции (1/2/3/4/5/6/7/8): ")

    if choice == "8":
        print("Выход из программы.")
        break

    if choice in ["1", "2", "3", "4", "6", "7"]:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == "1":
            result = num1 * num2
            print("Результат:", result)
        elif choice == "2":
            if num2 == 0:
                print("Ошибка: деление на ноль.")
            else:
                result = num1 / num2
                print("Результат:", result)
        elif choice == "3":
            result = num1 + num2
            print("Результат:", result)
        elif choice == "4":
            result = num1 - num2
            print("Результат:", result)
        elif choice == "6":
            result = num1 ** num2
            print("Результат:", result)
        elif choice == "7":
            result = num1 * 0.01
            print("1% числа:", result)

    elif choice == "5":
        num = int(input("Введите число для вычисления факториала: "))
        if num < 0:
            print("Ошибка: факториал отрицательного числа не определен.")
        else:
            result = math.factorial(num)
            print(f"Факториал числа {num} равен: {result}")

    else:
        print("Ошибка: Неверный выбор операции. Пожалуйста, выберите снова.")