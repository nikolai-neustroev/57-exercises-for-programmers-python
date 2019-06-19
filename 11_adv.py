# 11.
# Currency Conversion
from inputplus import input_float
import math, inquirer

xr = {"EUR": 113.0, "USD": 89.0}

question = [inquirer.List("currency_choice",
    message = "Please choose currency",
    choices = ["EUR", "USD"],
    default = "EUR")]

answer = inquirer.prompt(question)
currency = answer["currency_choice"]
pair = "USD" if currency == "EUR" else "EUR"

print("How much money would you like to exchange?")
amount = input_float()
exchanged_amount = math.ceil(amount * xr[currency]) / 100

print(f"{amount} {currency} at an exchange rate of {xr[currency]} is {exchanged_amount} {pair}.")
