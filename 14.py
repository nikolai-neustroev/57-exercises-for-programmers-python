# 14.
# Tax Calculator

from inputplus import input_float

print("What is the order amount?")
amount = input_float()

print("What is the state?")
state = str(input()).upper()

if state in ["WI", "WISCONSIN"]:
    tax = round(amount * 0.055, 2)
    print(f"""The subtotal is ${round(amount, 2)}.
The tax is ${tax}.
The total is ${amount + tax}.""")
else:
    print(f"The total is {amount}")
