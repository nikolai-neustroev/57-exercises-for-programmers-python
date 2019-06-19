# 6.
# Retirement Calculator.

import datetime
from inputplus import append_vec_int

age = []

print("What is your current age?")
append_vec_int(age)
print("At what age would you like to retire?")
append_vec_int(age)

current_year = datetime.datetime.now().year
year_diff = age[1] - age[0]
retirement_year = current_year + year_diff

if year_diff > 0:
    print(f"""You have {year_diff} years left until you can retire.
It's {current_year}, so you can retire in {retirement_year}.""")
else:
    print("You already can retire.")
