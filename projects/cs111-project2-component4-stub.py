# Author:  
# Date:  
# Description:  Retro Arcade - Component Four - Selection Menu

# Step 1: Import required libraries
import random

# Step 2:  Copy the playGameOfDice() function from Component 1 and paste it here


# Step 3:  Copy the playGameOfSlots() function from Component 2 and paste it here


# Step 4:  Copy both the generateMadlib() and createMadlib() functions from Component 3 and paste them here


#
# Display the winner for the current game
#
# Parameter
#  name - The name of the winner
#
def displayWinner(name):
    # Display the winner!
    winnerString = "*  " + name + " Wins!  *"
    starBorder = "*" * len(winnerString)
    print(starBorder)
    print(winnerString)
    print(starBorder)


#
# Primary Game Loop and Selection Menu
#
# The selection menu will be the core component that ties all three individual games
#   into a single program.  It contains the primary game loop that will continue
#   running until the player either selects (Q)uit from the selection menu or the
#   player runs out of credits.  Selection menu contains options for (D)ice, (S)lots,
#   and (M)adlib.  When the player selects either (D)ice or (S)lots, 10 credits are 
#   deducted from the player's balance.  When the player selects (M)adlib, 20 credits 
#   are added to the player's balance.  The player begins with 100 credits.  


# Step 5:  Declare an integer variable named balance and set the initial value to 100


# Step 6:  Prompt the player for their name


# Step 7:  Print a message welcoming the player by name to Retro Arcade. 


# Step 8:  Setup the Game Loop so that the game will continue running while the 
#    player's balance is > 0 and they have not selected to quit the game.


    # Step 8.1:  Display Game Menu


    # Step 8.2 : Display the player's balance


    # Step 8.3:  Prompt user for selection and validate input


    # Step 8.4:  Use if and elif statements to run a particular game based upon the 
    #    player's selection from the menu and add or subtract the appropriate amount 
    #    of credits from the players balance.  For the Dice and Slots games, check the
    #    return value and if the player wins (return value == True), use the provided 
    #    displayWinner() function to print the player's name.  If the computer wins
    #    (return value == False), use the displayerWinner() function to print "Computer".
    #    End the game if the user selects (Q)uit

   

# Step 9: Game Over. Print a nice message thanking the user for playing.





    
    

    
