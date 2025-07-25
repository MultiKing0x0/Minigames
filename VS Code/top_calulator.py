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
                elif operator == "-":
                    ergebnis = nummer1 - nummer2
                    ergebnis = round(ergebnis, 3)
                    print(ergebnis)
                elif operator == "*":
                    ergebnis = nummer1 * nummer2
                    ergebnis = round(ergebnis, 3)
                    print(ergebnis)
                elif operator == "/":
                    if nummer2 == 0:
                        print("Division durch Null ist nicht erlaubt.")
                    else:
                        ergebnis = nummer1 / nummer2
                        ergebnis = round(ergebnis, 3)
                        print(ergebnis)
            except ValueError:
                print(f"{nummer2} ist keine gültige Zahl.")
        else:
            print("Bitte gib nur einen dieser Operatoren ein.")
    except ValueError:
        print(f"{nummer1} ist keine gültige Zahl.")