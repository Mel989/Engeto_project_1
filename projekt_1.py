"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Melanie Demkova
email: mel@email.cz
discord: Mel_d989
"""

import sys
user = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

prihl_jmeno = input("Zadej přihlašovací jméno: ")
if prihl_jmeno not in user:
    print("Nejste registrovaný! Ukončuji program!")
    sys.exit()

heslo = input("Zadej heslo: ")
if user.get(prihl_jmeno) == heslo:
    print("-----------------------------------------------------")
    print("Vítej v textovém analyzátoru,", prihl_jmeno, " \nMáme 3 texty k analýze.")
    print("-----------------------------------------------------")
else:
    print("Nesprávné heslo!")
    sys.exit()

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
vyber_text = input("Zadejte číslo textu mezi 1 a 3: ")
print("-----------------------------------------------------")

if not vyber_text.isdigit():
    print("Nezadal jsi číslo, ukončuji program!")
else:
    vyber_text = int(vyber_text)
    if vyber_text < 1 or vyber_text > 3:
        print("Vybraný text není v zadání. Ukončuji program.")
    else:
        pocet_slov = len(TEXTS[vyber_text - 1].split())
        print("Vybraný text má", pocet_slov, "slov.")

        pocet_slov_s_velkym_pismenem = []
        for slova in TEXTS[vyber_text -1].split():
            if slova[0].isupper():
                pocet_slov_s_velkym_pismenem.append(slova)
        pocet_slov_s_velkym_pismenem_soucet = len(pocet_slov_s_velkym_pismenem)
        print("Vybraný text má", pocet_slov_s_velkym_pismenem_soucet, "slov začínajících velkým písmenem.")

        pocet_slov_velkymi_pismeny=[]
        for slova in TEXTS[vyber_text -1].split():
            if slova.isupper() and slova.isalpha():
                pocet_slov_velkymi_pismeny.append(slova)
        pocet_slov_velkymi_pismeny_soucet = len(pocet_slov_velkymi_pismeny)
        print("Vybraný text má", pocet_slov_velkymi_pismeny_soucet, "slov psaných velkými písmeny.", pocet_slov_velkymi_pismeny)

        pocet_slov_malymi_pismeny=[]
        for slova in TEXTS[vyber_text -1].split():
            if slova.islower():
                pocet_slov_malymi_pismeny.append(slova)
        pocet_slov_malymi_pismeny_soucet = len(pocet_slov_malymi_pismeny)
        print("Vybraný text má", pocet_slov_malymi_pismeny_soucet, "slov psaných malými písmeny.")

        pocet_cisel=[]
        for slova in TEXTS[vyber_text -1].split():
            if slova.isdigit():
                pocet_cisel.append(slova)
        pocet_cisel_soucet = len(pocet_cisel)
        print("Vybraný text má", pocet_cisel_soucet, "čísel.")

        soucet_cisel=0
        for slova in TEXTS[vyber_text -1].split():
            if slova.isdigit():
                soucet_cisel +=int(slova)
        print("Vybraný text má součet čísel: ", soucet_cisel)
        
        import string
        delky_slov = {}
        for slovo in TEXTS[vyber_text - 1].split():
            slovo = slovo.strip(string.punctuation)
            delka = len(slovo)
            if delka in delky_slov:
                delky_slov[delka] += 1
            else:
                delky_slov[delka] = 1

        print("-----------------------------------------------------")
        print("\nLEN |    OCCURRENCES   | NR.")
        print("-----------------------------------------------------")

        for delka in sorted(delky_slov.keys()):
            print("{:>3} | {:<16} | {}".format(delka, '*' * delky_slov[delka], delky_slov[delka]))