import random


def main():

    print("*" * 40)
    print("Zgadnij liczbe od 1 do 20!")
    print("Zaczynajmy")

    pc_losuje = random.choice(range(1, 21))
    ilosc_prob = 0
    while True:
        try:
            gracz_liczba = int(input("\nPodaj liczbe: "))
        except ValueError:
            print("Podałeś złą wartość!")
            continue

        if gracz_liczba < pc_losuje:
            print("Za mało!")
            ilosc_prob += 1
        elif gracz_liczba > pc_losuje:
            print("Za dużo!")
            ilosc_prob += 1
        else:
            ilosc_prob += 1
            print(f"\nBrawo! Zgadłeś w {ilosc_prob} próbach!")
            print(f"Liczba to {pc_losuje}")
            break


if __name__ == "__main__":
    main()
