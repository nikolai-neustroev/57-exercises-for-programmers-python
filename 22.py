# 22.
# Comparing Numbers

from inputplus import input_float

vec = []


def append_vec():
    print("Please enter a number.")
    tmp = input_float()
    if tmp in vec:
        print("You've already entered this number. Please try another one.")
        return append_vec()
    else:
        vec.append(tmp)


print("How many numbers do you want to compare?")
n = int(input_float())

while len(vec) < n:
    append_vec()

maximum = vec[0]

for i in vec:
    if i > maximum:
        maximum = i

print(f"The largest number is {maximum}.")
