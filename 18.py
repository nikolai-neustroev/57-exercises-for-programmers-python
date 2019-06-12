# 18.
# Temperature Converter


def input_temp():
    try:
        amount = float(input())
        return amount
    except ValueError:
        print("Error. Input must be a number.")
        return input_temp()


def temp_conv():
    print("""Press C to convert from Fahrenheit to Celsius.
Press F to convert from Celsius to Fahrenheit.""")
    unit = str(input()).upper()

    if unit == "F":
        print("""Your choice: F
Please enter the temperature in Fahrenheit:""")
        fah = input_temp()
        cel = (fah - 32) * 5 / 9
        print(f"The temperature in Celsius is {cel}")
    elif unit == "C":
        print("""Your choice: C
Please enter the temperature in Celsius:""")
        cel = input_temp()
        fah = (cel * 9 / 5) + 32
        print(f"The temperature in Fahrenheit is {fah}")
    else:
        return temp_conv()


temp_conv()
