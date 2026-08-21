time = int(input("Enter time in seconds: "))

hours = time//3600
mins = (time%3600)//60
sec = time%60
print(f"Hour:{hours}\nMinutes:{mins}\nSeconds:{sec}")

