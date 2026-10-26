import json


def main():

    print("Witam w Quizgame!")
    print("Zaczynajmy!")

    with open("quiz_pytania.json", "r", encoding="utf-8") as plik:
        pytania = json.load(plik)

    ilosc_punktow_gracza = 0

    for i, pytanie in enumerate(pytania, 1):
        for k, v in pytanie.items():
            if k == "tresc":
                print(f"\n{i}. {v}")
            if len(k) < 2:
                print(f"{k} {v}")

        while True:
            try:
                wybor = input("\nTwoja odpowiedź?: ").strip().lower()

                if wybor not in ("a", "b", "c"):
                    raise ValueError

                break
            except ValueError:
                print("Nie ma takiej opcji do wybrania!")

        if wybor == pytanie["poprawna"]:
            print(f"Dobrze! +1 punkt")
            ilosc_punktow_gracza += 1
        else:
            print("Niestety zła odpowiedź")

    print(f"Koniec quizu! Zdobyłeś {ilosc_punktow_gracza} z {len(pytania)}")


if __name__ == "__main__":
    main()
