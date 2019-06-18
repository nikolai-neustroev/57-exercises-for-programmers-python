# 26.
# Months to Pay Off a Credit Card

import math


def input_number():
    try:
        amount = float(input())
        return amount
    except ValueError:
        print("Error. Input must be a number.")
        return input_number()


def calc_months(balance, apr, mpayment):
    rate_p = 1 + apr / 365.0
    bp = math.ceil(100.0 * balance / mpayment) / 100.0
    y = 1.0 + bp * (1.0 - rate_p**30)
    dividend = math.log(y, 2)
    divisor = math.log(rate_p, 2)
    n_months = -1.0 / 30.0 * dividend / divisor
    return n_months


print("What is your balance?")
user_balance = input_number()

print("What is the APR on the card (as percent)?")
user_apr = input_number() / 100.0

print("What is the monthly payment you can make?")
user_mpayment = input_number()

user_nmonths = math.ceil(calc_months(user_balance, user_apr, user_mpayment))

print(f"It will take you {user_nmonths} months to pay off this card.")
