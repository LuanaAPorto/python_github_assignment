print("Welcome to my Python program")
hours_SU = input("How many hours did you spend on your phone on Sunday?")
hours_M = input("How many hours did you spend on your phone on Monday?")
hours_T = input("How many hours did you spend on your phone on Tuesday?")
hours_W = input("How many hours did you spend on your phone on Wednesday?")
hours_TR = input("How many hours did you spend on your phone on Thursday?")
hours_F = input("How many hours did you spend on your phone on Friday?")
hours_S = input("How many hours did you spend on your phone on Saturday?")

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
