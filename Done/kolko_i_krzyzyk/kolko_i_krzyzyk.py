# tworzenie planszy
plansza = []
for x in range(1, 10, 1):
    plansza.append(x)


def wyswietalnie_planszy(plansza):
    print(f"{plansza[0]} | {plansza[1]} | {plansza[2]}")
    print(f"{plansza[3]} | {plansza[4]} | {plansza[5]}")
    print(f"{plansza[6]} | {plansza[7]} | {plansza[8]}")


podane_liczby_graczy = []


def wybor_graczy(podane_liczby_graczy, gracz):
    while True:
        pole = input(f"Podaj numer pola dla '{gracz}': ").strip()
        if pole in "123456789" and len(pole) == 1:
            if pole in podane_liczby_graczy:
                print("To miejsce jest już zajęte")
                continue
            podane_liczby_graczy.append(pole)
            return pole
        print("Podaj cyfrę od 1 do 9!")


def gracza_x():
    return wybor_graczy(podane_liczby_graczy, "x")


def gracza_y():
    return wybor_graczy(podane_liczby_graczy, "y")


def czy_wygrana(plansza, gracz):
    uklady = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 4, 8),
        (2, 4, 6),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
    ]

    for a, b, c in uklady:
        if plansza[a] == plansza[b] == plansza[c] == gracz:
            return True
    return False


def main():
    print("Witamy w grze kółko i krzyzyk!")
    wyswietalnie_planszy(plansza)
    while True:

        pole_x = gracza_x()
        plansza[int(pole_x) - 1] = "x"
        wyswietalnie_planszy(plansza)
        wygrana = czy_wygrana(plansza, "x")
        if wygrana == True:
            return print("Gracz 'x' wygrał")

        if len(podane_liczby_graczy) == 9:
            print("Remis! Żaden z graczy nie wygrał")
            return

        pole_y = gracza_y()
        plansza[int(pole_y) - 1] = "y"
        wyswietalnie_planszy(plansza)
        wygrana = czy_wygrana(plansza, "y")
        if wygrana == True:
            return print("Gracz 'y' wygrał")


if __name__ == "__main__":
    main()
