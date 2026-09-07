a,b,c = map(int,input("Enter three sides: ").split())

if a+b>c and b+c>a and a+c>b:
    if a==b==c:
        print("Equilateral Triangle")
    elif a==b or b==c or c==a:
        print("Isoceles Triangle")
    else:
        print("Scalene Triangle")    
else:
    print("Invalid Input")        