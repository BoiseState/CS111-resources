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
    return ""



####################################
## Data
###################################

#
# Single string containing CSV formatted quiz question
#  "category,pointvalue,question,answer"
#
singleQuestionCSV = "Cats,100,Cats hate this,water"

#
# List of strings containing CSV formatted quiz data
#
questionList = ["Dinos,500,My existence has been debated but I have very long neck,brontosaurus",
                "Cats,200,This killed the cat,curiosity",
                "Math,200,Square me to get 100,10",
                "Dinos,100,Famous carnivore,t-rex",
                "Cats,400,Tiger + Lion =,liger",
                "Dinos,400,Turns out dinosaurs were covered in these,feathers",
                "Math,200,You wish you could eat this numerical constant,pi",
                "Math,400,It measures round and round and round,circumference",
                "Math,100,2 + 2 =,4",
                "Dinos,200,They have three horns,triceratops"]




#####################################
## Main
#####################################

### Step One ###

# Split singleQuestionCSV using a comma as a delimiter and store the result in a new list

# Use the constants at the top of the file to access the pieces of the question.
# Print the information, one part per line.
# Label each part when you print it.

### End Step One ###

### Step Two ###
# Implement getInfo function above #
### End Step Two ###


### Step Three ###

# Print the information again, but this time 
# call getInfo to get each part



### End Step Three ###



### Step Four ###

# Use len to print how many questions are in the questionList


# Use a for loop to print the category and value of each question in questionList



### End Step Four ###
