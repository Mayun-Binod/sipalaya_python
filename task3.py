# 1. Write a program to check if given year is leap year or not
# 2. Write a program to return the grade of a person according to the marks they received.  
# Example:
# input: Enter your marks: 90
# Output : Distinction

# 3. Write a program to take age as input from user and check whether the user is illegible for voting or not.
# 4. Write a program to check if a number is between 1 and 100. Print "In range" if true, otherwise "Out of range." 
# 5. Write a program to take time as input from user. Print "Morning" if the time is between 7 to 12.
# Print "Afternoon" if the time is between 12 to 3. Print "Evening" if the time is between 3 to 6. Else print "night"

# 1. An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
# In the Gregorian calendar, three conditions are used to identify leap years:
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year. This means that in the Gregorian calendar, the years 2000 and 2400 are leap years,
# while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

# 2. Write a program to return the grade of a person according to the marks they received. 
# Example:
# input: Enter your marks: 90
# Output : Distinction

marks=int(input("Enter your marks:"))
if marks>=90:
    print("you got distinction.")
elif marks<90 and marks>=80:
    print("you got first position")
elif marks<80 and marks>=70:
    print("you got second position")
elif marks<70 and marks>=40:
    print("you got third position")
else:
    print("sorry try again !")

# 3. Write a program to take age as input from user and check whether the user is illegible for voting or not.
age_user=int(input("Enter your age:"))
if age_user>=18:
    print("yes you are valid to vote")
else:
    print("sorry you cannot vote")

# 4. Write a program to check if a number is between 1 and 100. Print "In range" if true, otherwise "Out of range." 
number_as_user=int(input("Enter the number:"))
if number_as_user<=100 and number_as_user>=1:
    print("in range")
else:
    print("out if range")

# 5. Write a program to take time as input from user. Print "Morning" if the time is between 7 to 12.
# Print "Afternoon" if the time is between 12 to 3. Print "Evening" if the time is between 3 to 6. Else print "night"

user_time=int(input("please enter the time:"))
if user_time>=24:
    print("time is per a day.")
elif user_time<24 and user_time>=12:
    print("you are between 12 to 24 hours.")
else:
    print("sorry you are out of hours.")

