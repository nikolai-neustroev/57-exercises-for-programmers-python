# 10.
# Self-Checkout
import numpy as np

tax_rate = 0.055
user_price = np.array([])
user_quantity = np.array([])


def input_value(value):
    try:
        value = np.append(value, float(input()))
        return value
    except ValueError:
        print("Error. Input must be a number.")
        return input_value(value)


def ask_customer(price, quantity):
    print("Would you like to continue shopping? [y/n]")
    continue_shopping = input()
    if continue_shopping == "y":
        print("Enter the price of an item:")
        price = input_value(price)
        print("Enter the quantity of an item:")
        quantity = input_value(quantity)
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
user_price = input_value(user_price)
print("Enter the quantity of an item:")
user_quantity = input_value(user_quantity)
ask_customer(user_price, user_quantity)
