gewicht = input("Gib dein Gewicht an: ")
try:
    gewicht = float(gewicht)
    einheit = input("Kilogramm oder Pfund (k oder p): ")
    einheit = einheit.lower()
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

def sag_hallo():
    print("Hallo!")

sag_hallo()