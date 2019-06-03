# 11.
# Currency Conversion
import math

print("How many euros are you exchanging?")
euro = float(input())
print("What is the exchange rate?")
xr = float(input())
usd = math.ceil(euro * xr / 100)
print(f"{euro} euros at an exchange rate of {xr} is {usd} U.S. dollars.")
