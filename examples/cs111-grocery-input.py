# Author:  Luke Hindman
# Date:  Tue Oct 24 13:10:06 MDT 2017
# Description:  In-class example for user input and lists

# Create an empty grocery list
groceryList = []

# Prompt the user for an item to add to the list
item = input("Please enter an item: ")

# Add the item to the list
groceryList.append(item)

# Print the grocery list
for g in groceryList:
    print ("Don't forget the " + g + "!")

