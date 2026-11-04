import random
import time
import os


def main():

    print("*" * 50)
    print("Witam w gre o super nazwie!\n#__Pamięć__#\n")
    print(
        "Gra ma proste zasady.\n 1.Musisz zapmaiętać wyświetlaną liczbe a następnie ją poprawnie zapisać zapisać\n 2.Patrz punkt pierwszy :)\n"
    )

    print("Zaczynajmny ?")

    while input("Naciśnij sam Enter, aby przejść dalej...") != "":
        print("Nie wpisuj tekstu — naciśnij tylko Enter.")

    lvl_up = 10
    wynik = 0

    while True:

        losowa_liczba = random.choice(range(lvl_up, 10 * lvl_up))

        print()
        print(f"Liczba to: {losowa_liczba}")
        time.sleep(2.5)
        os.system("cls")

        # Wybór gracza -> liczba
        while True:

            wybor_gracza = input("Podaj liczbe: ").strip()

            if (
                len(wybor_gracza) != len(str(losowa_liczba))
                or not wybor_gracza.isdigit()
            ):
                print("Podaj poprawną liczbę!")
                continue

            if wybor_gracza == str(losowa_liczba):
                lvl_up *= 10
                wynik += 1
                print(f"Brawo. Podałeś prawidołową liczbę: {losowa_liczba}")
            else:
                print(f"Niestety! Poprawna liczba: {losowa_liczba}")
                print(f"Liczba wygranych rund: {wynik}")

            # Wybór gracza czy gramy dalej
            while True:

                wybor_gracza_2 = input("Gramy dalej (Y/N)? ").strip().lower()

                if wybor_gracza_2 in ("y", "n"):
                    break

                print("Podaj poprawną literę!")

            if wybor_gracza_2 == "n":
                return
            break


if __name__ == "__main__":
    main()
