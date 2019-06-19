# 7.
# The Area of a Rectangular Room

from inputplus import append_vec_float

f2m = 0.09290304
m2f = 3.280839895
dims = []


def choose():
    print("Please choose the prefered unit. Press \"m\" for meter or \"f\" for foot.")
    unit = input()
    if unit == "m":
        print("What is the length of the room in meters?")
        append_vec_float(dims)
        print("What is the width of the room in meters?")
        append_vec_float(dims)

        area_m = dims[0] * dims[1]
        area_f = round(area_m * m2f, 3)

        print(f"""You entered dimensions of {dims[0]} by {dims[1]} meters.
The area is
{area_m} square meters
{area_f} square feet""")

    elif unit == "f":
        print("What is the length of the room in feet?")
        append_vec_float(dims)
        print("What is the width of the room in feet?")
        append_vec_float(dims)

        area_f = dims[0] * dims[1]
        area_m = round(area_f * f2m, 3)

        print(f"""You entered dimensions of {dims[0]} by {dims[1]} feet.
The area is
{area_f} square feet
{area_m} square meters""")

    else:
        choose()

choose()
