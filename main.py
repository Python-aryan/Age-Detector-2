
# Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).

#

# Here are a few instructions that you must have to follow:

#

# Do not use any type of modules like DateTime or date utils. (-5 points)

# Users can optionally provide a year, and your program must tell their age in that particular year. (3points)

# Your code should handle all sort of errors like:                       (2 points)

# You are not yet born

# You seem to be the oldest person alive

# You can also handle any other errors, if possible!



print("Welcome To Our Programme")

aorb = input("To Enter your age Enter a, To enter your year of birth press b and\n"

             "To enter a year and want to check your age in that year press c\n")



if aorb=="a":

    age = int(input("Please enter your Age\n"))

    fage = 100-age

    print(f"You Are {age} years old and you need {fage} years to be at the Age of 100")



