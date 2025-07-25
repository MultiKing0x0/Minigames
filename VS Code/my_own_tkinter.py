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