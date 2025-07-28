"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Petr Svetr
email: petr.svetr@gmail.com
"""
import random

oddelovac = "-" * 47

print("Hi there!")
print(oddelovac)
print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")

prvni_cislo = random.choice(range(1,10))
ostatni = list(set(range(10)) - {prvni_cislo})
ostatni_cisla = random.sample(ostatni, 3)
tajne_cislo = str(prvni_cislo) + "".join(str(cislo) for cislo in ostatni_cisla)
pocet_pokusu = 0

while True:
    hracovo_cislo = str(input("Enter a number: "))
    if (
        len(hracovo_cislo) != 4
        or hracovo_cislo[0] == "0" 
        or hracovo_cislo.isdigit() == False 
        or len(set(hracovo_cislo)) != 4
        ):
        print("""Your number must contain:
- 4 unique numbers (0 - 9)
- first number must not be 0""")
    else:
        while tajne_cislo != hracovo_cislo:
