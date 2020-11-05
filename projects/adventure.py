# Author:  
# Date:  
# Description:  Retro Arcade - Component Three - Choose your own adventure

# Step 1: Import required libraries
import random

def create_adventure(name):
    """
    This is a choose your own adventure game.
    Create a story where you prompt the user for options that change the story.
    You should have many different paths through your story, but try to avoid going 
    too far as it becomes difficult to manage.
    """
    print(f"Welcome to choose your own adventure {name}") 
if __name__ == "__main__":            
    # Setup a default player
    player_name = "Bob"

    # Call the function to create a Madlib
    create_adventure(player_name)
    
    

    
