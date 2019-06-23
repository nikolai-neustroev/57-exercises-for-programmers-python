# 29.
# Handling Bad Input.


def input_r():
    try:
        r = float(input())
        while r == 0:
            print("Error. Zero is not a valid input.")
            return input_r()
        else:
            return r
    except ValueError:
        print("Error. Input must be a number.")
        return input_r()


print("What is the rate of return?")
user_r = input_r()
years = 72.0 / user_r
print(f"It will take {years} years to double your initial investment.")
