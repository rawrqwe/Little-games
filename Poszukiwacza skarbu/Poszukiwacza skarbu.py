import random


def utworz_plansze(rozmiar_planszy):
    plansza = []

    for wiersz in range(rozmiar_planszy):
        for kolumna in range(rozmiar_planszy):
            plansza.append((wiersz, kolumna))
    return plansza


def wyswietlanie_planszy(plansza, pozycja_gracza, rozmiar_planszy):
    for start in range(0, len(plansza), rozmiar_planszy):
        for pole in plansza[start : start + rozmiar_planszy]:
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


def oblicz_odleglosc(pozycja_gracza, pozycja_skarbu):
    gracz_wiersz, gracz_kolumna = pozycja_gracza
    skarb_wiesz, skarb_kolumna = pozycja_skarbu

    return abs(gracz_wiersz - skarb_wiesz) + abs(gracz_kolumna - skarb_kolumna)


def wybierz_poziom_trudnosci():

    while True:
        print("1. Łatwy poziom - 4x4")
        print("2. Łatwy normalny - 5x5")
        print("3. Łatwy trudny - 6x6")
        wybor_trudnosci = input("Podaj wybór: ").strip()

        if wybor_trudnosci == "1":
            rozmiar_planszy = 4
            break
        elif wybor_trudnosci == "2":
            rozmiar_planszy = 5
            break
        elif wybor_trudnosci == "3":
            rozmiar_planszy = 6
            break

        print("Wpisałeś nie poprawna wartość!")

    while True:
        wybor_limitu = input("Podaj limit ruchów(1-99): ").strip()
        try:
            limit_ruchow = int(wybor_limitu)
        except ValueError:
            print("Wpisz liczbę całkowitą.")
            continue

        if 1 <= limit_ruchow <= 99:
            break

        print("Limit musi być od 1 do 99.")

    return rozmiar_planszy, limit_ruchow


def rozegraj_runde(rozmiar_planszy, limit_ruchow):
    plansza = utworz_plansze(rozmiar_planszy)

    pozycja_gracza = (0, 0)
    pozycja_skarbu = random.choice(plansza[1:])

    licznik_ruchow = 0

    wyswietlanie_planszy(plansza, pozycja_gracza, rozmiar_planszy)

    while True:
        print()
        wybor = wybor_gracza()
        stara_pozycja = pozycja_gracza
        pozycja_gracza = ruch_gracz(wybor, pozycja_gracza, plansza)

        if stara_pozycja == pozycja_gracza:
            continue

        licznik_ruchow += 1
        print(f"Ruchy: {licznik_ruchow}/{limit_ruchow}")
        print()
        wyswietlanie_planszy(plansza, pozycja_gracza, rozmiar_planszy)

        if pozycja_gracza == pozycja_skarbu:
            print("Wygrałeś!")
            return

        if licznik_ruchow >= limit_ruchow:
            print("Przegrałeś! Skończyły się ruchy.")
            return

        odleglosc_przed = oblicz_odleglosc(stara_pozycja, pozycja_skarbu)
        odleglosc_po = oblicz_odleglosc(pozycja_gracza, pozycja_skarbu)

        if odleglosc_po < odleglosc_przed:
            print("Cieplej!")
        else:
            print("Zimniej!")


def zapytaj_tak_nie(pytanie):
    while True:
        odpowiedz = input(pytanie).strip().lower()
        if odpowiedz in ("t", "n"):
            return odpowiedz
        print("Wpisz t lub n.")


if __name__ == "__main__":
    ustawienia = wybierz_poziom_trudnosci()
    rozmiar_planszy = ustawienia[0]
    limit_ruchow = ustawienia[1]

    while True:

        rozegraj_runde(rozmiar_planszy, limit_ruchow)

        if zapytaj_tak_nie("Zagraj ponownie (t/n)? ") == "n":
            print("Do zobaczenia :)")
            break

        if zapytaj_tak_nie("Zostawić obecne ustawienia (t/n)? ") == "n":
            rozmiar_planszy, limit_ruchow = wybierz_poziom_trudnosci()

        print("To zaczynam nową rozgrywkę.")
