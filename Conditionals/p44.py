wgt = float(input("Enter weight in kg: "))
hgt = float(input("Enter height in m: "))

BMI = wgt/(hgt**2)

if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI < 25:
    print("Normal")
elif BMI >= 25 and BMI < 30:
    print("Overweight")
else:
    print("Obese")