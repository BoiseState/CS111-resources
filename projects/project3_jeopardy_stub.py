# Summary:
# author:
# date:


import random

# Constants for the parts of a question
CATEGORY = 0
VALUE = 1
QUESTION = 2
ANSWER = 3

# Constant representing a used question
NO_QUESTION = "____"



# Copy your getInfo function from the minitask
def getInfo(quesInfo, whichInfo):
    return "Not implemented"



# Read in a file and return a list containing the lines in the file
# Strip each line to remove the \n
# Copy getListFromFile to get you started
def loadCSV(filename):
    return []


# Takes a list containing every line from the question csv list
# Returns a new list containing only the categories
def getCategoryList(fileList):
    return []




# Takes a list containing every line from the question csv list
# Returns a new list containing only the questions whose category is in categoryList
def getQuestionList(fileList, categoryList):
    return []



# Prints question board
# For example:
# Q0($100)  Q1($200)  Q2($400)
# Q3($200)  Q4($150)  Q5($600)
# Q6($200)  Q7($150)  Q8($600)
#
# Be careful to check if there's actually a question before trying to get the question's value
# Does not return anything
def printBoard(questionList):
    print("PRINTING BOARD")
    


# Checks question list for a valid question
# If every element is NO_QUESTION, return false
# If at least one element has text, return true
def hasQuestions(questionList):
    return True


# Asks user which question he/she wants to answer
# Validates the number - is it in the right range? Is that element a question (i.e. is not NO_QUESTION)
# Use a try/except to handle the case the user gives you something that isn't a number
# See Day 26 slides for example try/except
# Returns a valid number
def getQuestionIndex(questionList):
    return 0





##########################################
## Main
##################################

# Put your main game loop code here!
