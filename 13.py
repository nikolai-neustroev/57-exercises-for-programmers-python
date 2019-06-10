# 13.
# Determining Compound Interest

import math

def input_amount():
    try:
        amount = float(input())
        return amount
    except ValueError:
        print("Error. Input must be a number.")
        return input_amount()

def calc_comp_interest(principal, interest, years, n_compound):
    end_amount = principal * (1.0 + interest / n_compound)**(n_compound*years)
    return end_amount

print("Enter the principal:")
principal = input_amount()

print("Enter the rate of interest:")
interest = input_amount() / 100.0

print("Enter the number of years:")
years = input_amount()

print("Enter the number of times the interest is compounded per year:")
n_compound = input_amount()

end_amount = math.ceil((calc_comp_interest(principal, interest, years, n_compound) * 100)) / 100
print(f"${principal} invested at {interest*100}% for {int(years)} years compounded {int(n_compound)} times per year is ${end_amount}.")
