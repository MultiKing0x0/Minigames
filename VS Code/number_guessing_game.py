import random

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