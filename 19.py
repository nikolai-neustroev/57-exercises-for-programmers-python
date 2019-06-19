# 19.
# BMI Calculator

from inputplus import input_float


def calc_bmi():
    print("Press I for Imperial units or M for metric.")
    syst = str(input()).upper()
    if syst == "I":
        print("Please enter your height (first feet, then inches).")
        feet = input_float()
        inches = input_float()
        height = feet * 12.0 + inches
        print("Please enter your weight (lb).")
        weight = input_float()
        bmi = weight / (height**2) * 703.0
        print(f"Your BMI is {round(bmi, 1)}.")
        return bmi
    elif syst == "M":
        print("Please enter your height (cm).")
        height = input_float()
        print("Please enter your weight (kg).")
        weight = input_float()
        bmi = weight / ((height/100.0)**2)
        print(f"Your BMI is {round(bmi, 1)}.")
        return bmi
    else:
        return calc_bmi()
    

def check_bmi(calcd_bmi):
    if calcd_bmi < 18.5:
        print("You are underweight. You should see your doctor.")
    elif calcd_bmi > 25.0:
        print("You are overweight. You should see your doctor.")
    else:
        print("You are within the ideal weight range.")
        

user_bmi = calc_bmi()
check_bmi(user_bmi)
