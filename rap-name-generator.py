# Guided Exploration No. 3
# Raymond Phillips

# Import the random library
import random

# Declare an empty list
possible_names = []

# Open and write to the rap-names-output.txt file
outputFile = open('rap-names-output.txt', 'w')

# Open rap-names.txt as a dataFile
with open('rap-names.txt', 'r') as dataFile:
    # Iterate through each line in rap-names.txt
    for name in dataFile:
        # Append name to the possible_names list
        possible_names.append(name.rstrip())

# Ask the user for the number of rap names to generate
count = int(input('How many rap names would you like to create? '))
# Ask the user for the number of parts within a rap name
parts = int(input('How many parts should the name contain? '))

# Iterate for the number of rap names the user input
for i in range(count):
    # Declare an empty list
    name_parts = []
    # Iterate for the number of parts the user input
    for j in range(parts):
        # Get a name and append to the name_parts list
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])

    # Write generated names to output file
    outputFile.write(f"{' '.join(name_parts)}\n")
    # Print out the generated rap name in terminal
    print(f"{' '.join(name_parts)}")

# Close the output file
outputFile.close()
