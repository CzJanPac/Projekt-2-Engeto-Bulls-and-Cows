"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Jan Páč
email: czjanpac@gmail.com
"""

import random
import time

oddelovac = "-" * 47
statistiky = []

def vygeneruj_nahodne_cislo():
    prvni_cislo = random.choice(range(1,10))
    ostatni = list(set(range(10)) - {prvni_cislo})
    ostatni_cisla = random.sample(ostatni, 3)
    tajne_cislo = str(prvni_cislo) + "".join(str(c) for c in ostatni_cisla)
    return tajne_cislo

def ziskej_vstup():
    while True:
        print(oddelovac)
        hracovo_cislo = input("Enter a 4-digit number: ")
        
        chyba = False

        if not hracovo_cislo.isdigit():
            print("Your number must contain only digits (0-9).")
            chyba = True

        if len(hracovo_cislo) != 4:
            print("Your number must be exactly 4 digits long.")
            chyba = True

        elif len(set(hracovo_cislo)) != 4:
            print("All digits must be unique - no duplicates allowed.")
            chyba = True

        if hracovo_cislo and hracovo_cislo[0] == "0":
            print("The first digit must not be 0.")
            chyba = True

        if not chyba:
            return hracovo_cislo

def vyhodnot_hadani(hracovo_cislo, tajne_cislo):
    bulls = 0
    cows = 0
    for i in range(4):
        if hracovo_cislo[i] == tajne_cislo[i]:
            bulls += 1
        elif hracovo_cislo[i] in tajne_cislo:
            cows += 1
    return bulls, cows

def vypis_statistiky():
    print(f"""{oddelovac}
Here are the statistics of your games:""")
    
    celkem_her = len(statistiky)
    celkem_pokusu = sum(hra['pokusy'] for hra in statistiky)
    celkovy_cas = sum(hra['cas'] for hra in statistiky)

    for index, hra in enumerate(statistiky, 1):
        minuty = int(hra['cas'] // 60)
        sekundy = int(hra['cas'] % 60)
        print(f"Game {index}: {hra['pokusy']} guesses, game time: {minuty} min {sekundy} sec")

    total_minutes = int(celkovy_cas // 60)
    total_seconds = int(celkovy_cas % 60)
    print(f"{oddelovac}")
    print(f"Total games: {celkem_her}")
    print(f"Total guesses: {celkem_pokusu}")
    print(f"Total playing time: {total_minutes} min {total_seconds} sec")

def hra():
    print(f"""{oddelovac}
I've generated a random 4 digit number for you.
Let's play a Bulls and Cows game.""")
    
    tajne_cislo = vygeneruj_nahodne_cislo()
    pocet_pokusu = 0
    cas_zacatek = time.perf_counter()

    while True:
        hracovo_cislo = ziskej_vstup()
        pocet_pokusu += 1
        bulls, cows = vyhodnot_hadani(hracovo_cislo, tajne_cislo)

        bull = "bull" if bulls == 1 else "bulls"
        cow = "cow" if cows == 1 else "cows"
        print(f"{bulls} {bull}, {cows} {cow}")

        if bulls == 4:
            cas_konec = time.perf_counter()
            cas_celkem = cas_konec - cas_zacatek
            minuty = int(cas_celkem // 60)
            sekundy = int(cas_celkem % 60)
            print(f"""Correct, you've guessed the right number in {pocet_pokusu} guesses!
Game time: {minuty} min {sekundy} sec
That's amazing!
{oddelovac}""")
            statistiky.append({"pokusy": pocet_pokusu, "cas": cas_celkem})
            break

def main():
    print("Hi there!")
    while True:
        hra()
        while True:
            hrat_znovu = input("Do you want to play again? ('yes' or 'no'): ").strip().lower()
            if hrat_znovu in ("yes", "no"):
                break
            print("Please enter 'yes' or 'no':")
        if hrat_znovu == "no":
            vypis_statistiky()
            break

if __name__ == "__main__":
    main()
