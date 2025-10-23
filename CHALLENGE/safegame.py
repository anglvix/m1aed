import random

password = [random.randint(0, 9) for _ in range(4)]

def open_safe():
    max_attempts = 10
    attempts = 0

    print("Welcome to the digital safe!")
    print("Try to guess the 4-digit password. Each number is between 0 and 9.")
    
    while attempts < max_attempts:
        user_input = input(f"\nAttempt {attempts + 1}: Enter 4 numbers separated by spaces: ")
        guess = user_input.split()

        if len(guess) != 4 or not all(num.isdigit() and 0 <= int(num) <= 9 for num in guess):
            print("Invalid! Please enter 4 numbers between 0 and 9 with spaces in between them.")
            continue

        guess = [int(num) for num in guess]
        attempts += 1

        correct = [guess[i] if guess[i] == password[i] else None for i in range(4)]

        if correct == password:
            print(f"Congrats! You cracked the safe. The password was {password}.")
            return
        else:
            if all(num is None for num in correct):
                print("No numbers are correct in their positions.")
            else:
                hint = [str(num) if num is not None else "*" for num in correct]
                print("Numbers correct and in the right position:", " ".join(hint))

    print(f"Game over. You've used all 10 attempts. The password was {password}.")

open_safe()
