import time
import os
import random

FAKE_FILES = [
    r"C:\Windows\System32\kernel32.dll",
    r"C:\Windows\System32\config\SYSTEM",
    r"C:\Windows\System32\drivers\disk.sys",
    r"C:\Users\User\Documents\save1.dat",
    r"C:\Program Files\Game\config.ini",
]

def fake_hack():
    os.system("cls")
    print("Malutki zjada windowsa!")
    time.sleep(1)
    print("Uruchamianie narzędzia naprawy systemu...")
    time.sleep(1)
    for _ in range(30):
        n = random.randint(100000, 999999)
        print(f"[LOG] Kod błędu: {n}")
        time.sleep(0.05)

    print("\nSkanowanie plików systemowych...\n")
    time.sleep(1)

    for path in FAKE_FILES:
        print(f"Usuwanie: {path}")
        time.sleep(0.6)

    print("\nTrwa czyszczenie rejestru...")
    for i in range(0, 101, 5):
        print(f"Postęp: {i}%")
        time.sleep(0.1)
    while True:
        print(f"{random.randint(1000000000000000000000000000000000000000000000000000000000000000000000000000, 9999999999999999000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)}")
        
fake_hack()