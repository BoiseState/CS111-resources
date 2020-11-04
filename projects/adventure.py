# Author:  
# Date:  
# Description:  Retro Arcade - Component Three - Madlib Game

# Step 1: Import required libraries
import random

# Step 2: Copy your generateMadlib() function from Madlib MiniTask and past it here
def create_adventure(name):
    """
    This is a choose your own adventure game.
    Create a story where you prompt the user for options that change the story.
    You should have many different paths through your story, but try to avoid going 
    too far as it becomes difficult to manage.
    """
    print(f"Welcome to choose your own adventure {name}") 
    # Step 3: The game should begin by displaying a welcome message including the
    #    name of the game (Madlib) and the players name.


    # Step 4: Prompt the player to Press Enter to generate the Madlib


    # Step 5: Call the generateMadlib() function and store the result to a variable


    # Step 6: Print the generated Madlib



######################################################################
# The code below this comment is what runs the program.  Please      #
#   take the time to look at how your function is being called and   #
#   what is being done with the return value, but you do not need    #
#   to modify this code to complete the component.                   #
######################################################################             
if __name__ == "__main__":            
    # Setup a default player
    player_name = "Bob"

    # Call the function to create a Madlib
    create_adventure(player_name)
    
    

    
