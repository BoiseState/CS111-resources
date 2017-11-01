#
# Author:  Luke Hindman
# Date:  Wed Nov  1 10:52:49 MDT 2017
# Description:  Inclass example on joining Lists to form Strings
#

# Declare list of temperatures as float values
highTempList = [78.5,82.3,79.3,90.2,83.4]

# Convert list of float values to a list of string values
highTempStringList = []
for temp in highTempList:
    highTempStringList.append(str(temp))

# Display the list of String values
print(highTempStringList)

# Use the join() function to create a string to high temp values,
#    delimited by "->"
output = " -> ".join(highTempStringList)

# Display the list
print(output)
