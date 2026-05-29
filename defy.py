import random
from random import choice, randint
import time
import postacie
import bossy
import questy
from ui import ekran_statystyk
from kowal import kowal
def drzewko_umiejetnosci(bohater):
    print("\n=== DRZEWKO UMIEJĘTNOŚCI ===")
    time.sleep(0.5)
    print("1 - Zwiększ szansę na cios krytyczny (wymagany level 20)")
    print("2 - Zwiększ obrażenia krytyczne (wymagany level 20)")
    print("3 - Zwiększ szansę na unik (wymagany level 30)")
    print("4 - Zwiększ obronę (wymagany level 40)")
    print("5 - Wyjście")
    wybor = input("> ").strip()
    if wybor == "1":
        if bohater.level >= 20:
            bohater.critical_chance += 0.05
            time.sleep(0.4)
            print("Zwiększasz szansę na cios krytyczny o 5%!")
        else:
            time.sleep(0.3)
            print("Musisz osiągnąć co najmniej 20 poziom, aby odblokować tę umiejętność.")
    elif wybor == "2":
        if bohater.level >= 20:
            bohater.critical_multiplier += 0.5
            time.sleep(0.4)
            print("Zwiększasz obrażenia krytyczne o 0.5!")
        else:
            time.sleep(0.3)
            print("Musisz osiągnąć co najmniej 20 poziom, aby odblokować tę umiejętność.")
    elif wybor == "3":
        if bohater.level >= 30:
            bohater.dodge_chance += 0.05
            time.sleep(0.4)
            print("Zwiększasz szansę na unik o 5%!")
        else:
            time.sleep(0.3)
            print("Musisz osiągnąć co najmniej 30 poziom, aby odblokować tę umiejętność.")
    elif wybor == "4":
        if bohater.level >= 40:
            bohater.defense += 5
            time.sleep(0.4)
            print("Zwiększono obronę o 5!")
        else:
            time.sleep(0.3)
            print("Musisz osiągnąć co najmniej 40 poziom, aby odblokować tę umiejętność.")
    elif wybor == "5":
        return


def zwykly_atak(postac, opponent):
    damage = max(1, postac.strength)
    if random.randint(1, 100) < postac.critical_chance * 100:
        damage = int(damage * postac.critical_multiplier)
        time.sleep(0.3)
        print("Cios krytyczny!")
        return damage
    return damage


def fire_ball(postac, opponent):
    if postac.mana < 20:
        print("-" * 40)
        time.sleep(0.3)
        print("Nie masz wystarczającej ilości many!")
        return 0
    postac.mana -= 10
    time.sleep(0.5)
    print(" Rzucasz Fire Ball!")
    damage = max(1, postac.strength * 2)
    slabos_wroga = opponent[5]
    if slabos_wroga == "ogien":
        damage = int(damage * 1.5)
        time.sleep(0.3)
        print("Zadajesz dodatkowe obrażenia, ponieważ przeciwnik jest słaby na ogień!")
    if random.randint(1, 100) < postac.critical_chance * 100:
        damage = int(damage * postac.critical_multiplier)
        time.sleep(0.3)
        print("Cios krytyczny!")
    return damage


def HydroPump(postac, opponent):
    if postac.mana < 20:
        print("-" * 40)
        time.sleep(0.3)
        print("Nie masz wystarczającej ilości many!")
        return 0
    postac.mana -= 20
    time.sleep(0.5)
    print(" Używasz Hydro Pump!")
    damage = max(1, postac.strength * 2)
    slabos_wroga = opponent[5]
    if slabos_wroga == "ogien":
        damage = int(damage * 1.5)
        time.sleep(0.3)
        print("Zadajesz dodatkowe obrażenia, ponieważ przeciwnik jest słaby na ogień!")
    if random.randint(1, 100) < postac.critical_chance * 100:
        damage = int(damage * postac.critical_multiplier)
        time.sleep(0.3)
        print("Cios krytyczny!")
    return damage


def Earthquake(postac, opponent):
    if postac.mana < 20:
        print("-" * 40)
        time.sleep(0.3)
        print("Nie masz wystarczającej ilości many!")
        return 0
    postac.mana -= 20
    time.sleep(0.5)
    print(" Używasz Earthquake!")
    damage = max(1, postac.strength * 2)
    slabos_wroga = opponent[5]
    if slabos_wroga == "trawa":
        damage = int(damage * 1.5)
        time.sleep(0.3)
        print("Zadajesz dodatkowe obrażenia, ponieważ przeciwnik jest słaby na trawę!")
    if random.randint(1, 100) < postac.critical_chance * 100:
        damage = int(damage * postac.critical_multiplier)
        time.sleep(0.3)
        print("Cios krytyczny!")
    return damage


