# 38.
# Filtering Values


def filter_even(lst):
    tmp = []
    for i in lst:
        if i % 2 == 0:
            tmp.append(i)
    return tmp


print("Enter a list of natural numbers, separated by spaces: ")

print(f"""The even numbers are {' '.join(str(i) for i in filter_even(
    list(map(int, 
             str(input()).split()
             ))))}""")
