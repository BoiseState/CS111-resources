# Author:  
# Date:  
# Description:  Retro Arcade - Component One - Dice Game


# Step 1. Import required libraries


#
# This game is player vs computer where each take turns rolling a single six-sided
#    die.  The player with the highest roll each round wins a point.  The computer
#    receives the point for a tie.  The first player to 5 points wins.
#
# Parameters
#   name - Name of the current player
#
# Returns
#   True - Player Wins
#   False - Player Loses
def play_dice_game(name):
    print(f"Welcome to the dice game {name}") 
    return False
    # Step 2. The game should begin by displaying a welcome message including the
    #    name of the game (Dice) and the players name.


    # Step 3. The game should have a variable for tracking the player's score
    #    and a variable for tracking the computer's score and both should
    #    be initialized to zero.

    
    # Step 4. The game will continue while the player's score is less than 5
    #    and the computer's score is less than 5.

        
        # Step 5. Display the current scores

        
        # Step 6. Prompt the player to Press Enter to roll


        # Step 7. Randomly generate integer value for players roll


        # Step 8. Randomly generate integer value for computers roll


        # Step 9. Compare results, print winner message, including name
        #    and increment the score of the winner


    # Step 10. If the player score is greater than the computer score, the player Wins so return True.
    #     Otherwise, return false.

          

######################################################################
# The code below this comment is what runs the program.  Please      #
#   take the time to look at how your function is being called and   #
#   what is being done with the return value, but you do not need    #
#   to modify this code to complete the component.                   #
######################################################################
if __name__ == "__main__":
    # Setup a default player
    player_name = "Bob"

    # Call the function and store the result
    player_won = play_dice_game(player_name)

    # Display the winner!
    if player_won:
        winner_message = f"*  {player_name}  Wins!  *"
    else:
        winner_message = "*  computer Wins!  *"
        
    star_border = "*" * len(winner_message)
    print(star_border)
    print(winner_message)
    print(star_border)
    
    

    
 