import random

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