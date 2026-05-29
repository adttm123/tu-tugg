def sklep(postac, pieniadze, MAXHP,
          Stalowy_miecz, Ulepszony_Stalowy_miecz,
          Mithrilowy_miecz, Excalibur,
          niga, nig, Ekwipunek):

    print("\nWybierz co chcesz kupić")
    print("Stalowy miecz 50 zł - a")
    print("Ulepszony Stalowy miecz 100 zł - b")
    print("Mithrilowy miecz 250 zł - c")
    print("Excalibur 1500 zł - d")
    print("Eliksir życia 30 zł - e")
    print("Ulepszony Eliksir życia 60 zł - f")
    print("Stalowa zbroja 200 zł - g")
    print("Zbroja Zeusa 1500 zł - h")
    print(f"Twoje pieniadze = {pieniadze}")
    inp = input("> ")

    if inp == "a":
        if Stalowy_miecz == 0:
            print("\nKupiłeś już ten miecz!")
        elif pieniadze >= 50:
            postac[1] += Stalowy_miecz
            pieniadze -= 50
            Stalowy_miecz = 0
            print("Kupiono Stalowy miecz Atak +20")
        else:
            print("\nNie masz wystarczająco pieniędzy!")

    elif inp == "b":
        if Ulepszony_Stalowy_miecz == 0:
            print("\nKupiłeś już ten miecz!")
        elif pieniadze >= 100:
            postac[1] += Ulepszony_Stalowy_miecz
            pieniadze -= 100
            Ulepszony_Stalowy_miecz = 0
            print("Kupiono Ulepszony Stalowy miecz Atak +20")
        else:
            print("\nNie masz wystarczająco pieniędzy!")

    elif inp == "c":
        if Mithrilowy_miecz == 0:
            print("\nKupiłeś już ten miecz!")
        elif pieniadze >= 250:
            postac[1] += Mithrilowy_miecz
            pieniadze -= 250
            Mithrilowy_miecz = 0
            print("Kupiono Mithrilowy miecz Atak +40")
        else:
            print("\nNie masz wystarczająco pieniędzy!")

    elif inp == "d":
        if Excalibur == 0:
            print("\nKupiłeś już ten miecz!")
        elif pieniadze >= 1500:
            postac[1] += Excalibur
            pieniadze -= 1500
            Excalibur = 0
            print("Kupiono Excalibur Atak +1500")
        else:
            print("\nNie masz wystarczająco pieniędzy!")

    elif inp == "e":
        if pieniadze >= 30:
            pieniadze -= 30
            print("Dodać do ekwipunku - a")
            print("Użyć - b")
            x = input("> ")
            if x == "a":
                Ekwipunek[0] += 1
                print("Eliksir życia dodany do Eq")
            elif x == "b":
                postac[0] = min(postac[0] + 40, MAXHP)
                print(f"Użyto eliksir! Masz teraz {postac[0]} HP")
        else:
            print("\nNie masz wystarczająco pieniędzy!")

    elif inp == "f":
        if pieniadze >= 60:
            pieniadze -= 60
            print("Dodać do ekwipunku - a")
            print("Użyć - b")
            x = input("> ")
            if x == "a":
                Ekwipunek[1] += 1
                print("Ulepszony eliksir życia dodany do Eq")
            elif x == "b":
                postac[0] = min(postac[0] + 80, MAXHP)
                print(f"Użyto ulepszonego eliksiru! Masz teraz {postac[0]} HP")
        else:
            print("\nNie masz wystarczająco pieniędzy!")

    elif inp == "g":
        if niga == 0:
            print("\nKupiłeś już tą zbroję!")
        elif pieniadze >= 200:
            MAXHP += 200
            pieniadze -= 200
            niga = 0
            print("Kupiono Stalową zbroję! MAXHP +200")
        else:
            print("\nNie masz wystarczająco pieniędzy!")

    elif inp == "h":
        if nig == 0:
            print("\nKupiłeś już tą zbroję!")
        elif pieniadze >= 1500:
            MAXHP += 800
            pieniadze -= 1500
            nig = 0
            print("Kupiono Zbroję Zeusa! MAXHP +800")
        else:
            print("\nNie masz wystarczająco pieniędzy!")

    else:
        print("\nNieznana opcja!")

    return (postac, pieniadze, MAXHP,
            Stalowy_miecz, Ulepszony_Stalowy_miecz,
            Mithrilowy_miecz, Excalibur,
            niga, nig, Ekwipunek)