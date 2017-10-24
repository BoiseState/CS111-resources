# Author:  Luke Hindman
# Date:  Tue Oct 24 13:10:06 MDT 2017
# Description:  In-class example for user input and lists

# Create an empty grocery list
groceryList = []

# Shopping list loop
done = False
while done == False:
    # Prompt the user for an item to add to the list
    item = input("Please enter an item or done when finished: ")

    # Check if user is done entering items,
    # otherwise add the item to the grocery list
    if item.lower() == "done":
        done = True
    else:        
        groceryList.append(item)

# Print the grocery list
for g in groceryList:
    print ("Don't forget the " + g + "!")

