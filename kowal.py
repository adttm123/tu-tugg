
import time


def kowal(bohater):
    time.sleep(0.3)
    print("\n" + "=" * 45)
    print("          KOWAL  ")
    print("=" * 45)
    time.sleep(0.4)
    print("Witaj w kuźni! Co mogę dla ciebie zrobić?")
    time.sleep(0.3)

    while True:
        print("\n" + "-" * 45)
        print(f"   Twoje złoto: {bohater.gold}")
        print("-" * 45)
        print("1 - Ulepsz broń       (+3 siły,   koszt: 50 zł)")
        print("2 - Ulepsz zbroję     (+5 obrony, koszt: 60 zł)")
        print("3 - Zahartuj broń     (+5% kryt,  koszt: 80 zł)")
        print("4 - Naprawa ekwipunku (+30 HP,    koszt: 40 zł)")
        print("5 - Wykuj legendarną broń          koszt: 200 zł)")
        print("6 - Wyjście z kuźni")
        print("-" * 45)

        wybor = input("> ").strip()

        if wybor == "6":
            time.sleep(0.3)
            print("Kowal: Wracaj, gdy będziesz potrzebował!")
            time.sleep(0.3)
            return

        elif wybor == "1":
            koszt = 50
            if bohater.gold < koszt:
                time.sleep(0.3)
                print("Kowal: Nie masz wystarczająco złota!")
                continue
            bohater.gold -= koszt
            bohater.strength += 3
            time.sleep(0.5)
            print("Kowal uderza w kowadło")
            time.sleep(0.8)
            print(f"Broń ulepszona! Twoja siła wzrosła do {bohater.strength}!")
            time.sleep(0.3)
            print(f"Pozostałe złoto: {bohater.gold} zł")

        elif wybor == "2":
            koszt = 60
            if bohater.gold < koszt:
                time.sleep(0.3)
                print("Kowal: Nie masz wystarczająco złota!")
                continue
            bohater.gold -= koszt
            bohater.defense += 5
            time.sleep(0.5)
            print("Kowal zakuwa płyty zbroi")
            time.sleep(0.8)
            print(f"Zbroja ulepszona! Twoja obrona wzrosła do {bohater.defense}!")
            time.sleep(0.3)
            print(f"Pozostałe złoto: {bohater.gold} zł")

        elif wybor == "3":
            koszt = 80
            if bohater.gold < koszt:
                time.sleep(0.3)
                print("Kowal: Nie masz wystarczająco złota!")
                continue
            bohater.gold -= koszt
            bohater.critical_chance += 0.05
            time.sleep(0.5)
            print("Kowal ostrzy i hartuje ostrze w ogniu ")
            time.sleep(0.8)
            print(f"Broń zahartowana! Szansa na cios krytyczny: {int(bohater.critical_chance * 100)}%!")
            time.sleep(0.3)
            print(f"Pozostałe złoto: {bohater.gold} zł")

        elif wybor == "4":
            koszt = 40
            if bohater.gold < koszt:
                time.sleep(0.3)
                print("Kowal: Nie masz wystarczająco złota!")
                continue
            bohater.gold -= koszt
            naprawione = 30
            if bohater.life + naprawione > bohater.maxlife:
                naprawione = bohater.maxlife - bohater.life
            bohater.life += naprawione
            time.sleep(0.5)
            print("Kowal naprawia twój ekwipunek i opatruje rany")
            time.sleep(0.8)
            print(f"Ekwipunek naprawiony! Odzyskujesz {naprawione} HP.")
            print(f"HP: {bohater.life}/{bohater.maxlife}")
            time.sleep(0.3)
            print(f"Pozostałe złoto: {bohater.gold} zł")

        elif wybor == "5":
            koszt = 200
            if bohater.gold < koszt:
                time.sleep(0.3)
                print("Kowal: To kosztuje 200 złota. Wróć gdy będziesz bogatszy!")
                continue
            # Sprawdź czy już ma legendarną broń
            if hasattr(bohater, "legendarna_bron") and bohater.legendarna_bron:
                time.sleep(0.3)
                print("Kowal: Już posiadasz legendarną broń. Jedna wystarczy!")
                continue
            bohater.gold -= koszt
            bohater.strength += 10
            bohater.critical_chance += 0.10
            bohater.critical_multiplier += 0.5
            bohater.legendarna_bron = True
            time.sleep(0.5)
            print("Kowal przez długą chwilę kuje w ciszy")
            time.sleep(1.2)
            print("Ogień bucha z pieca ")
            time.sleep(0.8)
            print("Metal iskrzy i świeci złotym blaskiem ")
            time.sleep(0.8)
            print("=" * 45)
            print("    LEGENDARNA BROŃ WYKUTA!  ")
            print("  +10 siły, +10% kryt, +0.5 mnożnik kryt!")
            print("=" * 45)
            time.sleep(0.5)
            print(f"Pozostałe złoto: {bohater.gold} zł")

        else:
            print("Wybierz opcję 1-6.")