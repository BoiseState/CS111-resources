#
# Project 2 - Generate a Random Name
#
# author:
#

# Import needed modules (if any)



# Generates a random name in the form Color Animal
# param: colorList - list of six color choices
#         animalList - list of six animal choices
# return: string, the generated name
def generateName(colorList, animalList):

    # Create a boolean variable called isValid and initalize it to False
    # This boolean tracks if the user has entered valid numbers


    # Use a while loop
    # Loop as long as isValid is False (Hint: use 'not' in your condition)

    
        # Ask for a number between 0 and 5

        # Ask for another number between 0 and 5

        # Set the value of isValid by using a boolean expression that
        # evaluates to True if and only if both numbers are in the
        # range 0 - 5, inclusive
        # Remember, you can store the results of boolean expressions
        # For example -- isGood = num > 10
        # Hint: both numbers have to be at least 0 and no greater than 5


    
    # Use the first number the user gave as an index into colorList
    # Store that element in another variable
    

    # Use the second number the user gave as an index into animalList
    # Store that element in another variable
    
    

    # Return a string that concatenates the color element with the animal element
    # Don't forget to put a space between the color and the animal!
    





###########################################################################
# Main - do not modify!                                                   #
# Tests your function                                                     #
# Will automatically provide input to your function, except the first call #
###########################################################################

from io import StringIO
import sys


colors = ["Red", "Orange", "Violet", "Rose", "Purple", "Aqua"]
animals = ["Bear", "Tiger", "Bat", "Aardvark", "Mouse", "Fly"]

print("Manual test of generate Name")
name = generateName(colors, animals)
print("Name generated: " + name)

print()
print()
print("Running automated input")


try:
    originalIn = sys.stdin

    # Valid numbers
    testNums = [(0, 3), (5, 0), (3, 2)]
    for num1, num2 in testNums:
        testInput = StringIO("{0}\n{1}\n".format(num1, num2))
        sys.stdin = testInput
    
        name = generateName(colors, animals)
        print("\nShould have generated " + colors[num1] + " " + animals[num2] + "; Got " + name)
        print()

    # Invalid numbers
    # -4, 5, 6, 2, 4, 1
    testInput = StringIO("-4\n5\n6\n2\n4\n1\n")
    sys.stdin = testInput
    num1 = 4
    num2 = 1
    name = generateName(colors, animals)
    print("\nShould have generated " + colors[num1] + " " + animals[num2] + "; Got " + name)
    print()

    
except Exception as e:
    print("\n\nYour function misbehaved")
    print(e)

finally:
    sys.stdin = originalIn



