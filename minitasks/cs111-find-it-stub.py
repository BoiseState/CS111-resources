# 
# Author:
# Date:
# Description:
#

#
#  Read lines of text from a specified file and create a list of those lines
#    with each line added as a separate String item in the list
#	
# Parameter
#   inputfile - A String with the name of a text file to convert to a Lit
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

#
# Use the getListFromFile() function to open the song data file
# and store the return value to songList
#


#
# Use a for loop, the in operator and the printSong() function 
#   to print each song in the songList that contains the word "cheese"
#

