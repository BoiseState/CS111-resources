#
# Author: 
# Date:  
# Description:  

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
# Component Four - Implement printCatalogStats() function here
#

#
# Component Three - Implement findSongs() function here
#

#
# Component Two - Implement printSong() function here
#

#
# Component One - Implement the printMenu() function here
#

#
# Component One - Main program loop begins here
#










#
# Component One - Program ends here
#
print("Leaving Jukebox Hero...  Goodbye!")


