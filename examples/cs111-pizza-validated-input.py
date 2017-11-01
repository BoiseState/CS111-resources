# 
# Author:  Luke Hindman
# Date:  Wed Nov  1 07:57:23 MDT 2017
# Description:  Example of using while loop for user input validation
#


validResponse = False
pizzaForBreakfast = False

while validResponse == False:
    # Prompt the user for a response
    response = input("Would you like pizza for breakfast? (Yes/No): ")

    # Check if user entered a valid response
    if response.lower() == "yes":
        pizzaForBreakfast = True
        validResponse = True
    elif response.lower() == "no":
        validResponse = True
    else:
        print("Please enter either Yes or No")

# Display a message based upon
#   the user's selection
if pizzaForBreakfast == True:
    print("Yay!!!  We're having pizza for breakfast!")
else:
    print("No pizza this morning...  :(")
