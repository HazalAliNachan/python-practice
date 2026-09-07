while True:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    op = input("+,-,*,/: ")

    match op:
        case "+":
            print("Result: ",a+b)
        case "-":
            print("Result: ",a-b)   
        case "*":
            print("Result: ",a*b)     
        case "/":
            if b==0:
                print("Cannot divide by zero")
            else: 
                print("Result: ",a/b) 
        case _:
            print("Invalid Operator")          