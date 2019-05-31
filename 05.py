numbers = []

def input_num():
    try:
        numbers.append(float(input()))
    except ValueError:
        print("Error. Input must be a number.")
        input_num()

print("Enter the first number: ")
input_num()
print("Enter the second number: ")
input_num()
print(f"""{numbers[0]} + {numbers[1]} = {numbers[0] + numbers[1]}
{numbers[0]} - {numbers[1]} = {numbers[0] - numbers[1]}
{numbers[0]} * {numbers[1]} = {numbers[0] * numbers[1]}
{numbers[0]} / {numbers[1]} = {numbers[0] / numbers[1]}""")