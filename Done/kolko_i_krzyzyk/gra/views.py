from django.shortcuts import render, redirect
from django.http import HttpResponse


def sprawdz_zwyciesce(plansza):
    uklady = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for a, b, c in uklady:
        if plansza[a] == plansza[b] == plansza[c]:
            if plansza[a] in ("X", "O"):
                return plansza[a]
    return None


def strona_glowna(request):
    if request.method == "POST" and "reset" in request.POST:
        request.session["plansza"] = list(range(1, 10))
        request.session["gracz"] = "X"
        return redirect("strona_glowna")

    plansza = request.session.get("plansza", list(range(1, 10)))
    gracz = request.session.get("gracz", "X")
    zwyciezca = sprawdz_zwyciesce(plansza)
    if request.method == "POST" and zwyciezca is None:
        wybrane_pole = request.POST.get("pole", "")

        if wybrane_pole in [str(i) for i in range(9)]:
            indeks = int(wybrane_pole)
            if plansza[indeks] not in ("X", "O"):
                plansza[indeks] = gracz

                if gracz == "X":
                    gracz = "O"
                else:
                    gracz = "X"

                request.session["plansza"] = plansza
                request.session["gracz"] = gracz

        return redirect("strona_glowna")

    return render(
        request,
        "gra/plansza.html",
        {"plansza": plansza, "gracz": gracz, "zwyciesca": zwyciezca},
    )
