#
# Project 2 - Generate a Random Name
#
# author:
#

# Import needed modules




# Generates a random number of cards to add to the player's hand
# return - number of cards dealt to player
def chance():
    # Declare an empty list in which to store the numbers


    # Use a for loop and random.randint to append 10 random numbers to the list
    # The random numbers should be between -5 and 5, inclusive

        
    # Print the possibilities for user
    # Print "You could win ..."
    # Then print the list items in two lines, 5 items per line
    # Items should be separated with two spaces
    
        
    # Randomly choose three elements from the list
    # random.choice or random.choices are good functions to use here
    # Make sure to store the random numbers

    

    # Compute the sum of the three random numbers
    # Store the sum in a variable

    
    
    # Display what player won
    # Print the three random elements chosen and their sum
    


    # Return how many cards the user won
    # (the sum of the three randomly chosen numbers)
    







###########################################################
# Main                                                    #
# Sets the random seed and calls your function            #
# With the seed set, your output should match the example #
###########################################################

print("Testing chance")
print()

for i in [3, 125, 6789]:
    random.seed(i)
    earned = chance()
    print("You earned " + str(earned) + " cards")
    print()
