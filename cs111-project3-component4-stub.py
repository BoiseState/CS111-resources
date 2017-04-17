# Author:  
# Date:  
# Description:  Jackpot Challenge - Component Four - Selection Menu

# Step 1: Import required libraries

# Step 2:  Copy the playGameOfDice() function from Component 1 and paste it here

# Step 3:  Copy the playGameOfSlots() function from Component 2 and paste it here

# Step 4:  Copy the playGameOfBlackjack() function from Component 3 and paste it here


#
# Prompt the user for a bet
#
# Parameter
#    maxBet - the max bet allowed
#
# Returns
#    An integer value containing the bet amount
def getBetFromUser(maxBet):
    validResponse = False
    bet = 0
    while validResponse == False:
        response = raw_input("Please enter your bet up to $" + str(maxBet) + ": ")
        if response.isdigit() and int(response) <= maxBet:
            validResponse = True
            bet = int(response)
        else:
            print("Please enter a valid bet")
    return bet


#
# Display the winner for the current game
#
# Parameter
#  winnerName - The name of the winner
#
def displayWinner(winnerName):
    # Display the winner!
    winnerString = "*  " + winnerName + " Wins!  *"
    starBorder = "*" * len(winnerString)
    print(starBorder)
    print(winnerString)
    print(starBorder)


#
# Primary Game Loop and Selection Menu
#
# The selection menu will be core component that ties all three individual games
#   into a single program.  It contains the primary game loop that will continue
#   running until the player either selects (Q)uit from the selection menu or the
#   player runs out of money.  Selection menu contains options for (D)ice, (S)lots,
#   and (B)lackjack.  When the player selects a game, this component will prompt
#   them for the bet amount and will add or subtract that amount from the their
#   balance depending upon whether they win or lose.  The player begins with $100.  


# Step 5:  Declare an integer variable called balance and set the initial value to 100


# Step 6:  Prompt the player for their name


# Step 7:  Print a message welcoming the player by name to Jackpot Challenge. 
#    It should also display their current balance.


# Step 8:  Setup the Game Loop so that the game will continue running while the 
#    player's balance is > 0 and they have not selected to quit the game.


    # Step 8.1:  Display Game Menu


    # Step 8.2:  Prompt user for selection and validate input


    # Step 8.3:  Use if and elif statements to run a particular game based upon the 
    #    player's selection from the menu.  Call the provided getBetFromUser() function
    #    before starting each game and store the bet amount to a variable.  If the
    #    player winds the game, add the bet amount to their balance.  If the player
    #    looses the game, deduct the amount from their balance.  End the game if the 
    #    user selects (Q)uit

   
#
# Step 9: Game Over.  To reach this point in the game, either the player has run
#    out of money (balance == 0), or the player has selected quit from the menu.
#    Display three different messages to the user depening upon their remaining 
#    balance.  These messages should find ways to provided a supportive message
#    to the player.
# 
#    balance > 100:  - Display Message 1
#    balance > 0 and balance <= 100 = Display Message 2
#    balance <= 0  - Display Message 3.
#



    
    

    
