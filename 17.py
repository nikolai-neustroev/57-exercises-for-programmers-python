# 17.
# Blood Alcohol Calculator

import inquirer


def input_amount():
    try:
        amount = float(input())
        return amount
    except ValueError:
        print("Error. Input must be a number.")
        return input_amount()


print("Enter your weight (lb.):")
weight = input_amount()

question = [inquirer.List("gender_choice",
                          message="Please choose your gender",
                          choices=["F", "M"],
                          default="F")]

answer = inquirer.prompt(question)
gender = answer["gender_choice"]

print("Enter number of drinks:")
n_drinks = input_amount()

print("Enter amount of alcohol by volume of the drinks consumed (oz):")
alcohol = input_amount()

print("Enter amount of time since your last drink:")
time = input_amount()

if gender is "F":
    r = 0.66
else:
    r = 0.73

bac = (n_drinks * alcohol * 5.14 / weight * r) - 0.015 * time

if bac >= 0.08:
    print(f"""Your BAC is {bac}.
It is not legal for you to drive.""")
else:
    print(f"""Your BAC is {bac}.
It is legal for you to drive.""")
