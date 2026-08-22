p = float(input("Enter principle amount: "))
t = float(input("Enter time: "))
r = float(input("Enter rate: "))

# a = p*pow((1+r/100),t)
a = p*(1+r/100)**t
print("Final Amount:",a)
ci = a-p

print(f"Compound Interest:{ci}")