def Thunderbolt(postac, opponent):
    if postac.mana < 20:
        print("-" * 40)
        time.sleep(0.3)
        print("Nie masz wystarczającej ilości many!")
        return 0
    postac.mana -= 20
    time.sleep(0.5)
    print(" Używasz Thunderbolt!")
    damage = max(1, postac.strength * 2)
    slabos_wroga = opponent[5]
    if slabos_wroga == "woda":
        damage = int(damage * 1.5)
        time.sleep(0.3)
        print("Zadajesz dodatkowe obrażenia, ponieważ przeciwnik jest słaby na wodę!")
    if random.randint(1, 100) < postac.critical_chance * 100:
        damage = int(damage * postac.critical_multiplier)
        time.sleep(0.3)
        print("Cios krytyczny!")
    return damage


def wybierz_atak(postac, opponent):
    print("a/A - Wykonaj Normalny Atak")
    print("b/B - Fire Ball!")
    print("c/C - Hydro Pump!")
    print("d/D - Earthquake!")
    print("e/E - Thunderbolt!")
    co = input().upper()
    if co == "A":
        return zwykly_atak(postac, opponent)
    if co == "B":
        return fire_ball(postac, opponent)
    if co == "C":
        return HydroPump(postac, opponent)
    if co == "D":
        return Earthquake(postac, opponent)
    if co == "E":
        return Thunderbolt(postac, opponent)
    print("Nie wybrano akcji")
    return 0


def random_oponent():
    opponents = [
        ["Cultists", 15, 3, 10, 5, "elektryczny"],
        ["Scavengers", 10, 3, 15, 3, "ogien"],
        ["Goatmen", 20, 5, 20, 7, "trawa"],
        ["Executioners", 18, 4, 25, 5, "woda"],
    ]
    return choice(opponents)


def level_up(bohater):
    if bohater.experience >= bohater.next_level_exp:
        bohater.level += 1
        bohater.experience -= bohater.next_level_exp
        bohater.next_level_exp = int(bohater.next_level_exp * 1.5)
        bohater.maxlife += 20
        bohater.life = bohater.maxlife
        bohater.maxmana += 10
        bohater.mana = bohater.maxmana
        bohater.strength += 2
        time.sleep(0.3)
        print(f" Gratulacje! Awansowałeś na poziom {bohater.level}!")
        time.sleep(0.3)
        print("Twoje statystyki wzrosły!")




def wybierz_klase():
    print("Wybierz klasę:")
    print("a/A - Wojownik")
    print("b/B - Mag")
    print("c/C - Tank")
    print("d/D - Łucznik")
    co = input().upper()
    if co == "A":
        return "Wojownik"
    if co == "B":
        return "Mag"
    if co == "C":
        return "Tank"
    if co == "D":
        return "Lucznik"
    print("Nie wybrano klasy")
    return None


def imie():
    print("Podaj imię swojej postaci:")
    return input().strip()


def main_gui():
    print("""
          ----------------------------------------
          |         Witaj w grze RPG!            |
          ----------------------------------------
        """)
    time.sleep(0.5)

    name = imie()
    if not name:
        print("Nie podano imienia")
        return None

    klasa = wybierz_klase()
    if klasa == "Wojownik":
        bohater = postacie.Wojownik(name)
    elif klasa == "Mag":
        bohater = postacie.Mag(name)
    elif klasa == "Lucznik":
        bohater = postacie.Lucznik(name)
    elif klasa == "Tank":
        bohater = postacie.Tank(name)
    else:
        print("Nie wybrano klasy")
        return None

    bohater.gold = 100
    bohater.backpack = []
    bohater.equipment = []
    bohater.quest_name = None
    bohater.quest_kills = 0
    bohater.quest_target = 0
    bohater.quest_reward_gold = 0
    bohater.quest_reward_exp = 0
    time.sleep(0.4)
    print(f"Wybrana klasa: {klasa}")
    time.sleep(0.3)
    print(f"Masz {bohater.gold} złota.")
    return bohater


def atak_hero(bohater):
    damage = max(1, bohater.strength)
    if random.randint(1, 100) < bohater.critical_chance * 100:
        damage *= 2
        print("Cios krytyczny!")
    return damage


def atak_przeciwnika(opponent, bohater):
    damage = max(1, opponent[2] - bohater.defense)
    return damage


