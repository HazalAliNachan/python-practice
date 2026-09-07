income = float(input('Enter income: '))

if income<=250000:
    tax = 0
elif income<=500000:
    tax = (income-250000)*0.05
elif income<=1000000:
    tax = 250000*0.05+(income-500000)*0.2     
elif income<=2000000:
    tax = 250000*0.05+500000*0.2+(income-1000000)*0.3

print("Total Tax:",tax)        