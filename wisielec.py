def wisielec():
    print("Witam w grze Wisielec !")
    # TODO: Dodać poziomy trudności
    # losowe słowo

    while True:
        slowo = "python"
        ilosc_pomylek = 6
        ukryte_slowo = ["_"] * len(slowo)
        podane_litery = []

        print(" ".join(ukryte_slowo))

        while ilosc_pomylek > 0 and "_" in ukryte_slowo:
            wybor_gracza = input("Podaj litere: ").strip().lower()

            if len(wybor_gracza) != 1 or not wybor_gracza.isalpha():
                print("Podaj jedna literę!")
                continue

            if wybor_gracza in podane_litery:
                print("Ta literaz została juz podana!")
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
                "Chcesz zagrać jeszcze raz?\n" "1. Tak\n" "2. Nie\n Wybór: "
            ).strip()

            if wybor_gracza_powtórka in ("1", "2"):
                break

            print("Wybierz 1 lub 2!")

        if wybor_gracza_powtórka == "2":
            print("Do następnego :)!")
            break


if __name__ == "__main__":
    wisielec()
