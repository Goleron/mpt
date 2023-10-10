import random

# Функция для получения имени пользователя
def get_user_name():
    user_name = input("Введите ваше имя: ")
    return user_name

# Инициализация параметров
user_name = get_user_name()
happiness = 50
energy = 50
friends = ["Лиза", "Макс", "Джейк"]
tasks = ["Уроки", "Подготовка к экзамену", "Поход в спортзал", "Встреча с друзьями"]

# Список событий в игре
events = [
    "Сегодня в школе прошли трудные уроки.",
    "Ты провел(а) долгие часы, готовясь к ближайшему экзамену.",
    "Ты успешно сходил(а) в спортзал и потренировался(ась).",
    "Ты провел(а) вечер весело, встретившись с друзьями.",
]

# Функция для вывода события и выбора действия
def choose_event():
    event = random.choice(events)
    print(f"{user_name}, событие: {event}\n")
    print("1. Реагировать позитивно.")
    print("2. Реагировать негативно.")
    choice = input(f"{user_name}, ваш выбор (1/2): ")

    while choice not in ("1", "2"):
        print("Пожалуйста, введите 1 или 2.")
        choice = input(f"{user_name}, ваш выбор (1/2): ")

    if choice == "1":
        handle_positive_event(event)
    elif choice == "2":
        handle_negative_event(event)

# Функция для обработки положительных событий
def handle_positive_event(event):
    global happiness
    global energy

    if "трудные уроки" in event:
        happiness -= 5
        energy -= 10
        print(f"{user_name}, трудные уроки в школе заставили вас подумать глубже.")
    elif "готовясь к экзамену" in event:
        happiness -= 3
        energy -= 10
        print(f"{user_name}, готовясь к экзамену, вы чувствуете себя более подготовленным(ой).")
    elif "потренировался(ась)" in event:
        happiness += 5
        energy -= 10
        print(f"{user_name}, поход в спортзал оставил вас бодрым(ой).")
    elif "встретившись с друзьями" in event:
        happiness += 10
        energy -= 5
        print(f"{user_name}, встреча с друзьями была веселой.")

# Функция для обработки отрицательных событий
def handle_negative_event(event):
    global happiness
    global energy

    if "трудные уроки" in event:
        happiness -= 10
        energy -= 10
        print(f"{user_name}, трудные уроки сильно утомили вас.")
    elif "готовясь к экзамену" in event:
        happiness -= 8
        energy -= 15
        print(f"{user_name}, подготовка к экзамену оказалась очень сложной.")
    elif "потренировался(ась)" in event:
        happiness -= 5
        energy -= 10
        print(f"{user_name}, после тренировки вам стало не по себе.")
    elif "встретившись с друзьями" in event:
        happiness -= 5
        energy -= 5
        print(f"{user_name}, встреча с друзьями прошла не так, как вы ожидали.")

# Функция для вывода результатов игры
def display_results():
    print("\nИгра завершена. Параметры жизни подростка:")
    print(f"Имя: {user_name}")
    print(f"Счастье: {happiness}")
    print(f"Энергия: {energy}")

# Главный цикл игры
def main():
    print(f"Добро пожаловать в игру 'Жизнь подростка', {user_name}!\n")
    print(f"{user_name}, ваша цель - управлять своей жизнью и принимать решения в различных ситуациях.")
    print("Давайте начнем ваше приключение!\n")

    for _ in range(4):
        choose_event()

    display_results()

if __name__ == "__main__":
    main()
