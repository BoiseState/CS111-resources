#
# Author:  Luke Hindman
# Date:  Mon Apr  3 17:10:25 MDT 2017
# Description:  This is an implementation of the MASH game.  Random selections
#   are made from Lists based upon the following categories:
#
#   M.A.S.H. (mansion, apartment, shack, house)
#   Who they'll marry
#   What their job is
#   Their means of transportation
#   Number of kids they'll have
#   Where they'll live
#   What their income is
#   The pet(s) they'll have
#
#   The random selections are used to predict the future of the player
#

import random

#
# Define CONSTANTS to hold the lists for each category
#
HOME_LIST = ["mansion", "apartment", "shack", "house"]
FEMALE_SPOUSE_LIST = ["Robin", "Lily", "Nora", "Patrice", "Zoey", "Quinn"]
MALE_SPOUSE_LIST = ["Ted", "Marshall", "Barney", "Ranjit", "Carl", "Linus"]
OCCUPATION_LIST = ["teacher", "architect", "lawyer", "newcaster", "undercover agent"]
TRANSPORTATION_LIST = ["walk", "ride the train", "ride a bus", "fly an airplane", "carpool"]
HOMETOWN_LIST = ["Cleveland", "Queens", "The Bronx", "Brooklyn", "Manhattan", "Staten Island"]


# This function will randomly select items from each category List
#   and use them to predict the player's future.
# Parameters:
#  playerName - A String containing the name of the player
#  spouseGender = A String containing either "MALE" or "FEMALE".
#
# Return
#  A String containing the player's future
#
def getFuture(playerName,spouseGender):

    # Randomly select items from list
    firstHome = random.choice(HOME_LIST)
    secondHome = random.choice(HOME_LIST)
    
    if (spouseGender == "female"):
        spouse = random.choice(FEMALE_SPOUSE_LIST)
    else:
        spouse = random.choice(MALE_SPOUSE_LIST)

    occupation = random.choice(OCCUPATION_LIST)
    transportation = random.choice(TRANSPORTATION_LIST)
    hometown = random.choice(HOMETOWN_LIST)

    # Randomly generate interger values for remaining future elements
    yearsOfMarriage = random.randint(3,8)
    numberOfKids = random.randint(0,7)
    numberOfCats = random.randint(0,18)
    numberOfDogs = random.randint(0,8)

    # Build a string containing the script of the player's future
    output = ""
    output += playerName + ", this is your future... "
    output += "You will marry " + spouse + " and live in a " + firstHome + ". "
    output += "After " + str(yearsOfMarriage) + " years of marriage, you will finally get your dream job of being a " + occupation + ". "
    output += "Your family will move to a " + secondHome + " in " + hometown + " where you will " + transportation + " to work each day. "
    output += "You and " + spouse + " will have " + str(numberOfKids) + " kids, " + str(numberOfCats) + " cats, and " + str(numberOfDogs)
    output += " dogs and will live happily ever after in " + hometown + "."

    # Return the string containing the player's future
    return output

# Primary Game Loop
playAgain = True
while playAgain == True:
    #
    # Prompt user for name
    #
    name = input("Please enter your name: ")

    #
    # Prompt user for gender of spouse
    #
    preferredGenderOfSpouse = input("Please enter the preferred gender of your spouse (male/female): ")
    

    # Sanitize user input by converting to lowercase.
    preferredGenderOfSpouse = preferredGenderOfSpouse.lower()

    #
    # Display Game Title Screen
    #
    print("M.A.S.H.")

    #
    # Generate the player's future
    #
    future = getFuture(name,preferredGenderOfSpouse)

    #
    # Display the player's future
    #
    print(future)

    #
    # Play it again?
    #
    playAgain = False
    response = input("Play again (Y/N): ")
    if response.lower() == "y":
        playAgain = True
    

#
# Game Over
#
print("Game Over...")

