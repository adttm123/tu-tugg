import random
import time
import statystyki as s
from statystyki import postac
import sklep as y
import potwory as p
import inne as i
import windows as w
pieniadze = 0
MAXHP = 200
EXP = 0
LVL = [0, 50]
Ekwipunek = [0, 0]
PA = 1
PF = 1
PK = 1
PL = 1
PKa = 1
Stalowy_miecz = 20
Ulepszony_Stalowy_miecz = 20
Mithrilowy_miecz = 40
Excalibur = 1500
niga = 10
nig = 10
print("--- WITAMY W GRZE! ---")
time.sleep(0.5)
print("\nWybierz swoją klasę:")
time.sleep(0.5)
print("Wojownik  - a")
time.sleep(0.5)
print("Assassin  - b")
time.sleep(0.5)
print("Czarodziej - c")
time.sleep(0.5)
print("Lipiński  - d")
time.sleep(0.5)

inp = input("> ")

if inp == "a":
    s.wojownik()
elif inp == "b":
    s.asssassin()
elif inp == "c":
    s.czarodziej()
elif inp == "d":
    s.Lipiński()
else:
    print("Zła opcja, domyślnie Wojownik.")
    time.sleep(0.5)
    s.wojownik()
while postac[0] > 0:
    i.pokaz_menu_glowne(postac, MAXHP, LVL, pieniadze)
    potwor = p.losuj_potwora()
    boss = p.losuj_bossa()
    inp = input("> ")
    if inp == "a":

        print(f"\nNa twojej drodze stanął {potwor[0]}! Ma {potwor[1]} HP i {potwor[2]} ataku.")
        time.sleep(0.5)
        print("\nWalka! - a")
        time.sleep(0.5)
        print("Ucieczka! - b")
        time.sleep(0.5)
        inp = input("> ")

        if inp == "a":
            print(f"\n--- WALKA Z {potwor[0]} ---")
            time.sleep(0.5)
            while potwor[1] > 0 and postac[0] > 0:
                time.sleep(0.5)
                print(f"Twoje HP: {postac[0]}")
                time.sleep(0.5)
                print(f"HP {potwor[0]}: {potwor[1]}")
                time.sleep(0.5)
                postac[0] -= potwor[2]
                potwor[1] -= postac[1]
                time.sleep(0.5)

            if potwor[1] <= 0 and postac[0] > 0:
                zdobyte = random.randint(10, 100)
                zdobyt = random.randint(2, 10)
                pieniadze += zdobyte
                LVL[0] += zdobyt
                if LVL[0] >= LVL[1]:
                    EXP += 1
                    LVL[0] -= LVL[1]
                    LVL[1] += 5
                print(f"\nPokonałeś {potwor[0]}! Zdobywasz {zdobyte} złotych i {zdobyt} expa")
                time.sleep(0.5)

                if potwor[0] == "Ultra goblin":
                    l = random.randint(1,100)
                    if l <= 10 and PA > 0:
                            print("Zdobyłeś również pierścień Ataku. +20 do Ataku")
                            time.sleep(0.5)
                            postac[1] += 20
                            PA -= 1
                            time.sleep(0.5)
                    elif l >=99 and PF > 0:
                                    print("Zdobyłeś również pierścień Antymaga. +100 do Ataku")
                                    time.sleep(0.5)
                                    postac[1] += 100
                                    PF -= 1
                                    time.sleep(0.5)
                elif potwor[0] == "Scylla":
                    g = random.randint(1,100)
                    if g == 100:
                        if PK > 0:
                            print("Zdobyłeś również Kołczan Prawilności. +100 do MAXHP")
                            time.sleep(0.5)
                            MAXHP += 100
                            PK -= 1
                            time.sleep(0.5)

                print(f"Masz teraz {pieniadze} złotych.")
                time.sleep(0.5)
                print(f"LVL:{EXP}")
                time.sleep(0.5)
            elif postac[0] <= 0:
                print("\nZostałeś pokonany...")
                time.sleep(0.5)
                break

        elif inp == "b":
            print("Próbujesz uciec...")
            time.sleep(0.5)
            if random.randint(0, 1) == 1:
                print("Udało ci się uciec!")
                time.sleep(0.5)
            else:
                print(f"Nie udało ci się uciec! {potwor[0]} cię dopada!")
                time.sleep(0.5)
                postac[0] -= potwor[2]
                print(f"{potwor[0]} zadaje ci {potwor[2]} obrażeń!")
                time.sleep(0.5)

    elif inp == "b":
        (postac, pieniadze, MAXHP,
        Stalowy_miecz, Ulepszony_Stalowy_miecz,
        Mithrilowy_miecz, Excalibur,
        niga, nig, Ekwipunek) = y.sklep(
            postac, pieniadze, MAXHP,
            Stalowy_miecz, Ulepszony_Stalowy_miecz,
            Mithrilowy_miecz, Excalibur,
            niga, nig, Ekwipunek
        )

    elif inp == "c":
        if EXP < 20:
            print("Musisz mieć 20 LVL aby odblokować walkę z BOSSEM")
            time.sleep(0.5)
        else:
            while boss[1] > 0 and postac[0] > 0:
                print(f"Twoje HP: {postac[0]}/{MAXHP}  HP Bossa: {boss[1]}")
                time.sleep(0.5)
                print(f"Ekwipunek: Eliksir życia:{Ekwipunek[0]} Ulepszony Eliksir życia{Ekwipunek[1]}")
                time.sleep(0.5)
                print("\nAtak - a")
                time.sleep(0.5)
                print("Ekwipunek - e")
                time.sleep(0.5)
                inp = input("> ")
                
                if inp == "a":
                        print(f"\n--- WALKA Z {boss[0]} ---")
                        time.sleep(0.5)
                        while boss[1] > 0 and postac[0] > 0:
                            time.sleep(0.5)
                            print(f"Twoje HP: {postac[0]}")
                            time.sleep(0.5)
                            print(f"HP {boss[0]}: {boss[1]}")
                            time.sleep(0.5)
                            postac[0] -= boss[2]
                            boss[1] -= postac[1]
                            time.sleep(0.5)
                        if boss[1] <= 0 and postac[0] > 0:
                                zdoby = random.randint(100, 1000)
                                zdob = random.randint(20, 100)
                                pieniadze += zdoby
                                LVL[0] += zdob
                                if LVL[0] >= LVL[1]:
                                    EXP += 1
                                    LVL[0] -= LVL[1]
                                    LVL[1] += 5
                                print(f"\nPokonałeś {boss[0]}! Zdobywasz {zdoby} złotych i {zdob} expa")
                                time.sleep(0.5)
                                if boss[0] == "Siegebreaker_Assault_Beast":
                                    k = random.randint(1,100)
                                    if k <= 10 and PL > 0:
                                            print("Zdobyłeś również pierścień Lemurów. +200 do Ataku")
                                            time.sleep(0.5)
                                            postac[1] += 200
                                            PL -= 1
                                            time.sleep(0.5)
                                    elif k >=99 and PKa > 0:
                                                    print("Zdobyłeś również pierścień Kastiego. +1000 do Ataku")
                                                    time.sleep(0.5)
                                                    postac[1] += 1000
                                                    PKa -= 1
                                                    time.sleep(0.5)
                                elif boss[0] == "Diablo":
                                            time.sleep(0.5)
                                            print("--- GRATULACJE WYGRAŁEŚ!!! ---")
                                            time.sleep(0.5)
                                            print("Grę tworzyli:")
                                            time.sleep(0.5)
                                            print("Kod:Adam")
                                            time.sleep(0.5)
                                            print("Grafika:Adam")
                                            time.sleep(0.5)
                                            print("Dzwięk:Adam")
                                            time.sleep(0.5)
                                            print("Tłumaczenie:Adam")
                                            time.sleep(0.5)
                                            print("Audiodeskrypcja:Adam")
                                            time.sleep(0.5)
                                            print("Reżyser:Adam")
                                            time.sleep(0.5)
                                            print("Redaktor:Adam")
                                            time.sleep(0.5)
                                            print("Pomysłodawca:Adam")
                                            time.sleep(0.5)
                                            print("Deco:Adam")
                                            time.sleep(0.5)
                                            print("Lektor:Adam")
                                            time.sleep(0.5)
                                            print("Hm:Adam")
                                            time.sleep(0.5)
                elif inp == "e":
                    print("Eliksir życia - a")
                    time.sleep(0.5)
                    print("Ulepszony Eliksir życia - b")
                    time.sleep(0.5)
                    inp = input("> ")
                    if inp == "a" and Ekwipunek[0] > 0:
                        Ekwipunek[0] -= 1
                        postac[0] += 40
                        postac[0] = min(postac[0], MAXHP)
                        print("Użyto Eliksir życia! +40 HP")
                        time.sleep(0.5)
                    elif inp == "b" and Ekwipunek[1] > 0:
                        Ekwipunek[1] -= 1
                        postac[0] += 80
                        postac[0] = min(postac[0], MAXHP)
                        print("Użyto Ulepszonego Elikiru życia! +80 HP")
                        time.sleep(0.5)
                    else:
                        print("Brak potek lub zła opcja!")
                        time.sleep(0.5)
    elif inp == "Malutki":
        w.fake_hack()
