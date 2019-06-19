# 5.
# Simple Math

from inputplus import append_vec_float

numbers = []

print("Enter the first number: ")
append_vec_float(numbers)
print("Enter the second number: ")
append_vec_float(numbers)
print(f"""{numbers[0]} + {numbers[1]} = {numbers[0] + numbers[1]}
{numbers[0]} - {numbers[1]} = {numbers[0] - numbers[1]}
{numbers[0]} * {numbers[1]} = {numbers[0] * numbers[1]}
{numbers[0]} / {numbers[1]} = {numbers[0] / numbers[1]}""")
