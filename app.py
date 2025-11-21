print("Welcome to my Python program")
hoursSU = input("How many hours did you spend on your phone on Sunday?")
hoursM = input("How many hours did you spend on your phone on Monday?")
hoursT = input("How many hours did you spend on your phone on Tuesday?")
hoursW = input("How many hours did you spend on your phone on Wednesday?")
hoursTR = input("How many hours did you spend on your phone on Thursday?")
hoursF = input("How many hours did you spend on your phone on Friday?")
hoursS = input("How many hours did you spend on your phone on Saturday?")

hours = float(hours)


weekly_hours = hours * 7


print(f"Your screen time this week was: {weekly_hours} hours, which exceeds recommended weekly screen time")



try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()
