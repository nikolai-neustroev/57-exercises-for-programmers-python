# 12.
# Computing Simple Interest
from inputplus import input_float


def calc_simple_interest(principal, interest, years):
    return principal * (1.0 + interest * years)


print("Enter the principal:")
user_principal = input_float()

print("Enter the rate of interest:")
user_interest = input_float() / 100.0

print("Enter the number of years:")
user_years = input_float()

for i in range(int(user_years)+1):
    end_amount = round(calc_simple_interest(user_principal, user_interest, i), 2)
    print(f"After {i} years at {user_interest * 100.0}%, the interest will be worth ${end_amount}.")
