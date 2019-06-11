# 14.
# Tax Calculator

def input_amount():
    try:
        amount = float(input())
        return amount
    except ValueError:
        print("Error. Input must be a number.")
        return input_amount()

print("What is the order amount?")
amount = input_amount()

print("What is the state?")
state = str(input()).upper()

if state in ["WI", "WISCONSIN"]:
    tax = round(amount * 0.055, 2)
    print(f"""The subtotal is ${round(amount, 2)}.
The tax is {tax}.
The total is ${amount + tax}.""")
else:
    print(f"The total is {amount}")
