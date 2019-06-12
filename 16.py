# 16.
# Legal Driving Age

import inquirer

legal_age = {"GB": 17,
             "FR": 18,
             "CA": 16}


def input_age():
    print("What is your age?")
    try:
        age = int(input())
        if age < 0:
            print("Enter a valid age.")
            return input_age()
        else:
            return age
    except ValueError:
        print("Error. Input must be a whole number.")
        return input_age()


question = [inquirer.List("country_choice",
    message = "Please choose country",
    choices = ["GB", "FR", "CA"],
    default = "GB")]

answer = inquirer.prompt(question)
country = answer["country_choice"]

age = input_age()
print("You're old enough to legally drive.") if age >= legal_age[country] else print("You aren't old enough to legally drive.")
