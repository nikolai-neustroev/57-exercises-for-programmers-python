# 35.
# Picking a Winner

from random import choice

contestants = []

usr_inp = None

while usr_inp != "":
    print("Enter a name")
    usr_inp = input()
    contestants.append(usr_inp)

print(f"The winner is... {choice(contestants)}!")
