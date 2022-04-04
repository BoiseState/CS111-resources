#
# Project 2 - Allows user to play several types of games
#
# author:
#

# Import needed modules


# Copy and paste the definition of getCards here


# Copy and paste the definition of generateName here


# Copy and paste the definition of chance here


# Copy and paste the definition of war here




#################################################################
#################################################################
#################################################################
#
# Main
#
#################################################################
#################################################################
#################################################################

# Initalize color list with six different colors


# Initialize animal list with six different animals


# Welcome User to game


# Tell the user they need to choose a name

# Use generateName to get a name; store the name

# Tell the user what the name is 


# Set up initial hand of cards
# Tell the user they need cards

# Use getCards to get and store how many cards the user has to start

# Tell the user how many starting cards are in their hand


# Initialize a boolean called keepPlaying to True


# Print "Let's play!"


# Use a while loop
# loop while the user has cards left and keepPlaying is True


    # Print the menu options (as shown in the instructions)


    
    # Ask the user to enter a menu choice
    # Be sure to store the user's input
    # Use either upper() or lower() to ensure the if/elif/else below
    # works regardless of if the user enters a capital letter or a lowercase letter


    
    # Use if/elif/else to handle user choice
    # if the user enters w, print "WAR TIME" and call war
    # make sure to update the number of cards the user now has


    # else if the user enters c, print "Taking a Chance" and call chance
    # make sure to update the number of cards the user now has
    # Print how many total cards the user has now


    # else if the user enters n, print "NEW NAME!"
    # use random.shuffle to shuffle both the animal list and the color list
    # call generateName
    # be sure to store the new name
    # tell the user what the user's new name is


    # else if the user enters d, print "Dealing more cards ..."
    # call getCards, making sure to update the number of cards in the user's hand
    # Print how many cards the user now has


    # else if the user enters q, set keepPlaying to False

    # else
    # the user has entered an invalid menu option
    # print "That is an invalid menu option."


    # print a blank line
    # e.g. print()

    
# If the user has cards left, thank the user by name for playing

# Otherwise, inform the user they ran out of cards and the game is over
