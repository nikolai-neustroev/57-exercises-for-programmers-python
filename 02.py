# 2.
# Counting the Number of Characters

def input_len():
    s = input()
    if len(s) == 0:
        print("Please enter something")
        input_len()
    else:
        print(s + " has " + str(len(s)) + " characters.")

print("What is the input string?")
input_len()
