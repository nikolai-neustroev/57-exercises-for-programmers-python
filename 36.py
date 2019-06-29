# 36.
# Computing Statistics
from inputplus import input_float
from copy import deepcopy
from statistics import stdev


def isnum(s):
    try:
        float(s)
    except:
        return(False)
    else:
        return(True)


def inp_vec(el, vec):
    if el is "done":
        return el, vec
    else:
        try:
            vec.append(float(el))
            return el, vec
        except ValueError:
            print("Input must be a number")
            return inp_vec(el, vec)


def add_num():
    print("Enter a number (enter 'done' to finish):")
    number = input()
    if isnum(number) or number == "done":
        return number
    else:
        print("Input must be a number")
        return add_num()


def maximum(arr):
    mx = arr[0]
    for i in arr:
        if mx < i:
            mx = i
    return mx


def minimum(arr):
    mn = arr[0]
    for i in arr:
        if mn > i:
            mn = i
    return mn


def average(arr):
    return sum(arr) / len(arr)


print("Enter a number:")
usr_inp = input_float()
usr_vec = []

while usr_inp != "done":
    usr_inp, usr_vec = inp_vec(usr_inp, usr_vec)
    usr_inp = add_num()

print(f"""Numbers: {usr_vec}.
The average is {average(usr_vec)}.
The maximum is {maximum(usr_vec)}.
The minimum is {minimum(usr_vec)}.
The standard deviation is {stdev(usr_vec)}""")

