# Author:  
# Date:  
# Description:  Jackpot Challenge - Component Three - Blackjack

# Step 1: Import required libraries

#
# This game is player vs house where they play a single hand of blackjack.
#   The player and the house both draw two cards with values in the range
#   1 - 11.  The player then has the option to draw additional cards (hit)
#   or stick with was was drawn (stand).  If the player exceeds 21 points
#   (busts), the house wins.  After the player is done playing, the house
#   will hit if the value of its hand is less than 17, otherwise it will
#   stand.  If the house busts, the player wins.  The player closest to 21
#   points without going over, wins.  If the player and the house have the
#   same number of points in their hand, the house wins.  
#
# Parameters
#   name - Name of the current player
#
# Returns
#   True - Player Wins
#   False - Player Loses
def playGameOfBlackjack(name):
    
    # Step 2: The game should begin by displaying a welcome message including the
    #    name of the game (Blackjack) and the players name.

    # Step 3: Declare two integer variables to track the number of points in 
    #    the player's hand and the dealer's hand respectively.
    #    What should the initial values be?

    # Step 4:  Use randint() function to "draw" two cards for player's hand 


    # Step 5:  Use randint() function to "draw" two cards for dealer's hand 


    # Step 6:  Use a while loop that will prompt the player to draw an additional
    #    card or stand.  The loop ends when the player stands or if the points
    #    in the player's hand exceeds 21 (busts).

        # Step 6.1:  Print the current point value of the players hand


        # Step 6.2:  Use a while loop to prompt the player to Please (H)it or (S)tand 
        #    and validate input.  If the player chooses to draw a card, use the 
        #    random() function to "draw" a card and add the points to the player's hand.

            
        # Step 6.3:  Check if the points in the player's hand exceeds 21 points.
        #    If player busts, print player loses message and return False


    # Step 7:  Use a while loop that will check the point total in the dealer's hand.
    #    If the points in the dealer's hand are less than 17, the dealer must draw an additional
    #    card.  If the dealer has 17 or more points, the dealer stands.  The loop ends when the 
    #    dealer stands or if the points in the dealer's hand exceeds 21 (busts).

        # Step 7.1:  Print the current point value of the dealers hand


        # Step 7.2:  If current point value in hand is < 17, 
        #   randomly generate an integer value for the houses draw.
        #   Otherwise, the dealer stands.

            
        # Step 7.3:  If dealer busts, print dealer loses message and return True


    # Step 8:  Compare the player's and dealer's hands, if player's hand is > houses hand and <= 21
    #    print winner message, including name and return True.  Otherwise, print player loses and return False                 

  

######################################################################
# The code below this comment is what runs the program.  Please      #
#   take the time to look at how your function is being called and   #
#   what is being done with the return value, but you do not need    #
#   to modify this code to complete the component.                   #
######################################################################           
        
# Setup a default player
playerName = "Bob"

# Call the function and store the result
playerWins = playGameOfBlackjack(playerName)

# Display the winner!
if playerWins == True:
    winnerString = "*  " + playerName + " Wins!  *"
else:
    winnerString = "*  House Wins!  *"
    
starBorder = "*" * len(winnerString)
print(starBorder)
print(winnerString)
print(starBorder)
    
    

    