def samouczek():
    print("\n=== SAMOUCZEK ===")
    time.sleep(0.5)
    print("1 - Poznaj podstawy walki")
    print("2 - Zacznij grę")
    print("3 - Wyjście z gry")

    while True:
        wybor = input("> ").strip()

        if wybor == "1":
            time.sleep(0.4)
            print("Każdy atak zadaje obrażenia.")
            time.sleep(0.3)
            print("Obrażenia nie mogą spaść poniżej 1.")
            time.sleep(0.3)
            print("Czasami trafisz cios krytyczny i podwajasz obrażenia.")
            time.sleep(0.3)
            print("Przeciwnik też cię atakuje, jeśli przeżyje.")
            time.sleep(0.3)
            print("Wpisz 2, aby przejść dalej.")
        elif wybor == "2":
            time.sleep(0.4)
            print("Przechodzisz do głównego lobby gry.")
            time.sleep(0.5)
            return "start"
        elif wybor == "3":
            print("Kończysz grę.")
            return "wyjdz"
        else:
            print("Wybierz 1, 2 lub 3.")


def walka(bohater):
    opponent = random_oponent()
    enemy_name = opponent[0]
    enemy_life = opponent[1]

    time.sleep(0.5)
    print(f"\nSpotykasz przeciwnika...")
    time.sleep(0.7)
    print(f"To {enemy_name}! Przygotuj się do walki!")
    time.sleep(0.5)

    while bohater.life > 0 and enemy_life > 0:
        print("\nWybierz akcję:")
        print("1 - Atak")
        print("2 - Wyjście z gry")
        wybor = input("> ").strip()

        if wybor == "1":
            damage = wybierz_atak(bohater, opponent)
            time.sleep(0.4)
            enemy_life -= damage
            print(f"{bohater.name} zadaje {damage} obrażeń {enemy_name}!")
            time.sleep(0.3)
            print(f"Życie {enemy_name}: {max(enemy_life, 0)}")

            if enemy_life <= 0:
                time.sleep(0.5)
                print(f"Pokonałeś {enemy_name}!")
                bohater.gold += opponent[3]
                bohater.experience += opponent[4]
                time.sleep(0.3)
                print(f"Zdobywasz {opponent[3]} złota i {opponent[4]} doświadczenia!")
                if bohater.quest_name is not None:
                    bohater.quest_kills += 1
                    time.sleep(0.2)
                    print(f"Quest: {bohater.quest_name} ({bohater.quest_kills}/{bohater.quest_target})")
                    if bohater.quest_kills >= bohater.quest_target:
                        questy.zakoncz_questa(bohater)
                level_up(bohater)
                break

            time.sleep(0.6)
            damage_enemy = atak_przeciwnika(opponent, bohater)
            if random.randint(1, 100) < opponent[4] * 100:
                damage_enemy = int(damage_enemy * 2)
                time.sleep(0.3)
                print(f"{enemy_name} trafia cios krytyczny!")
            if random.randint(1, 100) < bohater.dodge_chance * 100:
                time.sleep(0.3)
                print(f"{bohater.name} unika ataku {enemy_name}!")
                continue
            bohater.life -= damage_enemy
            print(f"{enemy_name} zadaje {damage_enemy} obrażeń {bohater.name}!")
            time.sleep(0.3)
            print(f"Życie {bohater.name}: {max(bohater.life, 0)}")
        elif wybor == "2":
            print("Kończysz grę.")
            return
        else:
            print("Nie wybrano akcji.")

    if bohater.life <= 0:
        time.sleep(0.5)
        print(f"{bohater.name} poległ.")
    elif enemy_life <= 0:
        time.sleep(0.4)
        print(f"Zwycięstwo! {bohater.name} kontynuuje przygodę.")


