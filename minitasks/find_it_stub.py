#
# Author:
# Date:
# Description:
#


# Constants used to refer to the parts of the quiz question
CATEGORY = 0
VALUE = 1
QUESTION = 2
ANSWER = 3


#
#  Read lines of text from a specified file and create a list of those lines
#    with each line added as a separate String item in the list
#
# Parameter
#   inputFile - A String with the name of a text file to convert to a Lit
#
# Return
#   A List containing each line from the text file
def getListFromFile (inputFile):
    outputList = []
    try:
        source = open(inputFile,"r")
        outputList =  source.readlines()
        source.close()
    except FileNotFoundError:
        print("Unable to open input file: " + inputFile)

    return outputList


#
# Splits a String containing all question information, then
# returns the specified part of the question
#
#
# Parameters
#   question - String containing comma separated quiz question details
#   whichInfo - constant representing which part of the question to return
#                should be one of CATEGORY, VALUE, QUESTION, ANSWER
# Return
#   String containing the specified part of the question
def getInfo(question, whichInfo):
    # paste your getInfo implementation here
    return ""



#####################################
## Main
#####################################


# Read the CSV file and get a list of contents

# Create a new list in which to store the categories

# Iterate through the file contents to get each category
# If the category isn't in the category list already, add the category to the category list
# HINT: to check if something IS in a list, you use -- if elem in myList:
#       to check if something IS NOT in a list you use -- if elem not in myList:


# Use a for loop to print all the categories
