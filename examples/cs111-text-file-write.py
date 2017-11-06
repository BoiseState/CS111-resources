#
# Author:  Luke Hindman
# Date: Mon Nov  6 16:13:43 MST 2017
# Description:  Example of how to write to a file with Exception Handling


#
# Write a List of strings to a file
#
# Parameter
#   outputFile - A String with the name of the file to write to
#   dataList - A List of strings to write to the file
#
# Return 
#    none
#
def writeListToFile(outputFile, dataList):
	try:
		destination = open(outputFile,"w")
		destination.writelines(dataList)
		destination.close()
	except IOError:
		print("Unable to write to output file" + outputFile)

# Create a string with the name of the file to write to
myFile = "names.txt"

# List of Strings to write to file, to ensure write the values to separate lines
#   in the files, each string must include a newline.  
#
# How can we modify the writeListToFile() function to do this for us automatically?
#
# nameList = ["Robin", "Lily", "Nora", "Patrice", "Zoey", "Quinn","Ted", "Marshall", "Barney", "Ranjit", "Carl", "Linus"]
nameList = ["Robin\n", "Lily\n", "Nora\n", "Patrice\n", "Zoey\n", "Quinn\n","Ted\n", "Marshall\n", "Barney\n", "Ranjit\n", "Carl\n", "Linus\n"]

# Call the above function to build a list of strings from the file
writeListToFile(myFile,nameList)

