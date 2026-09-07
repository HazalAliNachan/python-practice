year = int(input("Enter a year: "))

if year%400==0 or (year%4==0 and year%100!=0):
    print(year,"is a leapyear")
else:
    print(year,"is not a leapyear")    