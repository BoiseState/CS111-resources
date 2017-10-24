# Author:  Luke Hindman
# Date: Tue Oct 24 12:32:09 MDT 2017
# Description:  In class example for Lists

# Load the random module
import random

# List of patients for family counselling
patientList = ["Darth Vader", "Luke Skywalker", "Han Solo", "Leia Organa", "Jyn Erso", "Kylo Ren"]

# Randomly select the next person to talk to the group
patient = random.choice(patientList)

print(patient + ", this is a safe space.  Is there anything you would like to share with the group?")

