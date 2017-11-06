#
# Author:  Luke Hindman
# Date: Mon Nov  6 16:13:43 MST 2017
# Description:  Example of how to read from a file with Exception Handling

#
#  Read lines of text from a specified file and create a list of those lines
#    with each line added as a separate String item in the list
#	
# Parameter
#   inputFile - A String with the name of a text file to convert to a Lit
#
# Return
#   A List containing each line from the text file
def getListFromFile (inputFile):
	outputList = []
	try:
		source = open(inputFile,"r")
		outputList =  source.readlines()
		source.close()
	except FileNotFoundError:
		print("Unable to open input file: " + inputFile)
		
	return outputList

# Create a string with the name of the file to read from
myFile = "names.txt"

# Call the above function to build a list of strings from the file
myDataList = getListFromFile(myFile)

# Print the list
#
# Notice that each item in the list include the newline character (\n)
# How can we modify the getListFromFile() function to strip the
#   newline character from each string in the list before returning
#   this list?
#
print (myDataList)