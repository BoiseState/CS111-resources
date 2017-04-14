# Author:  
# Date:  
# Description:  Jackpot Challenge - Component One - Dice Game


# Import required libraries


#
# This game is player vs house where each take turns rolling a single six-sided
#    die.  The player with the highest roll each round wins a point.  The house
#    receives the point for a tie.  The first player to 5 points wins.
#
# Parameters
#   name - Name of the current player
#
# Returns
#   True - Player Wins
#   False - Player Loses
def playGameOfDice(name): 

    # The game should begin by displaying a welcome message including the
    #    name of the game (Dice) and the players name.


    # The game should have a variable for tracking the player's score
    #    and a variable for tracking the house's score

    
    # The game will continue while the players score is less than 5
    #    and the houses score is less than 5.

        
        # Print the current scores
        
        # Prompt the player to Press Enter to roll

        # Randomly generate integer value for players roll

        # Randomly generate integer value for houses roll

        # Compare results, print winner message, including name
        #    and increment the score of the winner


    # If the player score is greater than the house score, the player Wins so return True.
    #    Otherwise, return false.
            

######################################################################
# The code below this comment is what runs the program.  Please      #
#   take the time to look at how your function is being called and   #
#   what is being done with the return value, but you do not need    #
#   to modify this code to complete the component.                   #
######################################################################
        
# Setup a default player
playerName = "Bob"

# Call the function and store the result
playerWins = playGameOfDice(playerName)

# Display the winner!
if playerWins == True:
    winnerString = "*  " + playerName + " Wins!  *"
else:
    winnerString = "*  House Wins!  *"
    
starBorder = "*" * len(winnerString)
print(starBorder)
print(winnerString)
print(starBorder)
    
    

    
