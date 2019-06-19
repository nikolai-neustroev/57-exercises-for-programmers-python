# These functions are used to input specific type values into the programs.


def append_vec_float(vec):
    try:
        vec.append(float(input()))
    except ValueError:
        print("Error. Input must be a number.")
        append_vec_float(vec)


def append_vec_int(vec):
    try:
        vec.append(int(input()))
    except ValueError:
        print("Error. Input must be a number.")
        return append_vec_int(vec)


def input_int():
    try:
        return int(input())
    except ValueError:
        print("Error. Input must be a number.")
        return input_int()


def input_float():
    try:
        return float(input())
    except ValueError:
        print("Error. Input must be a number.")
        return input_float()
