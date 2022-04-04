#
# Project 2 - Hands out cards randomly
#
# author:
#

# Import needed modules



# Deals multiple cards between 5 and 10 times.  The number of cards
# given each time are multiples of a random number between 3 and 10.
#
# For instance, you may be dealt the first 5 multiples of 3 (3, 6, 9,
# 12, 15) or the first 7 multiples of 10 (10, 20, 30, 40, 50, 60,
# 70)
#
# return: number of new cards dealt to player
#
#
# Examples:
# Number of deals: 5
# Multiple: 6
# Result: 6 + 12 + 18 + 24 + 30 = 90
# Return: 90
#
# Number of deals: 7
# Multiple: 3
# Result: 3 + 6 + 9 + 12 + 15 + 18 + 21 = 84
# Return: 84
#
def getCards():
    # Generate the number of times to deal cards
    #      --> generate and store a random number between 5 and 10

    
    # Generate the multiple in which to deal cards
    #      --> generate a random number between 3 and 10
    #      --> store in a variable named multiple

    
    # Initalize a variable to track the total number of cards given
    # to the player


    # Use a for loop to deal cards in multiples
    # Use range to start at 1 and end at 1 + the number of deals

        # Add i * multiple to the number of cards given to the player


    # return the number of cards given to the player

        
    



###########################################################
# Main - do not modify!                                   # 
# Sets the random seed and calls your function            #
# With the seed set, your output should match the example #
###########################################################

print("Testing getCards")
print()

# This only needs to happen once
# Do NOT set the seed inside your function!
random.seed(123)

playerCards = 0
playerExpected = 0

expected = [105, 135, 112]

# Deal some cards three times
for i in range(3):
    cards = getCards()
    playerCards += cards
    playerExpected += expected[i]

    print("\nExpected return: " + str(expected[i]))
    print("Got: " + str(cards))
    
    print("Player should have {} cards; actually has {}".format(playerExpected, playerCards))
