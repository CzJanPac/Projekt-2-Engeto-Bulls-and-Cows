"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Jan Páč
email: czjanpac@gmail.com
"""

import random
import time

oddelovac = "-" * 47
statistiky = []

print("Hi there!")
while True:
    print(f"""{oddelovac}
I've generated a random 4 digit number for you.
Let's play a Bulls and Cows game.""")

    prvni_cislo = random.choice(range(1,10))
    ostatni = list(set(range(10)) - {prvni_cislo})
    ostatni_cisla = random.sample(ostatni, 3)
    tajne_cislo = str(prvni_cislo) + "".join(str(cislo) for cislo in ostatni_cisla)
    pocet_pokusu = 0

    cas_zacatek = time.perf_counter()

    while True:
        print(oddelovac)
        hracovo_cislo = str(input("Enter a number: "))
        if (
            len(hracovo_cislo) != 4
            or hracovo_cislo[0] == "0" 
            or hracovo_cislo.isdigit() == False 
            or len(set(hracovo_cislo)) != 4
            ):
            print("""Your number must contain:
    - 4 unique digits (0-9)
    - the first digit must not be 0""")
            continue
        pocet_pokusu += 1
        bulls = 0
        cows = 0
        for index in range(4):
            if hracovo_cislo[index] == tajne_cislo[index]:
                bulls += 1
            elif hracovo_cislo[index] in tajne_cislo:
                cows += 1
        if bulls == 1:
            bull = "bull"
        elif bulls != 1:
            bull = "bulls"
        if cows == 1:
            cow = "cow"
        elif cows != 1:
            cow = "cows"
        print(f"{bulls} {bull}, {cows} {cow}")

        if bulls == 4:
            cas_konec = time.perf_counter()
            cas_celkem = cas_konec - cas_zacatek
            minuty = int(cas_celkem // 60)
            sekundy = int(cas_celkem % 60)
            statistiky.append({"pokusy": pocet_pokusu,
                            "cas": cas_celkem
                            })
            print(f"""Correct, you've guessed the right number in {pocet_pokusu} guesses!
Game time: {minuty} min {sekundy} sec
That's amazing!
{oddelovac}""")
            
            while True:
                hrat_znovu = input("Do you want to play again? (yes or no): ").strip().lower()
                if hrat_znovu in ("yes", "no"):
                    break
                print("Answer yes or no, please: ")
            
            if hrat_znovu == "no":
                print(f"""{oddelovac}
Here is statistics of your games: """)
                
                celkem_her = len(statistiky)
                celkem_pokusu = sum(hra['pokusy'] for hra in statistiky)
                celkovy_cas = sum(hra['cas'] for hra in statistiky)
                
                for i, hra in enumerate(statistiky, 1):
                    minuty = int(hra['cas'] // 60)
                    sekundy = int(hra['cas'] % 60)
                    print(f"Game {i}: {hra['pokusy']} guesses, game time: {minuty} min {sekundy} sec")
                
                total_minutes = int(celkovy_cas // 60)
                total_seconds = int(celkovy_cas % 60)

                print(f"{oddelovac}")
                print(f"Total games: {celkem_her}")
                print(f"Total guesses: {celkem_pokusu}")
                print(f"Total playing time: {total_minutes} min {total_seconds} sec")
                
                exit()
            
            else:
                break



