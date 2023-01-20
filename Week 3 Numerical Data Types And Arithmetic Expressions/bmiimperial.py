weight = float(input("Please enter weight in pounds: "))
height = float(input("Please enter height in inches: "))
print("bmi is: {}".format(round(weight*0.453592/(height*0.0254)**2, 4)))
