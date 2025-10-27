import random

password = [random.randint(0,9) for _ in range(4)]

def safegame():
    maxattempts=10
    attempts=0

    print("welcome to the safe game!")
    print("guess the 4 digit password, you have 10 tries. Each number is between 0 and 9.")
    print(password)

    while attempts<maxattempts:
        inp=input(f"\n attempt: {attempts+1} enter 4 numbers seperated by spaces:")
        guess=inp.split()

        if len(guess)!=4 or not all (num.isdigit() and 0 <= int(num)<=9 for num in guess):
            print("invalid! enter 4 numbers between 0 and 9 with spaces in between them.")
            continue

        guess=[int(num) for num in guess]
        attempts+=1

        correct=[guess[i]if guess[i] == password [i] else None for i in range(4)]

        if correct==password:
            print(f"nice, you cracked the safe. The password was {password}.")
            return
        else:
            if all(num is None for num in correct):
                print("no numbers in their right positions")
            else:
                hint = [str(num) if num is not None else "*" for num in correct]
                print("numbers correct in the right position:"," ".join(hint))

    print(f"game over, the password was {password}")

safegame()