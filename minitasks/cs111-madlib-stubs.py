#
# Author: 
# Date: 
# Description:
#
# This Madlib will require the following categories
#  adj  - http://examples.yourdictionary.com/examples-of-adjectives.html
#  noun  - http://examples.yourdictionary.com/noun-examples.html
#  adverb  - http://examples.yourdictionary.com/examples-of-adverbs.html
#  exclamation  - http://examples.yourdictionary.com/examples-of-interjections.html

import random
               
#
# This function is an implementation of the <REPLACE WITH MADLIB NAME> Madlib.
#   It will dynamically generate a new Madlib each time it is called by
#   randomly selecting values from the above lists
# Return
# This function will return a String containing the new Madlib
def generateMadlib():
    # Step 1. Define List variables for each category in your Madlib.  
    #    Add additional lists as necessary.
    ADJ_LIST = []
    NOUN_LIST = []
    ADVERB_LIST = []
    EXCLAMATION_LIST = []

    # Setup the output string that will contain the Madlib
    output = ""

    # Step 2. Write your Madlib below using String concatenation and the random.choice() function
    output += "Use String concatenation to write your madlib.\n"
    output += "Replace these lines with your Madlib"


    # Return generated Madlib
    return output




#
# Generate the Madlib
#
madlib = generateMadlib()

#
# Print the Madlib
#
print(madlib)


