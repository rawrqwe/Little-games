def main():

    print("Witam w Quizgame!")
    print("Zaczynajmy!")

    pytania = [
        {
            "tresc": "Która funkcja wyświetla tekst?",
            "a": "input()",
            "b": "print()",
            "c": "int()",
            "poprawna": "b",
        },
        {
            "tresc": "Która funkcja pobiera tekst od użytkownika?",
            "a": "input()",
            "b": "print()",
            "c": "len()",
            "poprawna": "a",
        },
        {
            "tresc": "Ile wynosi 3 * 4?",
            "a": "7",
            "b": "34",
            "c": "12",
            "poprawna": "c",
        },
        {
            "tresc": "Co zwróci len('Python')?",
            "a": "5",
            "b": "6",
            "c": "7",
            "poprawna": "b",
        },
        {
            "tresc": "Który zapis tworzy listę?",
            "a": "[1, 2, 3]",
            "b": "(1, 2, 3)",
            "c": "{1, 2, 3}",
            "poprawna": "a",
        },
        {
            "tresc": "Jaki indeks ma pierwszy element listy?",
            "a": "1",
            "b": "-1",
            "c": "0",
            "poprawna": "c",
        },
        {
            "tresc": "Co robi break?",
            "a": "Kończy najbliższą pętlę",
            "b": "Zawsze kończy cały program",
            "c": "Rozpoczyna pętlę od nowa",
            "poprawna": "a",
        },
        {
            "tresc": "Co zwróci 'KOT'.lower()?",
            "a": "'KOT'",
            "b": "'kot'",
            "c": "'Kot'",
            "poprawna": "b",
        },
        {
            "tresc": "Jakie liczby otrzymasz z range(1, 4)?",
            "a": "1, 2, 3, 4",
            "b": "0, 1, 2, 3",
            "c": "1, 2, 3",
            "poprawna": "c",
        },
        {
            "tresc": "Który operator sprawdza, czy dwie wartości są równe?",
            "a": "=",
            "b": "==",
            "c": "!=",
            "poprawna": "b",
        },
    ]

    ilosc_punktow_gracza = 0

    for i, pytanie in enumerate(pytania, 1):
        for k, v in pytanie.items():
            if k == "tresc":
                print(f"\n{i}. {v}")
            if len(k) < 2:
                print(f"{k}) {v}")

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
