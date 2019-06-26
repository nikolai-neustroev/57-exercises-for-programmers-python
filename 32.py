# 32.
# Guess the Number Game
from inputplus import input_int
import random


def ask_restart(count):
    print(f"You got it in {count} guesses! Play again?")
    again = str(input()).upper()
    if again == "N":
        print("Goodbye!")
    elif again == "Y":
        try_loop()
    else:
        return ask_restart(count)


def set_lvl():
    print("Pick a difficulty level (1, 2, or 3):")
    lvl = input()
    if lvl == "1":
        guess = random.randint(1, 10)
        return guess
    elif lvl == "2":
        guess = random.randint(1, 100)
        return guess
    elif lvl == "3":
        guess = random.randint(1, 1000)
        return guess
    else:
        return set_lvl()


def try_loop():
    count = 1
    guess = set_lvl()
    print("I have my number. What's your guess?")
    user_try = input_int()
    while user_try != guess:
        if user_try > guess:
            print("Too high. Guess again.")
            user_try = input_int()
        elif user_try < guess:
            print("Too low. Guess again.")
            user_try = input_int()
        count += 1
    else:
        ask_restart(count)


try_loop()
