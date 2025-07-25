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