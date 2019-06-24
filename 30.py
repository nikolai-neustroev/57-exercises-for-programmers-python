# 30.
# Multiplication Table


def table_generator():
    for i in range(13):
        for j in range(13):
            if (i*j) > 0:
                yield i*j


for ind, el in enumerate(table_generator()):
    if len(str(el)) == 1:
        el = "  " + str(el)
    elif len(str(el)) == 2:
        el = " " + str(el)
    else:
        el = str(el)
    print(el, end=" ") if ((ind+1) % 12) != 0 else print(el, end="\n")
