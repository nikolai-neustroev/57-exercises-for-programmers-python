# 6.
# Retirement Calculator.

import datetime

age = []

def input_age():
    try:
        age.append(int(input()))
    except ValueError:
        print("Error. Age must be a number.")
        return input_age()

print("What is your current age?")
input_age()
print("At what age would you like to retire?")
input_age()

current_year = datetime.datetime.now().year
year_diff = age[1] - age[0]
retirement_year = current_year + year_diff

if year_diff > 0:
    print(f"""You have {year_diff} years left until you can retire.
It's {current_year}, so you can retire in {retirement_year}.""")
else:
    print("You already can retire.")
