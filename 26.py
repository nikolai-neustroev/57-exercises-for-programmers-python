# 26.
# Months to Pay Off a Credit Card

from inputplus import input_float
import math


def calc_months(balance, apr, mpayment):
    rate_p = 1 + apr / 365.0
    bp = math.ceil(100.0 * balance / mpayment) / 100.0
    y = 1.0 + bp * (1.0 - rate_p**30)
    dividend = math.log(y, 2)
    divisor = math.log(rate_p, 2)
    n_months = -1.0 / 30.0 * dividend / divisor
    return n_months


print("What is your balance?")
user_balance = input_float()

print("What is the APR on the card (as percent)?")
user_apr = input_float() / 100.0

print("What is the monthly payment you can make?")
user_mpayment = input_float()

user_nmonths = math.ceil(calc_months(user_balance, user_apr, user_mpayment))

print(f"It will take you {user_nmonths} months to pay off this card.")
