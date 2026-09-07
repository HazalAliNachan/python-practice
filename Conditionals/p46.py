month = int(input("Enter month(1-12): "))

if month in (12,1,2):
    print("Winter")
elif 3<=month<=5:
    print("Spring")    
elif 6<=month<=8:
    print("Summer") 
elif 9<=month<=11:
    print("Autumn") 
else:
    print("Invalid Month Entered ")                   