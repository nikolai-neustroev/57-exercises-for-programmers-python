# 20.
# Multistate Sales Tax Calculator

import math


def input_amount():
    try:
        amount = float(input())
        return amount
    except ValueError:
        print("Error. Input must be a number.")
        return input_amount()


tax_rate = {
    "IL": {"empty": 0.08},
    "ILLINOIS": {"empty": 0.08},
    "WI": {
        "EAU CLAIRE": 0.005,
        "DUNN": 0.004
    },
    "WISCONSIN": {
        "EAU CLAIRE": 0.005,
        "DUNN": 0.004
    }
}

print("What is the order amount?")
oa = input_amount()

print("What state do you live in?")
state = str(input()).upper()

if state in ["WI", "WISCONSIN"]:
    print("What county do you live in?")
    county = str(input()).upper()
elif state in ["IL", "ILLINOIS"]:
    county = "empty"

tax = math.ceil(100.0 * oa * tax_rate[state][county]) / 100.0
print(f"The tax is ${tax}.")

total = oa + tax
print(f"The total is ${total}.")
