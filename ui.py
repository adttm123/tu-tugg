
import time
import postacie
import bossy
import questy



def ekran_statystyk(bohater):
    time.sleep(0.3)


    print("\n" + "=" * 45)
    print("           KARTA POSTACI   ")
    print("=" * 45)
    time.sleep(0.2)
    print(f"  Imię       : {bohater.name}")
    print(f"  Klasa      : {bohater.__class__.__name__}")
    print(f"  Poziom     : {bohater.level}")
    print("-" * 45)
    time.sleep(0.2)
    print(f"    HP      : {bohater.life}/{bohater.maxlife}")
    print(f"   Mana    : {bohater.mana}/{bohater.maxmana}")
    print(f"   Doświad : {bohater.experience}/{bohater.next_level_exp}")
    print("-" * 45)
    time.sleep(0.2)
    print(f"    Siła       : {bohater.strength}")
    print(f"    Obrona     : {bohater.defense}")
    print(f"   Kryt. szansa  : {int(bohater.critical_chance * 100)}%")
    print(f"   Kryt. mnożnik : x{bohater.critical_multiplier}")
    print(f"   Szansa uniku  : {int(bohater.dodge_chance * 100)}%")
    print("-" * 45)
    time.sleep(0.2)
    print(f"   Złoto       : {bohater.gold}")
    print(f"   Plecak      : {len(bohater.backpack)} przedmiotów")
    if bohater.quest_name:
        print(f"   Quest       : {bohater.quest_name} ({bohater.quest_kills}/{bohater.quest_target})")
    else:
        print(f"   Quest       : Brak aktywnego questa")
    print("\n" + "=" * 45)
    time.sleep(0.3)
    input("  Wciśnij Enter, aby wrócić...")