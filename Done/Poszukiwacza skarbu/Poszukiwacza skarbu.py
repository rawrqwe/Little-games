import random

plansza = [
    (0, 0),
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 0),
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 0),
    (2, 1),
    (2, 2),
    (2, 3),
    (3, 0),
    (3, 1),
    (3, 2),
    (3, 3),
]

gracz_kolumna = 0
gracz_wiersz = 0
pozycja_gracza = (gracz_wiersz, gracz_kolumna)

pozycja_skarby = random.choice(plansza[1:])


def wyswietlanie_planszy(plansza, pozycja_gracza):

    for start in range(0, len(plansza), 4):
        for pole in plansza[start : start + 4]:
            if pole == pozycja_gracza:
                print(f"G", end="  ")
            else:
                print(".", end=" ")
        print()


def wybor_gracza():
    while True:
        wybor = input("Twój ruch w/a/s/d: ").strip().lower()

        if wybor in ("w", "a", "s", "d"):
            return wybor

        print("Wpisałeś nie poprawna wartość!")


def ruch_gracz(wybor_gracza, pozycja_gracza, plansza):
    wiersz, kolumna = pozycja_gracza

    if wybor_gracza == "w":
        wiersz -= 1
    elif wybor_gracza == "s":
        wiersz += 1
    elif wybor_gracza == "a":
        kolumna -= 1
    elif wybor_gracza == "d":
        kolumna += 1
    else:
        return pozycja_gracza

    nowa_pozycja = (wiersz, kolumna)

    if nowa_pozycja in plansza:
        return nowa_pozycja

    print("Nie możesz wyjść poza planszę!")
    return pozycja_gracza


if __name__ == "__main__":
    wyswietlanie_planszy(plansza, pozycja_gracza)
    while True:
        wybor = wybor_gracza()
        pozycja_gracza = ruch_gracz(wybor, pozycja_gracza, plansza)
        wyswietlanie_planszy(plansza, pozycja_gracza)

        if pozycja_gracza == pozycja_skarby:
            print("Wygrałeś!")
            break
