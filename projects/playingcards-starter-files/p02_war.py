#
# Project 2 - War
#
# author:
#

# Import any required modules



# Plays 10 rounds of War
# param: name - name of human player
#        numCards - number of cards currently in the player's hand
# return: number of cards player has at the end of the round
def war(name, numCards):
    # Initialize a variable to keep track of number of rounds


    # Use a while loop to play
    # Loop while the player still has cards AND the player has played less than 10 rounds

        
        # Prompt user to press enter to draw cards


        # Use random.randint to pick two cards between 1 and 10
        # The first card is the player's, the second is the computer's
      

        # Print the cards that were drawn using the player's name


        # Use an if/elif/else to determine who wins
        # The card with the highest value wins
        # If the player wins, add one card to the player's hand and print
        #          "[name] wins!" where [name] is replaced with the player's name


        # Else if the player loses, remove one card from the player's hand and print "Computer wins!"

    
        # Otherwise, it's a draw (the cards are equal), no cards are earned or lost and print "It's a draw..."

    

        # Print the number of cards now in the player's hand using the player's name


        # Increment the round counter

    

    # Return the number of cards in the player's hand
        




#########################################################
# Main                                                  #
# Calls the function - you don't need to modify this    #
# Check your output                                     #
# If the computer wins, do you lose a card?             #
# If the player wins, do you gain a card?               #
# If it's a draw, number of cards should not change     #
# Do you get a negative number of cards? You shouldn't! #
#########################################################


# Seed random so your output matches the example output
random.seed(100)

print("Playing war!\n")

# Starting hand
cards = 3
name = "Purple Koala"

# Play war
cards = war(name, cards)

# Print the hand
print("\nAfter the first round of war, " + name + " has " + str(cards) + " cards\n")

# Play war again
cards = war(name, cards)

# Print the hand
print("\nAfter the second round of war, " + name + " has " + str(cards) + " cards\n")


