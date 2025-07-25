import random

while True:
    programm = input("Welches Programm möchtest du testen? (rock_paper_scissors, zahlenratespiel, würfeln, taschenrechner, währungsrechner, temperaturrechner oder gewichtsrechner): ").lower().strip()

    # Währungsrechner
    if programm in ("währungsrechner", "währungsumrechner", "euro", "usd", "eurusd", "währungsumrechner", "währung", "currency", "eur", "usd"):
        while True:
            betrag = input("Gib den gewünschten Betrag an: ")
            try:
                betrag = float(betrag)
                währung = input("Gib die Währung des so eben genannten Betrags an (eur oder usd): ").lower()
                if währung in ("eur", "euro"):
                    neue_währung = betrag * 1.167
                    neue_währung = round(neue_währung, 2)
                    print(f"{betrag}€ sind umgerechnet {neue_währung}$")
                    break
                elif währung  in ("usd", "dollar"):
                    neue_währung = betrag / 1.167
                    neue_währung = round(neue_währung, 2)
                    print(f"{betrag}$ sind umgerechnet {neue_währung}€")
                    break
                else:
                    print(f"{währung} ist keine Währung. Bitte gib eur für EURO an oder usd für US-DOLLAR!")
            except ValueError:
                print(f"{betrag} ist keine Zahl. Bitte gib eine Zahl ein.")
    #Zahlenratespiel
    elif programm in ("zahlenratespiel", "zahlenraten", "zahlenraten", "zahlenraten-spiel", "zahlenratengame", "zahlenratengame"):
        print("Willkommen zum Zahlenratespiel!")
        print("Ich denke an eine Zahl zwischen 1 und 100. Versuche sie zu erraten!")
        zahl = random.randint(1, 100)
        versuche = 0
        while True:
            nutzer_eingabe = input("Gib deine Schätzung ein: ")
            try:
                nutzer_eingabe = int(nutzer_eingabe)
                versuche += 1
                if nutzer_eingabe < zahl:
                    print("Zu niedrig! Versuch es nochmal.")
                elif nutzer_eingabe > zahl:
                    print("Zu hoch! Versuch es nochmal.")
                else:
                    print(f"Herzlichen Glückwunsch! Du hast die Zahl {zahl} in {versuche} Versuchen erraten!")
                    break
            except ValueError:
                print("Bitte gib eine gültige Zahl ein.")
    # Rock, Paper, Scissors
    elif programm in ("rockpaperscissors", "rock_paper_scissors", "rps"):
        auswahl = ("r", "p", "s")
        while True:
            nutzer_will = input("Möchtest du ein Spiel spielen? (ja/nein): ").lower().strip()
            if nutzer_will in ("ja", "j", "yes", "y"):
                nutzer_wahl = input("Choose rock, paper or scissors(r, p, s): ").lower().strip()
                computer_wahl = random.choice(auswahl)
                if computer_wahl == "r":
                    computer_wahl = "rock"
                elif computer_wahl == "p":
                    computer_wahl = "paper"
                elif computer_wahl == "s":
                    computer_wahl = "scissors"
                if nutzer_wahl == "r":
                    nutzer_wahl = "rock"
                elif nutzer_wahl == "p":
                    nutzer_wahl = "paper"
                elif nutzer_wahl == "s":
                    nutzer_wahl = "scissors"
                print(f"Du hast {nutzer_wahl} gewählt, der Computer hat {computer_wahl} gewählt.")
                if nutzer_wahl == computer_wahl:
                    print("Unentschieden!")
                elif (nutzer_wahl == "rock" and computer_wahl == "scissors") or \
                    (nutzer_wahl == "paper" and computer_wahl == "rock") or \
                    (nutzer_wahl == "scissors" and computer_wahl == "paper"):
                    print("Du hast gewonnen!")
                else:
                    print("Der Computer hat gewonnen!")
            else:
                print("Danke fürs Spielen!")
                break
    # Würfelgenerator
    elif programm in ("würfeln", "würfelspiel", "würfelgenerator", "würfel", "dice"):
        while True:
            nutzer_antwort = input("Möchtest du würfeln? (ja/nein): ").lower().strip()
            if nutzer_antwort in ("ja", "jo","j"):
                wurf1 = random.randint(1, 6)
                wurf2 = random.randint(1, 6)
                print(f"Du hast geworfen: {wurf1} und {wurf2}")
            elif nutzer_antwort in ("nein", "ne", "n"):
                print("Okay, vielleicht ein anderes Mal!")
                break
            else:
                print("Bitte gib ja oder nein ein!")
    # Temperaturrechner
    elif programm in ("temperaturrechner", "temperaturumrechner", "celsius", "fahrenheit", "temp", "temperature", "tempconverter", "temperatureconverter", "grad", "temperatur"):
        while True:
            temp = input("Wie viel Grad ist es: ")
            try:
                temp = float(temp)
                einheit = input("Celsius oder Fahrenheit (c oder f): ").lower()
                if einheit in ("c", "celsius"):
                    ergebnis = (temp * 9/5) + 32
                    ergebnis = round(ergebnis, 2)
                    print(f"{temp}°C sind umgerechnet {ergebnis}°F")
                    break
                elif einheit in ("f", "fahrenheit"):
                    ergebnis = (temp - 32) * 5/9
                    ergebnis = round(ergebnis, 2)
                    print(f"{temp}°F sind umgerechnet {ergebnis}°C")
                    break
                else:
                    print("Bitte gib nur den Buchstaben c für Celsius oder f für Fahrenheit ein")
            except ValueError:
                print("Bitte gib eine gültige Zahl für die Temperatur ein.")
    # Gewichtsrechner
    elif programm in ("gewichtsrechner", "gewichtsumrechner", "gewicht", "weight", "lbs", "kg", "kilogramm", "pound", "pounds", "weightconverter"):
        while True:
            gewicht = input("Gib dein Gewicht an: ")
            try:
                gewicht = float(gewicht)
                einheit = input("Kilogramm oder Pfund (k oder p): ").lower()
                if einheit == "k":
                    ergebnis = gewicht * 2.20462
                    ergebnis = round(ergebnis, 3)
                    print(f"{gewicht} kg sind umgerechnet {ergebnis} lbs")
                elif einheit == "p":
                    ergebnis = gewicht * 0.453592
                    ergebnis = round(ergebnis, 3)
                    print(f"{gewicht} lbs sind umgerechnet {ergebnis} kg")
                else:
                    print("Bitte gib nur den Buchstaben k für Kilogramm oder p für Pfund ein")
            except ValueError:
                print("Bitte gib eine gültige Zahl für das Gewicht ein.")
    # Taschenrechner
    elif programm in ("taschenrechner", "rechner", "calculator"):
        while True:
            nummer1= input("Gib die erste Zahl ein: ")
            try:
                nummer1=float(nummer1)
                operator=input("Gib einer dieser Operatoren ein ( + - * /): ")
                if operator in ("+", "-", "*", "/"):
                    nummer2=input("Gib die zweite Zahl ein: ")
                    try:
                        nummer2=float(nummer2)
                        if operator == "+":
                            ergebnis= nummer1 + nummer2
                            ergebnis = round(ergebnis, 3)
                            print(ergebnis)
                            break
                        elif operator == "-":
                            ergebnis = nummer1 - nummer2
                            ergebnis = round(ergebnis, 3)
                            print(ergebnis)
                            break
                        elif operator == "*":
                            ergebnis = nummer1 * nummer2
                            ergebnis = round(ergebnis, 3)
                            print(ergebnis)
                            break
                        elif operator == "/":
                            if nummer2 == 0:
                                print("Division durch Null ist nicht erlaubt.")
                                break
                            else:
                                ergebnis = nummer1 / nummer2
                                ergebnis = round(ergebnis, 3)
                                print(ergebnis)
                                break
                    except ValueError:
                        print(f"{nummer2} ist keine gültige Zahl.")
                else:
                    print("Bitte gib nur einen dieser Operatoren ein.")
            except ValueError:
                print(f"{nummer1} ist keine gültige Zahl.")
    else:
        print("Ungültige Eingabe. Bitte versuche es erneut.")