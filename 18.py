# 18.
# Temperature Converter

from inputplus import input_float


def temp_conv():
    print("""Press C to convert from Fahrenheit to Celsius.
Press F to convert from Celsius to Fahrenheit.""")
    unit = str(input()).upper()

    if unit == "F":
        print("""Your choice: F
Please enter the temperature in Fahrenheit:""")
        fah = input_float()
        cel = (fah - 32) * 5 / 9
        print(f"The temperature in Celsius is {cel}")
    elif unit == "C":
        print("""Your choice: C
Please enter the temperature in Celsius:""")
        cel = input_float()
        fah = (cel * 9 / 5) + 32
        print(f"The temperature in Fahrenheit is {fah}")
    else:
        return temp_conv()


temp_conv()
