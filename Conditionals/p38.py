age= int(input("Enter your age: "))

if age>=18:
    print("You Can Vote")
else:
    print("You Cannot Vote")    
    print("You can vote after",18-age,"year(s)")