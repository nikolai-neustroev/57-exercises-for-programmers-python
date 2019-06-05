# 11.
# Currency Conversion
import math, inquirer

xr = {"EUR": 113.0, "USD": 89.0}

def input_amount():
    print("How much money would you like to exchange?")
    try:
        amount = float(input())
        return(amount)
    except ValueError:
        print("Error. Input must be a number.")
        return input_amount()

question = [inquirer.List("currency_choice",
    message = "Please choose currency",
    choices = ["EUR", "USD"],
    default = "EUR")]

answer = inquirer.prompt(question)
currency = answer["currency_choice"]
pair = "USD" if currency == "EUR" else "EUR"

amount = input_amount()
exchanged_amount = math.ceil(amount * xr[currency]) / 100

print(f"{amount} {currency} at an exchange rate of {xr[currency]} is {exchanged_amount} {pair}.")
