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

    # Create a variable named colorIdx initialized to -1

    # Create a variable named animalIdx initialized to -1


    # Use a while loop
    # Loop while colorIdx or animalIdx has a value outside the range [0, 5]
    # (i.e. loop until colorIdx and animalIdx have valid values)

        # Ask the user for a value between 0 and 5
        # Store in colorIdx

        # Ask the user for a value between 0 and 5
        # Store in animalIdx

    
    
    # Use colorIdx as an index into colorList
    # Store that element from colorList in another variable
    

    # Use animalIdx as an index into animalList
    # Store that element from animalList in another variable
    
    

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

print("=" * 35)
print("Manual test of generate Name")
print("=" * 35)
name = generateName(colors, animals)
print("Name generated: " + name)

print()
print()
print("=" * 35)
print("Running automated input")
print("=" * 35)


try:
    originalIn = sys.stdin

    # Valid numbers
    testNums = [(0, 3), (5, 0), (3, 2)]
    for num1, num2 in testNums:
        testInput = StringIO("{0}\n{1}\n".format(num1, num2))
        sys.stdin = testInput
    
        name = generateName(colors, animals)
        print("\nExpected: " + colors[num1] + " " + animals[num2] + "\nGot: " + name)
        print()

    # Invalid numbers
    # -4, 5, 6, 2, 4, 1
    testInput = StringIO("-4\n5\n6\n2\n4\n1\n")
    sys.stdin = testInput
    num1 = 4
    num2 = 1
    name = generateName(colors, animals)
    print("\nExpected: " + colors[num1] + " " + animals[num2] + "\nGot: " + name)
    print()

    
except Exception as e:
    print("\n\nYour function misbehaved")
    print(e)

finally:
    sys.stdin = originalIn




