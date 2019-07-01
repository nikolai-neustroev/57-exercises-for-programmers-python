# 37.
# Password Generator

from inputplus import input_int
import random
import string


def chr_pass(length):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for i in range(length))


def num_pass(length):
    numbers = string.digits
    return "".join(random.choice(numbers) for i in range(length))


def spc_pass(length):
    spc = string.punctuation
    return "".join(random.choice(spc) for i in range(length))


def inp_num(pass_len):
    print("How many numbers?")
    len_num = int(input_int())
    if len_num >= pass_len:
        print("The number of digits cannot exceed total number of symbols.")
        return inp_num(pass_len)
    else:
        return len_num


def inp_spc(pass_len):
    print("How many special characters?")
    len_spc = int(input_int())
    if len_spc >= pass_len:
        print("The number of special characters cannot exceed total number of symbols.")
        return inp_spc(pass_len)
    else:
        return len_spc


print("Input length:")
usr_len = int(input_int())

len_num = inp_num(usr_len)

len_spc = inp_spc(usr_len)

print(len_num)
len_spc
chr_len = usr_len - len_num - len_spc

password = chr_pass(chr_len) + num_pass(len_num) + spc_pass(len_spc)
password = list(password)
password = random.sample(password, len(password))
password = "".join(password)

print(f"""Random string is:
{password}""")
