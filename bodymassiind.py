
# weight = input("Enter your weight: ")
# height = input("Enter your height: ")
# w = float(weight)
# h = float(height)
# bmi = int((w/(h**2)))
# print("Your BMI is " + str(bmi))


# *****Upgraded version of BMI---BMI2******
# Using the F-string to print and rounding of numbers
name = input("What is your name? ")
weight = input("Enter your weight in kilogram: ")
height = input("Enter your height in metres: ")
w = float(weight)
h = float(height)
# bmi = int((w/(h**2)))
bmi = round(w/(h**2))
if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are UNDERWEIGHT. ")
elif bmi < 25:
    print(f"Your BMI is {bmi} and you have a NORMAL WEIGHT. ")
elif bmi < 30:
    print(f"Your BMI is {bmi} and you are OVERWEIGHT. ")
elif bmi < 35:
    print(f"Your BMI is {bmi} and you are OBESE")
else:
    print(f"Your BMI is {bmi} and you are CLINICALLY OBESE. ")
print(f"THANK YOU {name} FOR CHECKING YOUR BMI. ")

