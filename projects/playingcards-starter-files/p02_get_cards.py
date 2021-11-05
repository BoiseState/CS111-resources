#
# Project 2 - Generate a Random Name
#
# author:
#

# Import needed modules

import random


# Randomly deals some cards
# param: currentCards - the number of cards the player currently has
# return: total number of cards in the hand (including the newly dealt cards)
def getCards(currentCards):
    # declare a variable to store the number of times to deal cards
    # initialize it to 0

    # declare a variable to store the number of cards
    # initialize it to 0


    # Use an if/else
    # If the user already has cards (currentCards is greater than 0),

        # Set the number of deals to 3

        # Set the number of cards to currentCards

    # Otherwise,
        # Set the number of deals to 6



    # Use a for loop
    # Iterate number of deals times (either 3 or 6)

        # Generate and store a random number between 0 and 4, inclusive

        # Add the number to the number of cards


    # return the number of cards




###########################################################
# Main - do not modify!                                   # 
# Sets the random seed and calls your function            #
# With the seed set, your output should match the example #
###########################################################

print("Testing getCards")
print()


random.seed(123)

cards = 0

# Deal cards three times
for i in range(3):
    print()
    print("Starting with " + str(cards) + " cards")
    cards = getCards(cards)
    print("Now I have " + str(cards) + " cards")
    print()
