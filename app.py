print("Welcome to my Python program")
hoursSU = input("How many hours did you spend on your phone on Sunday?")
hoursM = input("How many hours did you spend on your phone on Monday?")
hoursT = input("How many hours did you spend on your phone on Tuesday?")
hoursW = input("How many hours did you spend on your phone on Wednesday?")
hoursTR = input("How many hours did you spend on your phone on Thursday?")
hoursF = input("How many hours did you spend on your phone on Friday?")
hoursS = input("How many hours did you spend on your phone on Saturday?")

hours_SU = float(hours_SU)
hours_M = float(hours_M)
hours_T = float(hours_T)
hours_W = float(hours_W)
hours_TR = float(hours_TR)
hours_F = float(hours_F)
hours_S = float(hours_S)

weekly_hours = hours_SU + hours_M + hours_T + hours_W + hours_TR + hours_F + hours_S 

if weekly_hours <= 15:
    print("Your weekly screen time, of {weekly_hours} hours, looks great! Keep it up")

else:
print(f"Your screen time this week was: {weekly_hours} hours, which exceeds recommended weekly screen time.")


try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()
