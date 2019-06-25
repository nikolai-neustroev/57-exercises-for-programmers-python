# 31.
# Karvonen Heart Rate

from inputplus import input_int

print("How old are you?")
age = input_int()
print("What is your resting heart rate?")
restingHR = input_int()

print("Intensity     |   Rate")
for intensity in range(55, 100, 5):
    targetHR = (((220 - age) - restingHR) * intensity / 100) + restingHR
    print(f"{intensity}%           |   {round(targetHR)} bpm")
