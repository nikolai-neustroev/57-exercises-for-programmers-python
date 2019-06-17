# 25.
# Password Strength Indicator

import re

supp_lng = ["ENG", "RUS"]

levels = {
    0: ["is a very weak password", "-- очень слабый пароль"],
    1: ["is a weak password", "-- слабый пароль"],
    2: ["is a strong password", "-- сильный пароль"],
    3: ["is a very strong password", "-- очень сильный пароль"]
}

enter_pw_lng = {
    "ENG": "Please enter password.",
    "RUS": "Пожалуйста, введите пароль."
}


def password_validator(password):
    if len(password) < 8 and password.isdigit():
        level = 0
        return level
    elif len(password) < 8 and password.isalpha():
        level = 1
        return level
    elif len(password) >= 8 and bool(re.match('^(?=.*[0-9])(?=.*[a-zA-Z])((?![!@#%$^&*=+><]).)*$', password)):
        level = 2
        return level
    elif len(password) >= 8 and bool(re.match('^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#%$^&*=+><])', password)):
        level = 3
        return level


def choose_lng():
    print(f"Please choose language / Пожалуйста, выберите язык: {supp_lng}")
    lng = str(input()).upper()
    if lng in supp_lng:
        return lng
    else:
        return choose_lng()


user_lng = choose_lng()

print(enter_pw_lng[user_lng])
user_password = str(input())

user_pw_lvl = password_validator(user_password)
print(f"{user_password} {levels[user_pw_lvl][supp_lng.index(user_lng)]}")
