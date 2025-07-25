import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random

class MinigamesGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Minigames & Rechner")
        self.root.geometry("500x600")
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(expand=True, fill="both")
        self.create_main_menu()

    def clear_window(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def create_main_menu(self):
        self.clear_window()
        title = tk.Label(self.main_frame, text="🎮 Minigames & Rechner", font=("Arial", 20, "bold"))
        title.pack(pady=20)
        buttons = [
            ("💱 Währungsrechner", self.waehrungsrechner),
            ("🎯 Zahlenratespiel", self.zahlenratespiel),
            ("✂️ Schere, Stein, Papier", self.rock_paper_scissors),
            ("🎲 Würfeln", self.wuerfeln),
            ("🌡️ Temperaturrechner", self.temperaturrechner),
            ("⚖️ Gewichtsrechner", self.gewichtsrechner),
            ("🧮 Taschenrechner", self.taschenrechner)
        ]
        for text, cmd in buttons:
            b = tk.Button(self.main_frame, text=text, font=("Arial", 14), width=30, command=cmd)
            b.pack(pady=7)

    def waehrungsrechner(self):
        self.clear_window()
        tk.Label(self.main_frame, text="💱 Währungsrechner", font=("Arial", 18, "bold")).pack(pady=15)
        betrag_var = tk.StringVar()
        waehrung_var = tk.StringVar(value="EUR")
        tk.Label(self.main_frame, text="Betrag:").pack()
        tk.Entry(self.main_frame, textvariable=betrag_var).pack(pady=3)
        tk.Label(self.main_frame, text="Währung (EUR/USD):").pack()
        ttk.Combobox(self.main_frame, textvariable=waehrung_var, values=["EUR", "USD"], state="readonly").pack(pady=3)
        result = tk.Label(self.main_frame, text="")
        result.pack(pady=10)
        def convert():
            try:
                betrag = float(betrag_var.get())
                w = waehrung_var.get().upper()
                if w == "EUR":
                    umgerechnet = round(betrag * 1.167, 2)
                    result.config(text=f"{betrag}€ = {umgerechnet}$")
                elif w == "USD":
                    umgerechnet = round(betrag / 1.167, 2)
                    result.config(text=f"{betrag}$ = {umgerechnet}€")
                else:
                    result.config(text="Ungültige Währung!")
            except ValueError:
                result.config(text="Bitte Zahl eingeben!")
        tk.Button(self.main_frame, text="Umrechnen", command=convert).pack(pady=5)
        tk.Button(self.main_frame, text="Zurück", command=self.create_main_menu).pack(pady=5)

    def zahlenratespiel(self):
        self.clear_window()
        tk.Label(self.main_frame, text="🎯 Zahlenratespiel", font=("Arial", 18, "bold")).pack(pady=15)
        zahl = random.randint(1, 100)
        versuche = tk.IntVar(value=0)
        info = tk.Label(self.main_frame, text="Ich denke an eine Zahl zwischen 1 und 100.")
        info.pack(pady=5)
        eingabe = tk.Entry(self.main_frame)
        eingabe.pack(pady=5)
        result = tk.Label(self.main_frame, text="")
        result.pack(pady=5)
        def raten():
            try:
                guess = int(eingabe.get())
                versuche.set(versuche.get() + 1)
                if guess < zahl:
                    result.config(text="Zu niedrig!")
                elif guess > zahl:
                    result.config(text="Zu hoch!")
                else:
                    result.config(text=f"Richtig! ({versuche.get()} Versuche)")
            except ValueError:
                result.config(text="Bitte Zahl eingeben!")
        tk.Button(self.main_frame, text="Raten", command=raten).pack(pady=5)
        tk.Button(self.main_frame, text="Neues Spiel", command=self.zahlenratespiel).pack(pady=2)
        tk.Button(self.main_frame, text="Zurück", command=self.create_main_menu).pack(pady=5)

    def rock_paper_scissors(self):
        self.clear_window()
        tk.Label(self.main_frame, text="✂️ Schere, Stein, Papier", font=("Arial", 18, "bold")).pack(pady=15)
        result = tk.Label(self.main_frame, text="")
        result.pack(pady=10)
        def play(choice):
            comp = random.choice(["Stein", "Papier", "Schere"])
            if choice == comp:
                res = "Unentschieden!"
            elif (choice == "Stein" and comp == "Schere") or (choice == "Papier" and comp == "Stein") or (choice == "Schere" and comp == "Papier"):
                res = "Du gewinnst!"
            else:
                res = "Computer gewinnt!"
            result.config(text=f"Du: {choice}\nComputer: {comp}\n{res}")
        frame = tk.Frame(self.main_frame)
        frame.pack(pady=5)
        for wahl in ["Stein", "Papier", "Schere"]:
            tk.Button(frame, text=wahl, width=10, command=lambda w=wahl: play(w)).pack(side=tk.LEFT, padx=5)
        tk.Button(self.main_frame, text="Zurück", command=self.create_main_menu).pack(pady=10)

    def wuerfeln(self):
        self.clear_window()
        tk.Label(self.main_frame, text="🎲 Würfeln", font=("Arial", 18, "bold")).pack(pady=15)
        result = tk.Label(self.main_frame, text="")
        result.pack(pady=10)
        def roll():
            wurf1 = random.randint(1, 6)
            wurf2 = random.randint(1, 6)
            result.config(text=f"Du hast geworfen: {wurf1} und {wurf2}")
        tk.Button(self.main_frame, text="Würfeln", command=roll).pack(pady=5)
        tk.Button(self.main_frame, text="Zurück", command=self.create_main_menu).pack(pady=10)

    def temperaturrechner(self):
        self.clear_window()
        tk.Label(self.main_frame, text="🌡️ Temperaturrechner", font=("Arial", 18, "bold")).pack(pady=15)
        temp_var = tk.StringVar()
        einheit_var = tk.StringVar(value="C")
        tk.Label(self.main_frame, text="Temperatur:").pack()
        tk.Entry(self.main_frame, textvariable=temp_var).pack(pady=3)
        tk.Label(self.main_frame, text="Einheit (C/F):").pack()
        ttk.Combobox(self.main_frame, textvariable=einheit_var, values=["C", "F"], state="readonly").pack(pady=3)
        result = tk.Label(self.main_frame, text="")
        result.pack(pady=10)
        def convert():
            try:
                t = float(temp_var.get())
                e = einheit_var.get().upper()
                if e == "C":
                    f = round((t * 9/5) + 32, 2)
                    result.config(text=f"{t}°C = {f}°F")
                elif e == "F":
                    c = round((t - 32) * 5/9, 2)
                    result.config(text=f"{t}°F = {c}°C")
                else:
                    result.config(text="Ungültige Einheit!")
            except ValueError:
                result.config(text="Bitte Zahl eingeben!")
        tk.Button(self.main_frame, text="Umrechnen", command=convert).pack(pady=5)
        tk.Button(self.main_frame, text="Zurück", command=self.create_main_menu).pack(pady=5)

    def gewichtsrechner(self):
        self.clear_window()
        tk.Label(self.main_frame, text="⚖️ Gewichtsrechner", font=("Arial", 18, "bold")).pack(pady=15)
        gewicht_var = tk.StringVar()
        einheit_var = tk.StringVar(value="kg")
        tk.Label(self.main_frame, text="Gewicht:").pack()
        tk.Entry(self.main_frame, textvariable=gewicht_var).pack(pady=3)
        tk.Label(self.main_frame, text="Einheit (kg/lbs):").pack()
        ttk.Combobox(self.main_frame, textvariable=einheit_var, values=["kg", "lbs"], state="readonly").pack(pady=3)
        result = tk.Label(self.main_frame, text="")
        result.pack(pady=10)
        def convert():
            try:
                g = float(gewicht_var.get())
                e = einheit_var.get().lower()
                if e == "kg":
                    lbs = round(g * 2.20462, 3)
                    result.config(text=f"{g} kg = {lbs} lbs")
                elif e == "lbs":
                    kg = round(g * 0.453592, 3)
                    result.config(text=f"{g} lbs = {kg} kg")
                else:
                    result.config(text="Ungültige Einheit!")
            except ValueError:
                result.config(text="Bitte Zahl eingeben!")
        tk.Button(self.main_frame, text="Umrechnen", command=convert).pack(pady=5)
        tk.Button(self.main_frame, text="Zurück", command=self.create_main_menu).pack(pady=5)

    def taschenrechner(self):
        self.clear_window()
        tk.Label(self.main_frame, text="🧮 Taschenrechner", font=("Arial", 18, "bold")).pack(pady=15)
        num1_var = tk.StringVar()
        num2_var = tk.StringVar()
        op_var = tk.StringVar(value="+")
        tk.Label(self.main_frame, text="Erste Zahl:").pack()
        tk.Entry(self.main_frame, textvariable=num1_var).pack(pady=3)
        tk.Label(self.main_frame, text="Operator:").pack()
        ttk.Combobox(self.main_frame, textvariable=op_var, values=["+", "-", "*", "/"], state="readonly").pack(pady=3)
        tk.Label(self.main_frame, text="Zweite Zahl:").pack()
        tk.Entry(self.main_frame, textvariable=num2_var).pack(pady=3)
        result = tk.Label(self.main_frame, text="")
        result.pack(pady=10)
        def calc():
            try:
                n1 = float(num1_var.get())
                n2 = float(num2_var.get())
                op = op_var.get()
                if op == "+":
                    erg = n1 + n2
                elif op == "-":
                    erg = n1 - n2
                elif op == "*":
                    erg = n1 * n2
                elif op == "/":
                    if n2 == 0:
                        result.config(text="Division durch Null!")
                        return
                    erg = n1 / n2
                result.config(text=f"Ergebnis: {round(erg, 3)}")
            except ValueError:
                result.config(text="Bitte gültige Zahlen eingeben!")
        tk.Button(self.main_frame, text="Berechnen", command=calc).pack(pady=5)
        tk.Button(self.main_frame, text="Zurück", command=self.create_main_menu).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = MinigamesGUI(root)
    root.mainloop() 