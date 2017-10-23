# Author:  
# Date:  
# Description:  Retro Arcade - Component Two - Slots Game

# Step 1: Import required libraries


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
    symbolList = ["Cherry", "Lemon", "Seven", "Diamond", "Heart"]
    
    # Step 2: The game should begin by displaying a welcome message including the
    #    name of the game (Slots) and the players name.


    # Step 3: Declare an integer variable called attempts to track the number of attempts.  
    #    What should the initial value be?


    # Step 4: Declare a boolean variable called playerHasWon and set it to false to 
    #    indicate that the player has not won yet

    
    # Step 5: The game will continue while the number of attempts is less than 5
    #    and the player hasnt won.


        # Step 6: Print the number of attempts remaining for the player


        # Step 7: Prompt the player to Press Enter to pull the handle


        # Step 8: Randomly select three symbols from a List containing game symbols
        #       and store each to a variable


        # Step 9: Print the selected symbols on a single line with several spaces
        #   between each character


        # Step 10: Check if all three symbols match, set the player has won flag to True


        # Step 11: Increment the number of attempts


    # Step 12: Return whether the player has won


   

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
    winnerString = "*  Computer Wins!  *"
    
starBorder = "*" * len(winnerString)
print(starBorder)
print(winnerString)
print(starBorder)
    
    

    
