weight = float(input("Please enter weight in kilograms: "))
height = float(input("Please enter height in meters: "))
bmi = weight/height**2
if bmi < 18.5:
    print("BMI is: {:.2f}, Status is Underweight".format(bmi))
elif bmi < 24.9:
    print("BMI is: {:.2f}, Status is Normal".format(bmi))
elif bmi < 29.9:
    print("BMI is: {:.2f}, Status is Overweight".format(bmi))
else:
    print("BMI is: {:.2f}, Status is Obese".format(bmi))
