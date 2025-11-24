print("Welcome to my Python program"). #Welcome message

try:  #to make sure all inputs are valid numbers

#Asks users for their screen time each day of the week individualy

    hours_SU = input("How many hours did you spend on your phone on Sunday? ") 
    hours_M = input("How many hours did you spend on your phone on Monday? ")
    hours_T = input("How many hours did you spend on your phone on Tuesday? ")
    hours_W = input("How many hours did you spend on your phone on Wednesday? ")
    hours_TR = input("How many hours did you spend on your phone on Thursday? ")
    hours_F = input("How many hours did you spend on your phone on Friday? ")
    hours_S = input("How many hours did you spend on your phone on Saturday? ")

#Converting inputs to float

    hours_SU = float(hours_SU)
    hours_M = float(hours_M)
    hours_T = float(hours_T)
    hours_W = float(hours_W)
    hours_TR = float(hours_TR)
    hours_F = float(hours_F)
    hours_S = float(hours_S)

#Calculating the weekly screen time of the user, based on the collected information,inputs

    weekly_hours = hours_SU + hours_M + hours_T + hours_W + hours_TR + hours_F + hours_S 

#Return a positive message if the value for weekly_hours is up to 15

    if weekly_hours <= 15:
        print("Your weekly screen time, of {weekly_hours} hours, looks great! Keep it up")

#Return a negative message if the value for weekly_hours is more than 15
    else:
        print(f"Your screen time this week was: {weekly_hours} hours, which exceeds recommended weekly screen time.")

#Return message asking for user to enter a valid input(numbers, not letters)
except ValueError:
    print("Please enter a valid number.")
    exit()
