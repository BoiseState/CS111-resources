#
# Author:  Luke Hindman
# Date:  Wed Nov  1 10:52:49 MDT 2017
# Description:  Inclass example of testing whether
#    a string contains another string
#

# Prompt the user for favorite pizza toppings
favoriteToppings = input("Please enter your favorite pizza toppings: ")

if "anchovies" in favoriteToppings.lower():
    print("Yuck! How can you possibly eat anchovies on your pizza?")
elif "olives" in favoriteToppings.lower():
    print("Olives are delicious!")
else:
    print("Sounds good to me!")

