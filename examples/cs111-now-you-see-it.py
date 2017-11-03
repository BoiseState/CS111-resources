#
# Author:  Luke Hindman
# Date: Fri Nov  3 15:30:23 MDT 2017
# Description:  Test out printing backspace character to erase a line of text

import sys
import time

#
# Write a message directly to the console one character
#   at a time. The time between characters is set with
#   the waitTime specified in decimal seconds. Once the 
#   message has been printed, it is deleted one character
#   at a time by moving the cursor backward, overwriting
#   the character at that position with a space, and then
#   moving the cursor backward again ('\b \b').
#
# Parameters
#   message - String containing message to be written to the console
#   waitTime - Decimal time in seconds to wait between characters
#
# Return 
#   none
def printVanishingMessage(message, waitTime):
    for i in range(0,len(message)):
        sys.stdout.write(message[i])
        sys.stdout.flush()
        time.sleep(waitTime)

    for i in range(0,len(message)):
        sys.stdout.write('\b \b')
        sys.stdout.flush()
        time.sleep(waitTime)


# Run it once
printVanishingMessage("Hello World", 0.1)
# Move to the next line
print()


# Run it in an infinite loop
while True: 
    printVanishingMessage("Hello World",0.1)
