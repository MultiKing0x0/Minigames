def eur_usd_converter():
    while True:
        betrag = input("Gib den gewünschten Betrag an: ")
        try:
            betrag = float(betrag)
            währung = input("Gib die Währung des so eben genannten Betrags an (eur oder usd): ").lower()
            if währung in ("eur", "euro"):
                neue_währung = betrag * 1.167
                neue_währung = round(neue_währung, 2)
                print(f"{betrag}€ sind umgerechnet {neue_währung}$")
            elif währung  in ("usd", "dollar"):
                neue_währung = betrag / 1.167
                neue_währung = round(neue_währung, 2)
                print(f"{betrag}$ sind umgerechnet {neue_währung}€")
            else:
                print(f"{währung} ist keine Währung. Bitte gib eur für EURO an oder usd für US-DOLLAR!")
        except ValueError:
            print(f"{betrag} ist keine Zahl. Bitte gib eine Zahl ein.")

print(eur_usd_converter())