def sklep(bohater):
    while True:
        time.sleep(0.3)
        print("\n=== SKLEP ===")
        print(f"Masz {bohater.gold} złota.")
        print("1 - Mikstura zdrowia (20 zł)")
        print("2 - Mikstura many (15 zł)")
        print("3 - Wzmocnienie siły (30 zł)")
        print("4 - Miecz żelazny (50 zł)")
        print("5 - Zbroja skórzana (45 zł)")
        print("6 - Eliksir życia (60 zł)")
        print("7 - Eliksir many (55 zł)")
        print("8 - Wyjście ze sklepu")

        wybor = input("> ").strip()
        if wybor == "8":
            print("Wracasz do głównego menu.")
            return

        if wybor == "1":
            name = "Mikstura zdrowia"
            price = 20
            kind = "health"
            value = 50
        elif wybor == "2":
            name = "Mikstura many"
            price = 15
            kind = "mana"
            value = 30
        elif wybor == "3":
            name = "Wzmocnienie siły"
            price = 30
            kind = "strength"
            value = 3
        elif wybor == "4":
            name = "Miecz żelazny"
            price = 50
            kind = "sword"
            value = 5
        elif wybor == "5":
            name = "Zbroja skórzana"
            price = 45
            kind = "armor"
            value = 20
        elif wybor == "6":
            name = "Eliksir życia"
            price = 60
            kind = "health"
            value = 100
        elif wybor == "7":
            name = "Eliksir many"
            price = 55
            kind = "mana"
            value = 80
        else:
            print("Wybierz liczbę 1-8.")
            continue

        if bohater.gold < price:
            time.sleep(0.3)
            print("Nie masz wystarczająco złota.")
            continue

        bohater.gold -= price
        bohater.backpack.append((name, kind, value))
        time.sleep(0.4)
        print(f"Kupujesz {name} i odkładasz go do plecaka.")
        time.sleep(0.2)
        print(f"Masz teraz {bohater.gold} złota.")


def plecak(bohater):
    while True:
        print("\n=== PLECAK ===")
        time.sleep(0.3)
        print("1 - Pokaż plecak")
        print("2 - Użyj przedmiotu")
        print("3 - Wyjście")

        wybor = input("> ").strip()
        if wybor == "1":
            if len(bohater.backpack) == 0:
                print("Plecak jest pusty.")
                continue
            i = 1
            while i <= len(bohater.backpack):
                item = bohater.backpack[i - 1]
                print(str(i) + " - " + item[0])
                i += 1
            continue

        if wybor == "2":
            if len(bohater.backpack) == 0:
                print("Plecak jest pusty.")
                continue
            i = 1
            while i <= len(bohater.backpack):
                item = bohater.backpack[i - 1]
                print(str(i) + " - " + item[0])
                i += 1
            try:
                nr = int(input("Wybierz numer przedmiotu do użycia: ").strip())
                item = bohater.backpack[nr - 1]
            except (ValueError, IndexError):
                print("Podano zły numer.")
                continue
            name = item[0]
            kind = item[1]
            value = item[2]
            time.sleep(0.4)
            if kind == "health":
                healed = value
                if bohater.life + healed > bohater.maxlife:
                    healed = bohater.maxlife - bohater.life
                bohater.life += healed
                print("Używasz " + name + " i odzyskujesz " + str(healed) + " życia.")
            elif kind == "mana":
                restored = value
                if bohater.mana + restored > bohater.maxmana:
                    restored = bohater.maxmana - bohater.mana
                bohater.mana += restored
                print("Używasz " + name + " i odzyskujesz " + str(restored) + " many.")
            elif kind == "strength":
                bohater.strength += value
                print("Używasz " + name + " i zyskujesz +" + str(value) + " siły.")
            elif kind == "sword":
                bohater.strength += value
                print("Używasz " + name + " i Twoje obrażenia rosną o " + str(value) + ".")
            elif kind == "armor":
                bohater.maxlife += value
                bohater.life += value
                print("Używasz " + name + " i masz +" + str(value) + " życia.")
            else:
                print("Nieznany przedmiot.")
            bohater.backpack.pop(nr - 1)
            continue

        if wybor == "3":
            return

        print("Wybierz 1 do 3.")


def eksploracja(bohater):
    time.sleep(0.5)
    print("Wyruszasz na eksplorację...")
    time.sleep(1.0)
    random_event = random.randint(1, 3)
    if random_event == 1:
        print("Podczas eksploracji napotykasz grupę bandytów!")
        time.sleep(0.5)
        print("Okradają cię i tracisz 20% swojego złota.")
        bohater.gold = int(bohater.gold * 0.8)
    elif random_event == 2:
        print("Podczas eksploracji znajdujesz ukryty skarb!")
        time.sleep(0.5)
        print("Zyskujesz 50 złota.")
        bohater.gold += 50
    elif random_event == 3:
        print("Podczas eksploracji napotykasz tajemniczego wędrowca.")
        time.sleep(0.5)
        print("Daje ci on magiczny eliksir, który przywraca 50 życia.")
        healed = 50
        if bohater.life + healed > bohater.maxlife:
            healed = bohater.maxlife - bohater.life
        bohater.life += healed
        time.sleep(0.3)
        print(f"Używasz eliksiru i odzyskujesz {healed} życia.")


