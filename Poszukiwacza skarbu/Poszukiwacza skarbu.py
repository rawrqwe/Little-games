import random


def utworz_plansze(rozmiar_planszy):
    plansza = []

    for wiersz in range(rozmiar_planszy):
        for kolumna in range(rozmiar_planszy):
            plansza.append((wiersz, kolumna))
    return plansza


def wyswietlanie_planszy(
    plansza, pozycja_gracza, rozmiar_planszy, odwiedzone_pola, odkryte_pulapki
):
    for start in range(0, len(plansza), rozmiar_planszy):
        for pole in plansza[start : start + rozmiar_planszy]:
            if pole == pozycja_gracza:
                print(f"G", end="  ")
            elif pole in odkryte_pulapki:
                print("X", end=" ")
            elif pole in odwiedzone_pola:
                print("*", end=" ")
            else:
                print(".", end=" ")
        print()


def wybor_gracza():
    while True:
        wybor = input("Twój ruch w/a/s/d lub p (podpowiedź): ").strip().lower()

        if wybor in ("w", "a", "s", "d", "p"):
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
        print("4. Coś trudniejszego :)")
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
        elif wybor_trudnosci == "4":
            while True:
                wybor_trudnosci = input("Podaj rozmiar planszy od 5 do 10: ").strip()
                if wybor_trudnosci in ("5", "6", "7", "8", "9", "10"):
                    rozmiar_planszy = int(wybor_trudnosci)
                    break
                print("Wpisałeś nie poprawna wartość!")
            break

        print("Wpisz poprawną opcję od 1 do 4.")

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

    while True:
        wybor_limitu_pulapek = input(
            f"Podaj ilość pułapek(0 - {rozmiar_planszy **2 -2}): "
        ).strip()
        try:
            liczba_pulapek = int(wybor_limitu_pulapek)
        except ValueError:
            print("Wpisz liczbę całkowitą.")
            continue

        if 0 <= liczba_pulapek <= rozmiar_planszy**2 - 2:
            break

        print(f"Ilość musi być od 0 do {rozmiar_planszy **2 -2}.")

    return rozmiar_planszy, limit_ruchow, liczba_pulapek


def rozegraj_runde(rozmiar_planszy, limit_ruchow, liczba_pulapek):
    plansza = utworz_plansze(rozmiar_planszy)
    pozycja_gracza = (0, 0)
    odwiedzone_pola = {pozycja_gracza}
    pozycja_skarbu = random.choice(plansza[1:])

    licznik_ruchow = 0

    pozycje_pulapek = wylosuj_pulapke(plansza, pozycja_skarbu, liczba_pulapek)
    odkryte_pulapki = set()

    wyswietlanie_planszy(
        plansza, pozycja_gracza, rozmiar_planszy, odwiedzone_pola, odkryte_pulapki
    )

    podpowiedz_uzyta = False

    while True:
        print()
        wybor = wybor_gracza()
        stara_pozycja = pozycja_gracza

        if wybor == "p":
            if podpowiedz_uzyta:
                print("Podpowiedź została już użyta w tej rundzie.")
            else:
                odleglosc = oblicz_odleglosc(pozycja_gracza, pozycja_skarbu)
                print(f"Odległość od skarbu: {odleglosc}")
                podpowiedz_uzyta = True
            continue

        pozycja_gracza = ruch_gracz(wybor, pozycja_gracza, plansza)

        if stara_pozycja == pozycja_gracza:
            continue

        odwiedzone_pola.add(pozycja_gracza)
        licznik_ruchow += 1
        if pozycja_gracza in pozycje_pulapek and pozycja_gracza not in odkryte_pulapki:
            odkryte_pulapki.add(pozycja_gracza)
            licznik_ruchow += 1
            print("Wpadłeś w pułapkę! Zużywasz jeden dodatkowy ruch.")

        print(f"Ruchy: {licznik_ruchow}/{limit_ruchow}")
        print()
        wyswietlanie_planszy(
            plansza, pozycja_gracza, rozmiar_planszy, odwiedzone_pola, odkryte_pulapki
        )

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


def wylosuj_pulapke(plansza, pozycja_skarbu, liczba_pulapek):
    mozliwe_pola = []

    for pole in plansza[1:]:
        if pole != pozycja_skarbu:
            mozliwe_pola.append(pole)

    miejsca_pulapki = []
    for _ in range(liczba_pulapek):
        wylosowane_pole = random.choice(mozliwe_pola)
        miejsca_pulapki.append(wylosowane_pole)
        mozliwe_pola.remove(wylosowane_pole)

    return miejsca_pulapki


if __name__ == "__main__":
    ustawienia = wybierz_poziom_trudnosci()
    rozmiar_planszy = ustawienia[0]
    limit_ruchow = ustawienia[1]
    liczba_pulapek = ustawienia[2]

    while True:

        rozegraj_runde(rozmiar_planszy, limit_ruchow, liczba_pulapek)

        if zapytaj_tak_nie("Zagraj ponownie (t/n)? ") == "n":
            print("Do zobaczenia :)")
            break

        if zapytaj_tak_nie("Zostawić obecne ustawienia (t/n)? ") == "n":
            rozmiar_planszy, limit_ruchow, liczba_pulapek = wybierz_poziom_trudnosci()

        print("To zaczynam nową rozgrywkę.")
