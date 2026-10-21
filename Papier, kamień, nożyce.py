import random
import sys

print("*" * 50)
print("Papier, kamień, nożyce\n")
print("Czy chcesz zagrać?\n1. Tak\n2. Nie\n")

while True:
    wybor_gracza = input("Podaj wybór: ").strip()

    if wybor_gracza == "1":
        print("\nWięc zaczynajmy!\n")
        break
    elif wybor_gracza == "2":
        print("\nNa razie!")
        sys.exit()
    else:
        print("Niepoprawny wybór! Wpisz 1 albo 2.\n")

while True:
    try:
        ilosc_wygranych = int(input("Podaj, do ilu wygranych chcesz grać: "))

        if ilosc_wygranych > 0:
            break

        print("Podaj liczbę większą od zera.\n")

    except ValueError:
        print("Wpisz liczbę całkowitą, np. 3.\n")

if ilosc_wygranych > 7:
    print("\nCałkiem sporo :)")

print("\nPowodzenia!")
print("\n1. Kamień\n2. Papier\n3. Nożyce\n")

ilosc_wygranych_gracz = 0
ilosc_wygranych_PC = 0

dostepne_mozliwosci = ["Kamień", "Papier", "Nożyce"]

while True:
    gracz_wybor = input("Podaj cyfrę lub pierwszą literę: ").strip().lower()

    if gracz_wybor not in ["1", "2", "3", "k", "p", "n"]:
        print("Niepoprawny wybór! Wpisz 1, 2, 3 albo k, p, n.\n")
        continue

    pc_wybor = random.choice(dostepne_mozliwosci)
    print(f"\nKomputer wybrał: {pc_wybor}")

    if gracz_wybor == "1" or gracz_wybor == "k":
        if pc_wybor == "Kamień":
            print("Remis! Nikt nie dostaje punktu.")
        elif pc_wybor == "Papier":
            print("Punkt dla komputera!")
            ilosc_wygranych_PC += 1
        else:
            print("Punkt dla gracza!")
            ilosc_wygranych_gracz += 1

    elif gracz_wybor == "2" or gracz_wybor == "p":
        if pc_wybor == "Kamień":
            print("Punkt dla gracza!")
            ilosc_wygranych_gracz += 1
        elif pc_wybor == "Papier":
            print("Remis! Nikt nie dostaje punktu.")
        else:
            print("Punkt dla komputera!")
            ilosc_wygranych_PC += 1

    elif gracz_wybor == "3" or gracz_wybor == "n":
        if pc_wybor == "Kamień":
            print("Punkt dla komputera!")
            ilosc_wygranych_PC += 1
        elif pc_wybor == "Papier":
            print("Punkt dla gracza!")
            ilosc_wygranych_gracz += 1
        else:
            print("Remis! Nikt nie dostaje punktu.")

    print(f"Wynik: gracz {ilosc_wygranych_gracz}" f" : {ilosc_wygranych_PC} komputer\n")

    if ilosc_wygranych_gracz == ilosc_wygranych:
        print(
            f"Gracz wygrał wynikiem "
            f"{ilosc_wygranych_gracz} do {ilosc_wygranych_PC}!"
        )
        break

    elif ilosc_wygranych_PC == ilosc_wygranych:
        print(
            f"Komputer wygrał wynikiem "
            f"{ilosc_wygranych_PC} do {ilosc_wygranych_gracz}!"
        )
        break