def trening(bohater):
    time.sleep(0.4)
    print("Bohater trenuje, aby stać się silniejszym!")
    time.sleep(1.0)
    print("Zyskujesz 10 punktów doświadczenia.")
    bohater.experience += 10
    level_up(bohater)


def boss_fight(bohater):
    if bohater.level < 20:
        print("Musisz osiągnąć co najmniej 20 poziom, aby walczyć z bossem.")
        return
    random_boss = random.randint(1, 100)
    if random_boss <= 50:
        boss = bossy.Rakanoth()
    elif random_boss <= 80:
        boss = bossy.Adria()
    else:
        boss = bossy.Diablo()
    time.sleep(0.5)
    print("  Napotykasz potężnego bossa: " + boss.name + "!")
    time.sleep(0.8)

    boss_as_list = [boss.name, boss.life, boss.strength, 0, boss.critical_chance, "brak"]

    while bohater.life > 0 and boss.life > 0:
        print("\nWybierz akcję:")
        print("1 - Atak")
        print("2 - Wyjście z gry")
        wybor = input("> ").strip()

        if wybor == "1":
            damage = wybierz_atak(bohater, boss_as_list)
            time.sleep(0.4)
            boss.life -= damage
            print(f"{bohater.name} zadaje {damage} obrażeń {boss.name}!")
            time.sleep(0.3)
            print(f"Życie {boss.name}: {max(boss.life, 0)}")

            if boss.life <= 0:
                time.sleep(0.6)
                print(f"Pokonałeś {boss.name}!")
                bohater.gold += boss.gold
                bohater.experience += boss.experience
                time.sleep(0.3)
                print(f"Zdobywasz {boss.gold} złota i {boss.experience} doświadczenia!")
                level_up(bohater)
                break

            time.sleep(0.6)
            damage_enemy = max(1, boss.strength - bohater.defense)
            if random.randint(1, 100) < boss.critical_chance * 100:
                damage_enemy = int(damage_enemy * boss.critical_multiplier)
                time.sleep(0.3)
                print(f"{boss.name} trafia cios krytyczny!")
            if random.randint(1, 100) < bohater.dodge_chance * 100:
                time.sleep(0.3)
                print(f"{bohater.name} unika ataku {boss.name}!")
                continue
            bohater.life -= damage_enemy
            print(f"{boss.name} zadaje {damage_enemy} obrażeń {bohater.name}!")
            time.sleep(0.3)
            print(f"Życie {bohater.name}: {max(bohater.life, 0)}")
        elif wybor == "2":
            print("Kończysz grę.")
            return
        else:
            print("Nie wybrano akcji.")


def gra():
    decyzja = samouczek()
    if decyzja == "wyjdz":
        return

    bohater = None

    while True:
        time.sleep(0.3)
        print("""
              ----------------------------------------
              |         GŁÓWNE LOBBY GRY             |
              ----------------------------------------
        """)

        if bohater is None:
            print("1 - Stwórz postać")
            print("2 - Wyjście")
            wybor = input("> ").strip()

            if wybor == "1":
                bohater = main_gui()
                if bohater is None:
                    continue
                time.sleep(0.5)
                print(f"Witaj, {bohater.name}! Twoja przygoda zaczyna się teraz!")
                time.sleep(0.5)
                continue

            if wybor == "2":
                print("Kończysz grę.")
                return

            print("Wybierz 1 lub 2.")
            continue

        print("1 - Walka")
        print("2 - Sklep")
        print("3 - Plecak")
        print("4 - Eksploracja")
        print("5 - Walka z bossem (min. 20 poziom)")
        print("6 - Trening")
        print("7 - Questy")
        print("8 - Drzewko umiejętności")
        print("9 - Statystyki")
        print("10 - Kowal")
        print("11 - Wyjście")

        wybor = input("> ").strip()

        if wybor == "1":
            walka(bohater)
        elif wybor == "2":
            sklep(bohater)
        elif wybor == "3":
            plecak(bohater)
        elif wybor == "4":
            eksploracja(bohater)
        elif wybor == "5":
            boss_fight(bohater)
        elif wybor == "6":
            trening(bohater)
        elif wybor == "7":
            questy.quest_menu(bohater)
        elif wybor == "8":
            drzewko_umiejetnosci(bohater)
        elif wybor == "9":
            ekran_statystyk(bohater)
        elif wybor == "10":
            kowal(bohater)
        elif wybor == "11":
            print("Kończysz grę.")
            return
        else:
            print("Wybierz 1 do 11.")


def main():
    gra()


if __name__ == "__main__":
    main()