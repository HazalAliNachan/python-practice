num = int(input("Enter a number: "))

if num%5==0 and num%11==0:
    print("Number is divisible by both 5 and 11")

elif num%5==0:
    print("Number is only divisible by 5")

elif num%11==0:
    print("Number is only divisible by 11")

else:
    print("Number is not divisible by 5 or 11")            