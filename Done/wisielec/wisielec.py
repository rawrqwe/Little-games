import random
from pathlib import Path


def wisielec():
    print("Witam w grze Wisielec !")
    while True:
        print("Mamy dwa poziomy tryby")
        print("1. Szybka gra")
        print("2. Zaawansowana -> Możliwości modyfikowania !")

        while True:
            wybor_gracza_zaawansowany = input("Podaj wybór: ")

            if wybor_gracza_zaawansowany in ("1", "2"):
                break

            print("Wybierz 1 lub 2!")

        if wybor_gracza_zaawansowany == "1":
            with open(
                Path(__file__).parent / "wisielec_szybka_gra.txt", encoding="utf-8"
            ) as plik:
                slowa = plik.read().splitlines()

            print("\n" + "*" * 50)
            print("Szybka gra!")

        if wybor_gracza_zaawansowany == "2":
            print("\n" + "*" * 50)
            print("Gra zaawansowana!")
            print(
                "W tym trybie mozesz ustawić długość słowa oraz ilość możliwych pomyłek :)"
            )
            while True:
                gracza_dlugosci_slowa = input("Podaj długość słowa(3-15): ")

                if gracza_dlugosci_slowa.isdecimal():
                    gracza_dlugosci_slowa = int(gracza_dlugosci_slowa)
                    if 3 <= gracza_dlugosci_slowa <= 15:
                        print(f"Wybrana długość słowa to: {gracza_dlugosci_slowa}")
                        break

                print("Wybierz liczbę od 3 do 15!")

            while True:
                gracz_ilosc_pomylek = input(
                    f"Podaj ilość możliwych pomyłek(1-{gracza_dlugosci_slowa}): "
                )

                if gracz_ilosc_pomylek.isdecimal():
                    gracz_ilosc_pomylek = int(gracz_ilosc_pomylek)
                    if 1 <= gracz_ilosc_pomylek <= gracza_dlugosci_slowa:
                        print(f"\nWybrana ilość pomyłek to: {gracz_ilosc_pomylek} ")
                        break

                print(f"Wybierz liczbę od 1 do {gracza_dlugosci_slowa}")

            with open(
                Path(__file__).parent / "wisielec_zaawansowana_gra.txt",
                encoding="utf-8",
            ) as plik:
                slowa = plik.read().splitlines()

            slowa_wybrana_dlugosc = []
            for slowo in slowa:
                if len(slowo) == gracza_dlugosci_slowa:
                    slowa_wybrana_dlugosc.append(slowo)
            slowa = slowa_wybrana_dlugosc
            print("Zaczynajmy!\n")

        while True:

            slowo = random.choice(slowa)
            if wybor_gracza_zaawansowany == "1":
                ilosc_pomylek = len(slowo)
            else:
                ilosc_pomylek = gracz_ilosc_pomylek
            ukryte_slowo = ["_"] * len(slowo)
            podane_litery = []

            print(" ".join(ukryte_slowo))

            while ilosc_pomylek > 0 and "_" in ukryte_slowo:
                wybor_gracza = input("Podaj litere: ").strip().lower()

                if len(wybor_gracza) != 1 or not wybor_gracza.isalpha():
                    print("Podaj jedną literę!\n")
                    continue

                if wybor_gracza in podane_litery:
                    print("Ta literaz została juz podana!\n")
                    continue

                podane_litery.append(wybor_gracza)

                if wybor_gracza in slowo:
                    for i, litera in enumerate(slowo):
                        if wybor_gracza == litera:
                            ukryte_slowo[i] = litera

                    print("Trafileś !")
                else:
                    ilosc_pomylek -= 1
                    print("Pudło!")

                print(" ".join(ukryte_slowo))
                print(f"Pozostało {ilosc_pomylek} prób !")

            if "_" not in ukryte_slowo:
                print(f"Gratulacje! Wygrałeś! Słowo to: {slowo}")
            else:
                print(f"Przegrałeś! Słowo to: {slowo}")

            while True:
                wybor_gracza_powtórka = input(
                    "\nCo chcesz zrobić?\n"
                    "1. Zagraj ponownie\n"
                    "2. Zmień tryb\n"
                    "3. Zakończ grę\n"
                    "Wybór: "
                ).strip()

                if wybor_gracza_powtórka in ("1", "2", "3"):
                    break

                print("Wybierz 1, 2 lub 3!")

            if wybor_gracza_powtórka == "2":
                break

            if wybor_gracza_powtórka == "3":
                print("Do następnego :)!")
                return


if __name__ == "__main__":
    wisielec()
