# 28.
# Adding numbers

from inputplus import append_vec_float, input_int

numbers = []


def initial():
    print("How many numbers do you want to add?")
    return input_int()


n = initial()

for i in range(n):
    print("Enter a number: ")
    append_vec_float(numbers)

print(f"The total is: {sum(numbers)}")
