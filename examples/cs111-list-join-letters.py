#
# Author:  Luke Hindman
# Date:  Wed Nov  1 10:52:49 MDT 2017
# Description:  Inclass example on joining Lists to form Strings
#

# Declare list of temperatures as float values
letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Use the join() function to create a string with
#   each letter separated by " - "
output = " - ".join(letterList)

# Display the list
print(output)
