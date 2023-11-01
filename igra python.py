import time
import random
import json
import csv 

WEAK_ATTACK = "1"
STRONG_ATTACK = "2"
DEFEND = "3"


def save_to_csv():
    with open("game_history.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([player_name, len(player_inventory), player_health, game_over, ",".join(locations_visited)])

def load_game():
    global player_name, player_inventory, game_over, locations_visited, player_health

    with open("game_save.json", "r") as f:
        game_data = json.load(f)

    player_name = game_data["player_name"]
    player_inventory = set(game_data["player_inventory"])
    game_over = game_data["game_over"]
    locations_visited = game_data["locations_visited"]
    player_health = game_data["player_health"]
    print("Игра загружена!")

def save_game():
    game_data = {
        "player_name": player_name,
        "player_inventory": list(player_inventory),
        "game_over": game_over,
        "locations_visited": locations_visited,
        "player_health": player_health
    }
    with open("game_save.json", "w") as f:
        json.dump(game_data, f)
    print("Игра сохранена!")

def ask_name():
    global player_name
    print("Как вас зовут, путник?")
    player_name = input("> ").strip()
    print(f"Добро пожаловать в мир нашей игры, {player_name}!\n")

def cave_dialogue():
    print("\nОсторожно проникая в пещеру, вы обнаруживаете слабо мерцающий огонек вдали.")
    time.sleep(2)
    print("Приближаясь, вы видите умирающего пирата, рядом с которым горит зажженная свеча.")
    time.sleep(2)
    print('Пират с трудом произносит: "Так много лет... Цель всей моей жизни была найти это сокровище."')
    time.sleep(2)
    print('"Возьми эту карту из моих рук... И найди клад. Пусть он не уйдет со мной в могилу."')
    time.sleep(2)
    print("Пират скончался...")
    time.sleep(2)
    add_to_inventory("карта сокровищ")
    print("\nКак вы двигаетесь глубже в пещеру, вы замечаете человека с следом крови на его одежде.")
    time.sleep(2)
    print('Таинственный человек: "Я слышал, что у тебя есть карта, которую этот пират держал. Отдай ее мне или пожалеешь!"')
    time.sleep(2)
    
    choice = ""
    while choice not in ["1", "2"]:
        print("\nЧто вы будете делать?")
        print("1. Отдать карту таинственному человеку")
        print("2. Отказаться и продолжить свою миссию")
        
        choice = input("> ").strip()

        if choice == "1":
            print("Вы решаете отдать карту. Таинственный человек уходит, оставив вас в покое.")
            player_inventory.remove("карта сокровищ")
            return
        elif choice == "2":
            print("Вы решаете продолжить свою миссию и искать клад пирата.")
    

    search_for_treasure()

def search_for_treasure():
    print("\nС картой в руках, вы начинаете следовать указаниям.")
    time.sleep(2)
    print("Проходя по засекреченным уголкам пещеры, вы чувствуете, что приближаетесь к своей цели.")
    time.sleep(2)
    print("Наконец, вы обнаруживаете древний сундук, скрытый среди камней и мха.")
    time.sleep(2)
    print("Вы открываете сундук и видите, что он полон золота, драгоценных камней и других сокровищ!")
    time.sleep(2)
    print("Теперь это сокровище принадлежит вам.")
    add_to_inventory("древний сундук с сокровищами")

def show_inventory():
    global player_inventory
    if player_inventory:
        print(f"Ваш инвентарь: {', '.join(player_inventory)}")
    else:
        print("Ваш инвентарь пуст.")

def sword_in_inventory():
    if "магический меч" in player_inventory:
        damage = damage * 2

def add_to_inventory(item):
    global player_inventory
    player_inventory.add(item)
    print(f"{item} добавлено в ваш инвентарь!\n")

def check_location(location):
    if location in locations_visited:
        print(f"Вы уже были в {location}. Выберите другое место.")
        return True
    return False

def castle_dialogue():
    print("\nВы встретили Поверженного рыцаря...")
    time.sleep(1)
    print(f'Поверженный рыцарь: "Ты кто такой, {player_name}? Что делаешь в моем замке?"')
    response = input("> ").strip()
    print(f'Поверженный рыцарь: " {response}? Ладно, не важно. Докажи, что ты рыцарь и ты получишь мой крутейший меч. Ответь на мой вопрос."')
    time.sleep(1)
    print('Поверженный рыцарь: "Кто основатель рыцарского ордена Круглого стола?"')

    answer = input("> ").strip().lower()

    if answer == "король артур":
        print('Поверженный рыцарь: "Верно! Вот мой меч."')
        add_to_inventory("магический меч")
    else:
        print('Поверженный рыцарь: "Ты обманщик! Убирайся отсюда!"')

def forest_dialogue():
    print("\nВы встретили гнома, охраняющего мост...")
    time.sleep(1)
    print('Гном: "Чтобы пройти, реши мои загадки!"')

    riddles = [
        {"q": "Без окон, без дверей, полна комната гостей.", "a": "арбуз"},
        {"q": "Не лает, не кусает, в дом не пускает.", "a": "замок"},
        {"q": "Стоит домик, в темном углу. Всех на свете ждет в гостях.", "a": "холодильник"}
    ]


    correct_answers = 0
    for riddle in riddles:
        print(riddle["q"])
        answer = input("> ").strip().lower()
        if answer == riddle["a"]:
            correct_answers += 1
            print('Гном: "Верно!"')
        else:
            print('Гном: "Неправильно!"')

    if correct_answers == 3:
        print('Гном: "Ты прошел испытание! Держи свою награду."')
        add_to_inventory("тайное зелье")
    else:
        print('Гном: "Ты не прошел испытание! Теперь ты должен сразиться со мной!"')
        fight_with_gnome()

def fight_with_gnome():
    global player_health
    player_health = 100
    gnome_health = 80

    while player_health > 0 and gnome_health > 0:
        print("\nВаше здоровье:", player_health)
        print("Здоровье гнома:", gnome_health)

        print("\nВыберите действие:")
        print(f"{WEAK_ATTACK}. Слабая атака")
        print(f"{STRONG_ATTACK}. Сильная атака")
        print(f"{DEFEND}. Защита")
        choice = input("> ").strip()

        gnome_choice = random.choice([WEAK_ATTACK, STRONG_ATTACK, DEFEND])

        if choice == WEAK_ATTACK:
            hit_chance = random.randint(1, 100)
            if hit_chance <= 90:
                damage = random.randint(5, 10)
                gnome_health -= damage
                print(f"Вы нанесли гному {damage} урона!")
            else:
                print("Вы промахнулись!")

        elif choice == STRONG_ATTACK:
            hit_chance = random.randint(1, 100)
            if hit_chance <= 40:
                damage = random.randint(15, 25)
                gnome_health -= damage
                print(f"Вы нанесли гному {damage} урона!")
            else:
                print("Вы промахнулись!")
        elif choice == DEFEND:
           print("Вы готовитесь к защите!")

        # Гном атакует
        if gnome_choice == WEAK_ATTACK:
            hit_chance = random.randint(1, 100)
            if hit_chance <= 90:
                damage = random.randint(5, 10)
                if choice == "3":
                    damage //= 2
                player_health -= damage
                print(f"Гном нанес вам {damage} урона!")
            else:
                print("Гном промахнулся!")

        elif gnome_choice == STRONG_ATTACK:
            hit_chance = random.randint(1, 100)
            if hit_chance <= 40:
                damage = random.randint(10, 20)
                if choice == "3":
                    damage //= 2
                player_health -= damage
                print(f"Гном нанес вам {damage} урона!")
            else:
                print("Гном промахнулся!")
        
        elif gnome_choice == DEFEND:
            print("Гном готовится к защите!")

    if player_health > 0:
        print("\nВы победили гнома!")
    else:
        print("\nГном победил вас...")
        global game_over
        game_over = True



def main_story():
    global game_over, locations_visited

    while not game_over:
        location = ""
        print("\nКуда вы хотите пойти дальше?")
        print("1. Замок")
        print("2. Лес")
        print("3. Пещера")
        print("4. Показать инвентарь")
        print("5. Завершить игру")
        print("6.Увидеть свое здоровье")
        print("7. Сохранить игру")
        print("8. Загрузить игру")
        print("9. Завершить игру")

        choice = input("> ").strip()

        if choice == "1":
            location = "Замок"
            if check_location(location):
                continue
            locations_visited.append(location)
            print(f"\nДобро пожаловать в {location}!")
            castle_dialogue()

        elif choice == "2":
            location = "Лес"
            if check_location(location):
                continue
            locations_visited.append(location)
            print(f"\nВы зашли в {location}...")
            forest_dialogue()
            
        elif choice == "3":
            location = "Пещера"
            if check_location(location):
                continue

            locations_visited.append(location)
            cave_dialogue() 

        elif choice == "4":
            show_inventory()

        elif choice == "5":
            print("Спасибо за игру!")
            game_over = True
        elif choice == "6":
            print(f"Ваше текущее состояние здоровья: {player_health} HP")
            if choice == "7":
             save_game()

        elif choice == "8":
            load_game()

        elif choice == "9":
            print("Спасибо за игру!")
        save_to_csv()  # Сохраняем историю игрока в CSV-файл при завершении
        game_over = True


    else:
        print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    player_name = ""
    player_inventory = set()
    game_over = False
    locations_visited = []
    ask_name()
    player_health = 100 
    main_story()