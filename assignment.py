# 6. Write a program to check if an input number is a multiple of 5 or not.
# 7. Write a program to check if a string contains only alphabets and numbers or not. 
# Print, "YES" if it only contains numbers and letters, otherwise print "NO".
# 8. Write a program to check if the length of a string is an even number. 
input_string = input("Enter a string: ")
if len(input_string) % 2 == 0:
    print("Even length")
else:
    print("Odd length")

# Print "Even length" if true, otherwise "Odd length."
# 9 . Write a program to convert temperature from degree Celsius to Fahrenheit and Kelvin.
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Convert to Kelvin
kelvin = celsius + 273.15

print(f"Temperature in Fahrenheit: {fahrenheit}°F")
print(f"Temperature in Kelvin: {kelvin}K")

# 10. Write a program to check if a number is a perfect square. Print 
# "Perfect square" if true, otherwise "Not a perfect square."
import math
number = int(input("Enter a number: "))
sqrt = math.isqrt(number)

if sqrt * sqrt == number:
    print("Perfect square")
else:
    print("Not a perfect square")


# 6. Write a program to check if an input number is a multiple of 5 or not.
number = int(input("Enter a number: "))
if number % 5 == 0:
    print("The number is a multiple of 5.")
else:
    print("The number is not a multiple of 5.")

# 7. Write a program to check if a string contains only alphabets and numbers or not. 
input_string = input("Enter a string: ")
if input_string.isalnum():
    print("YES")
else:
    print("NO")

# 10. Write a program to check if a number is a perfect square. Print 
# "Perfect square" if true, otherwise "Not a perfect square."
