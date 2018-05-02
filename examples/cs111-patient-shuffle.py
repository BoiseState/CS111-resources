# Author:  Luke Hindman
# Date: Tue Oct 24 12:32:09 MDT 2017
# Description:  In class example for Lists

# Load the random module
import random

# List of patients for family counselling
patientList = ["Darth Vader", "Luke Skywalker", "Han Solo", "Leia Organa", "Jyn Erso", "Kylo Ren"]

# Shuffle the patient list
random.shuffle(patientList)

# Print the speaking order
print("Patients will speak in the following order:")
for patient in patientList:
    print("  - " + patient)
