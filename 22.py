# 22.
# Comparing Numbers

vec = []


def input_number():
    try:
        amount = float(input())
        return amount
    except ValueError:
        print("Error. Input must be a number.")
        return input_number()


def append_vec():
    print("Please enter a number.")
    tmp = input_number()
    if tmp in vec:
        print("You've already entered this number. Please try another one.")
        return append_vec()
    else:
        vec.append(tmp)


print("How many numbers do you want to compare?")
n = int(input_number())

while len(vec) < n:
    append_vec()

maximum = vec[0]

for i in vec:
    if i > maximum:
        maximum = i

print(f"The largest number is {maximum}.")
