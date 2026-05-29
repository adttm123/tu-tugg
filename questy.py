
import time
import random
from defy import level_up


def zakoncz_questa(bohater):
    time.sleep(0.5)
    print("\n=== QUEST ZAKOŃCZONY ===")
    time.sleep(0.4)
    print(f"Ukończyłeś questa: {bohater.quest_name}!")
    time.sleep(0.3)
    print(f"Otrzymujesz {bohater.quest_reward_gold} złota i {bohater.quest_reward_exp} doświadczenia.")
    bohater.gold += bohater.quest_reward_gold
    bohater.experience += bohater.quest_reward_exp
    bohater.quest_name = None
    bohater.quest_kills = 0
    bohater.quest_target = 0
    bohater.quest_reward_gold = 0
    bohater.quest_reward_exp = 0
    level_up(bohater)


def start_quest(bohater):
    if bohater.quest_name is not None:
        print("Masz już aktywnego questa. Najpierw go ukończ.")
        return
    quest = {
        "name": "Zabij 20 przeciwników",
        "target": 20,
        "reward_gold": 150,
        "reward_exp": 100,
    }
    bohater.quest_name = quest["name"]
    bohater.quest_kills = 0
    bohater.quest_target = quest["target"]
    bohater.quest_reward_gold = quest["reward_gold"]
    bohater.quest_reward_exp = quest["reward_exp"]
    time.sleep(0.4)
    print("Rozpoczynasz questa: Zabij 20 przeciwników.")
    time.sleep(0.3)
    print("Gdy zniszczysz 20 potworów, otrzymasz nagrodę.")


def quest_menu(bohater):
    print("\n=== QUESTY ===")
    time.sleep(0.3)
    if bohater.quest_name is None:
        print("Brak aktywnego questa.")
        print("1 - Rozpocznij questa: Zabij 20 przeciwników")
        print("2 - Wyjście")
        wybor = input("> ").strip()
        if wybor == "1":
            start_quest(bohater)
        else:
            print("Wracasz do menu.")
        return
    print(f"Aktywny quest: {bohater.quest_name}")
    print(f"Postęp: {bohater.quest_kills}/{bohater.quest_target}")
    print("1 - Rezygnuj z questa")
    print("2 - Wyjście")
    wybor = input("> ").strip()
    if wybor == "1":
        bohater.quest_name = None
        bohater.quest_kills = 0
        bohater.quest_target = 0
        bohater.quest_reward_gold = 0
        bohater.quest_reward_exp = 0
        time.sleep(0.3)
        print("Zrezygnowałeś z questa.")
    else:
        print("Wracasz do menu.")
