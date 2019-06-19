# 13.
# Determining Compound Interest

from inputplus import input_float
import math


def calc_comp_interest(principal, interest, years, n_compound):
    return principal * (1.0 + interest / n_compound)**(n_compound*years)


print("Enter the principal:")
user_principal = input_float()

print("Enter the rate of interest:")
user_interest = input_float() / 100.0

print("Enter the number of years:")
user_years = input_float()

print("Enter the number of times the interest is compounded per year:")
user_n_compound = input_float()

end_amount = math.ceil((calc_comp_interest(user_principal, user_interest, user_years, user_n_compound) * 100)) / 100
print(f"""${user_principal} invested at {user_interest*100}% for {int(user_years)} years
compounded {int(user_n_compound)} times per year is ${end_amount}.""")
