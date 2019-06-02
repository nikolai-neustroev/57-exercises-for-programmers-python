# 9.
# Paint Calculator
import math

paint_const = 350 #sq. feet covered by 1 gallon
dims = []

def input_dim():
    try:
        dims.append(float(input()))
    except ValueError:
        print("Error. Input must be a number.")
        return input_dim()

def output_vol(area):
    total_paint = area / paint_const
    ceiled_paint = math.ceil(total_paint)
    print(f"You will need to purchase {ceiled_paint} gallons of paint to cover {area} square feet.")

def paint_vol():
    print("""Please choose your room\'s shape.
Type \"rect\" for a rectangular room,
\"round\" for a round room, \"L\" for L-shaped room.""")
    room_shape = input()

    if room_shape == "rect":
        print("Enter the length of a room in feet:")
        input_dim()
        print("Enter the width of a room in feet:")
        input_dim()

        area = dims[0] * dims[1]
        output_vol(area)

    elif room_shape == "round":
        print("Enter the radius of a room in feet:")
        input_dim()

        area = dims[0]**2 * 3.14159265359
        output_vol(area)

    elif room_shape == "L":
        print("Enter the larger length of a room in feet:")
        input_dim()
        print("Enter the smaller length of a room in feet:")
        input_dim()
        print("Enter the larger width of a room in feet:")
        input_dim()
        print("Enter the smaller width of a room in feet:")
        input_dim()

        area = dims[0] * dims[2] - dims[1] * dims[3]
        output_vol(area)

    else:
        return paint_vol()

paint_vol()
