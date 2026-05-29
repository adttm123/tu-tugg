import time
def pokaz_menu_glowne(postac, MAXHP, LVL, pieniadze):
    print("\nWalka - a")
    time.sleep(0.5)
    print("Sklep - b")
    time.sleep(0.5)
    print("Walka z BOSSEM (LVL 20) - c")
    time.sleep(0.5)
    print(f"Twoje pieniadze = {pieniadze}")
    time.sleep(0.5)
    print(f"LVL: {LVL[0]}/{LVL[1]}")
    time.sleep(0.5)
    print(f"HP: {postac[0]}/{MAXHP}")
    time.sleep(0.5)
