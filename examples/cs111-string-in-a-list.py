#
# Author:  Luke Hindman
# Date:  Wed Nov  1 10:52:49 MDT 2017
# Description:  Inclass example of testing whether
#    a List contains a string
#

# Prompt the user for favorite pizza toppings
shoppingList = ["milk", "eggs", "bread", "squash", "cookies", "salad"]

item = input("Enter item for shopping list: ")

if item.lower() in shoppingList:
    print("Already on the list!")
else:
    print("I can't believe I for got that!")
    shoppingList.append(item.lower())

print(shoppingList)
             
             
