# 12.
# Computing Simple Interest

def input_amount():
    try:
        amount = float(input())
        return(amount)
    except ValueError:
        print("Error. Input must be a number.")
        return input_amount()
        
def calc_simple_interest(principal, interest, years):
    end_amount = principal * (1.0 + interest * years)
    return end_amount

print("Enter the principal:")
principal = input_amount()

print("Enter the rate of interest:")
interest = input_amount() / 100.0

print("Enter the number of years:")
years = input_amount()

for i in range(int(years)+1):
    end_amount = round(calc_simple_interest(principal, interest, i), 2)
    print(f"After {i} years at {interest * 100.0}%, the interest will be worth ${end_amount}.")
