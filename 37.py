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


def inp_dig(pass_len):
    print("How many digits?")
    len_dig = int(input_int())
    if len_dig >= pass_len:
        print("""There must be at least one digit, one special character, and one letter.
The number of digits cannot exceed total number of symbols.""")
        return inp_dig(pass_len)
    else:
        return len_dig


def inp_spc(pass_len):
    print("How many special characters?")
    len_spc = int(input_int())
    if len_spc >= pass_len:
        print("""There must be at least one digit, one special character, and one letter.
The number of special characters cannot exceed total number of symbols.""")
        return inp_spc(pass_len)
    else:
        return len_spc


print("Input length:")
usr_len = int(input_int())

usr_len_dig = inp_dig(usr_len)

# Updating usr_len to prevent usr_len_spc going out of the limit
usr_len = usr_len - usr_len_dig

usr_len_spc = inp_spc(usr_len)

chr_len = usr_len - usr_len_spc

password = chr_pass(chr_len) + num_pass(usr_len_dig) + spc_pass(usr_len_spc)
password = list(password)
password = random.sample(password, len(password))
password = "".join(password)

print(f"""Random string is:
{password}""")
