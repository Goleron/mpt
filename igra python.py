import random

def get_user_name():
    user_name = input("Введите ваше имя: ")
    return user_name

user_name = get_user_name()
happiness = 50
energy = 50

questions = [
    "Сегодня у вас были трудные уроки в школе. Решили ли вы уделить им больше внимания?",
    "Ближайший экзамен требует серьезной подготовки. Вы собираетесь заняться учебой?",
    "Сегодня отличный день для похода в спортзал. Пойдете тренироваться?",
    "Ваши друзья предложили вам встречу. Согласны ли вы на вечер веселья с ними?",
]

positive_responses = ["Отлично!", "Замечательно!", "Прекрасно!"]
negative_responses = ["Ой...", "Не очень...", "Сложно..."]

used_questions = []

def choose_event():
    if len(used_questions) == len(questions):
        print("Вы ответили на все вопросы. Игра завершена.")
        display_results()
        return

    while True:
        event_index = random.randint(0, len(questions) - 1)
        if event_index not in used_questions:
            break

    used_questions.append(event_index)
    event = questions[event_index]
    print(f"{user_name}, вопрос: {event}\n")

    while True:
        choice = input(f"{user_name}, ваш ответ (да/нет): ").lower()
        if choice in ("да", "нет"):
            break
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")

    if choice == "да":
        handle_positive_event(event)
    else:
        handle_negative_event(event)

    print(random.choice(positive_responses if choice == "да" else negative_responses))
    continue_story()

def continue_story():
    print("\nПрошло несколько дней...")
    print(f"{user_name}, ваши действия повлияли на вашу жизнь. Вот новые события:\n")

    new_questions = [
        "Ваш друг Макс предложил вам пойти на важное мероприятие. Согласны ли вы?",
        "На уроках появилась новая девушка, которая просит помощи в учебе. Поможете ли вы ей?",
        "Вы нашли старую забытую книгу в библиотеке. Решите ли вы ее прочитать?",
    ]

    for question in new_questions:
        while True:
            choice = input(f"{user_name}, {question} (да/нет): ").lower()
            if choice in ("да", "нет"):
                break
            else:
                print("Пожалуйста, введите 'да' или 'нет'.")

        if choice == "да":
            print("Вы сделали позитивный выбор!")
        else:
            print("Вы сделали негативный выбор!")

    display_results()

def handle_positive_event(event):
    global happiness
    global energy

    if "трудные уроки" in event:
        happiness -= 5
        energy -= 10
        print(f"{user_name}, трудные уроки в школе заставили вас подумать глубже.")
    elif "ближайший экзамен" in event:
        happiness -= 3
        energy -= 10
        print(f"{user_name}, подготовка к экзамену, вы чувствуете себя более подготовленным(ой).")
    elif "поход в спортзал" in event:
        happiness += 5
        energy -= 10
        print(f"{user_name}, поход в спортзал оставил вас бодрым(ой).")
    elif "встреча с друзьями" in event:
        happiness += 10
        energy -= 5
        print(f"{user_name}, встреча с друзьями была веселой.")

def handle_negative_event(event):
    global happiness
    global energy

    if "трудные уроки" in event:
        happiness -= 10
        energy -= 10
        print(f"{user_name}, трудные уроки сильно утомили вас.")
    elif "ближайший экзамен" in event:
        happiness -= 8
        energy -= 15
        print(f"{user_name}, подготовка к экзамену оказалась очень сложной.")
    elif "поход в спортзал" in event:
        happiness -= 5
        energy -= 10
        print(f"{user_name}, после тренировки вам стало не по себе.")
    elif "встреча с друзьями" in event:
        happiness -= 5
        energy -= 5
        print(f"{user_name}, встреча с друзьями прошла не так, как вы ожидали.")

def display_results():
    print("\nИгра завершена. Параметры жизни подростка:")
    print(f"Имя: {user_name}")
    print(f"Счастье: {happiness}")
    print(f"Энергия: {energy}")

def main():
    print(f"Добро пожаловать в игру , {user_name}!\n")
    print(f"{user_name}, ваша цель - управлять своей жизнью и принимать решения в различных ситуациях.")
    print("Давайте начнем ваше приключение!\n")

    choose_event()

if __name__ == "__main__":
    main()
