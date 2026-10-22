import random


def main():
    while True:
        print("Zaczynam grę!\n")

        gracz_kostka = random.choice(range(1, 7))
        pc_kostka = random.choice(range(1, 7))
        status = ""

        if gracz_kostka > pc_kostka:
            status = "Wygrałeś!\n"
        elif gracz_kostka < pc_kostka:
            status = "Przegrałeś!\n"
        else:
            status = "Remis!\n"

        print(f"Twój rzut: {gracz_kostka}")
        print(f"Rzut komputera: {pc_kostka}")
        print(status)

        while True:
            print("1 — zagraj ponownie")
            print("0 — zakończ")

            gracz_wybor = input("Twój wybór: ").strip()

            match gracz_wybor:
                case "1":
                    print("Zaczynam nowa rundę!")
                    break
                case "0":
                    print("Kończymy grę")
                    return
                case _:
                    print("Nie ma takiej opcji!")


if __name__ == "__main__":
    main()
