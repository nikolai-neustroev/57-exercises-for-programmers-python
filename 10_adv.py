# 10.
# Self-Checkout
import numpy as np

tax_rate = 0.055
price = np.array([])
quantity = np.array([])

def input_price(price):
    try:
        price = np.append(price, float(input()))
        return price
    except ValueError:
        print("Error. Input must be a number.")
        return input_price(price)

def input_quantity(quantity):
    try:
        quantity = np.append(quantity, float(input()))
        return quantity
    except ValueError:
        print("Error. Input must be a number.")
        return input_quantity(quantity)

def ask_customer(price, quantity):
    print("Would you like to continue shopping? [y/n]")
    continue_shopping = input()
    if continue_shopping == "y":
        print("Enter the price of an item:")
        price = input_price(price)
        print("Enter the quantity of an item:")
        quantity = input_quantity(quantity)
        return ask_customer(price, quantity)
    elif continue_shopping == "n":
        subtotal = np.sum(price * quantity)
        subtotal = round(subtotal)
        tax = round(subtotal * tax_rate, 2)
        total = round(subtotal + tax, 2)
        print(f"Subtotal: ${subtotal}. Tax: ${tax}. Total: ${total}")
    else:
        return ask_customer(price, quantity)

print("Enter the price of an item:")
price = input_price(price)
print("Enter the quantity of an item:")
quantity = input_quantity(quantity)
ask_customer(price, quantity)
