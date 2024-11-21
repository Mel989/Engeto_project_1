"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Melanie Demkova
email: mel@email.cz
discord: Mel_d989
"""

import random
import time

def generate_secret_number():
    # Vytvoření čtyřmístného tajného čísla s unikátními číslicemi a nezačínajícího nulou
    digits = list("123456789")
    secret_number = random.choice(digits)
    digits = list("0123456789")
    while len(secret_number) < 4:
        digit = random.choice(digits)
        if digit not in secret_number:
            secret_number += digit
    return secret_number

def validate_guess(guess):
    # Ověření, že vstup má správný formát
    if len(guess) != 4:
        return "Vstup musí obsahovat přesně 4 číslice."
    if not guess.isdigit():
        return "Vstup musí obsahovat pouze čísla."
    if guess[0] == "0":
        return "Číslo nesmí začínat nulou."
    if len(set(guess)) != 4:
        return "Číslo musí mít unikátní číslice."
    return None

def evaluate_guess(secret, guess):
    # Vyhodnocení zadaného vstupu
    bulls = cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def print_feedback(guess, bulls, cows):
    # Správné množné číslo pro bulls a cows
    bulls_text = f"{bulls} bull" if bulls == 1 else f"{bulls} bulls"
    cows_text = f"{cows} cow" if cows == 1 else f"{cows} cows"
    print(f"{guess} -> {bulls_text}, {cows_text}")

def main():
    print("Vítej ve hře Bulls and Cows!")
    print("Vygeneroval jsem tajné čtyřmístné číslo.")
    print("Pokud uhodneš číslo i jeho umístění, získáváš 'bull'.")
    print("Pokud uhodneš pouze číslo, ale ne jeho umístění, získáváš 'cow'.")
    print("Hodně štěstí!\n")
    
    secret_number = generate_secret_number()
    attempts = 0
    start_time = time.time()

    while True:
        guess = input("Zadej svůj tip (čtyřmístné číslo): ")
        error_message = validate_guess(guess)
        if error_message:
            print("Chyba:", error_message)
            continue
        
        attempts += 1
        bulls, cows = evaluate_guess(secret_number, guess)
        print_feedback(guess, bulls, cows)
        
        if bulls == 4:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Gratuluji! Uhodl jsi tajné číslo {secret_number} na {attempts} pokusů za {elapsed_time:.2f} sekund.")
            break

if __name__ == "__main__":
    main()