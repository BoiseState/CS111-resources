# Author:  
# Date:  
# Description:  Jackpot Challenge - Component Two - Slots Game

# Import required libraries


#
# This is a single player game where the player has five attempts to randomly
#   select three items and match all three.  If the player draws three matching
#   items, then the game is over and the player wins.  If the completes five
#   attempts without drawing a match, the game is over and the player loses.
#
# Parameters
#   name - Name of the current player
#
# Returns
#   True - Player Wins
#   False - Player Loses
def playGameOfSlots(name):
    # Create List of Game Symbols (unicode characters)
    # Actual slot machines have 20 symbols per wheel
    # https://unicode-table.com/en
    symbolList = [u"\u2762",u"\u2600", u"\u2605", u"\u2602", u"\u265E", u"\u262F", u"\u262D", u"\u2622",u"\u260E", u"\u221E", u"\u2744", u"\u266B"]
    
    # The game should begin by displaying a welcome message including the
    #    name of the game (Slots) and the player’s name.


    # The game should have a variable to track the number of attempts.


    # Set a boolean variable to indicate that the player has not one yet

    
    # The game will continue while the number of attempts is less than 5
    #    and the player hasn’t won.
    while attempts < 5 and playerHasWon == False:
        # Print the number of attempts


        # Prompt the player to “Press Enter to pull the handle”


        # Randomly select three values from a List containing game symbols


        # Print the selected symbols on a single line with several spaces
        #   between each character


        # If all three symbols match, the player has won


        # Increment the number of attempts


    # Return whether the player has won
   


######################################################################
# The code below this comment is what runs the program.  Please      #
#   take the time to look at how your function is being called and   #
#   what is being done with the return value, but you do not need    #
#   to modify this code to complete the component.                   #
######################################################################             
        
# Setup a default player
playerName = "Bob"

# Call the function and store the result
playerWins = playGameOfSlots(playerName)

# Display the winner!
if playerWins == True:
    winnerString = "*  " + playerName + " Wins!  *"
else:
    winnerString = "*  House Wins!  *"
    
starBorder = "*" * len(winnerString)
print(starBorder)
print(winnerString)
print(starBorder)
    
    

    
