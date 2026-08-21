# Method1
# a,b,c = input("Enter three numbers: ").split()
# a = int(a)
# b = int(b)
# c = int(c)

# sum = a+b+c
# avg = sum/3
# print("Average:",avg)

# Method2
a,b,c = map(int,input("Enter three numbers: ").split())
sum = a+b+c
avg = sum/3
print(f"Average:{avg:.2f}")
