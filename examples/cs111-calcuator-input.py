# Author:  Luke Hindman
# Date:  Tue Oct 24 13:14:40 MDT 2017
# Description:  In-class example for user input

# Display welcome message
print("Welcome to the Simple Calculator where all we do is add!")

# Prompt the user for two numbers
num1 = input("Please enter the first number: ")
num2 = input("Please enter the second number: ")

# Calculate the sum of the two numbers, must cast the strings before addition
sum = int(num1) + int(num2)

# Display the result
print("The sum of " + num1 + " and " + num2 + " is " + str(sum))
