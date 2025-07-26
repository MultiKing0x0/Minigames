import tkinter as tk
import random

class MyOwnTkinter:
    def dice():
        while True:
            nutzer_antwort = input("Möchtest du würfeln? (ja/nein): ").lower()
            if nutzer_antwort == "ja":
                wurf1 = random.randint(1, 6)
                wurf2 = random.randint(1, 6)
                print("Du hast geworfen:", (wurf1, wurf2))
            elif nutzer_antwort == "nein" or "ne":
                print("Okay, vielleicht ein anderes Mal!")
                break
            else:
                print("Bitte gib ja oder nein ein!")
    
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

    def number_guessing_game():
        while True:
            try:
                guess = int(input("Gib eine Zahl zwischen 1 und 100 ein: "))
                if guess < 1 or guess > 100:
                    print("Ungültige Eingabe. Bitte versuche es erneut.")
                else:
                    number = random.randint(1, 100)
                    if guess == number:
                        print("Herzlichen Glückwunsch! Du hast die Zahl erraten:", number)
                    elif guess < number:
                        print("Die gesuchte Zahl ist größer als", guess)
                    else:
                        print("Die gesuchte Zahl ist kleiner als", guess)
            except ValueError:
                print("Das war keine gültige Zahl. Versuche es erneut.")

    def rock_paper_scissors():
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

    def temperature_converter():
        temp=input("Wie viel Grad ist es: ")
        try:
            temp = float(temp)
            einheit = input("Celsius oder Fahrenheit (c oder f): ")
            einheit = einheit.lower()
            if einheit == "c":
                ergebnis = (temp * 9/5) + 32
                ergebnis = round(ergebnis, 2)
                print(f"{temp}°C sind umgerechnet {ergebnis}°F")
            elif einheit == "f":
                ergebnis = (temp - 32) * 5/9
                ergebnis = round(ergebnis, 2)
                print(f"{temp}°F sind umgerechnet {ergebnis}°C")
            else:
                print("Bitte gib nur den Buchstaben c für Celsius oder f für Fahrenheit ein")
        except ValueError:
            print("Bitte gib eine gültige Zahl für die Temperatur ein.")

    