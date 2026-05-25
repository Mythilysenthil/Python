weight= float(input("Weight: "))
height= float(input("Height: "))
if weight > 0 and height > 0:
    bmi = weight / (height ** 2)
    print("Your BMI is:", format(bmi, ".2f"))
else:
    print("Please enter valid positive values for weight and height.")