# Overview of what this code intends to accomplish

## The following information will be retrieved

# a) Total number of votes cast
# b) A complete list of candidates who received votes
# c) Total number of votes each candidate received
# d) Percentage of votes each candidate won
# e) The winner of the election based on popular vote

## In order to accomplish this, the following steps will take place

# 1. Open the data file.
# 2. Write down the names of all the candidates.
# 3. Add a vote count for each candidate.
# 4. Get the total votes for each candidate.
# 5. Get the total votes cast for the election.

## The data we need to retrieve
# 1. Total # of votes cast
# 2. Complete list of candidates that recieved votes
# 3. Percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    for row in file_reader:
        print(row)



# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

# Filename variable to save to file
# file_to_save=os.path.join("analysis","election_analysis.txt")

# Use open() function in "w" mode to write data
open(file_to_save,"w")

# Write some data to the file
outfile = open(file_to_save, "w")

# Write some data to the file
outfile.write('Hello World')

# Close the file
outfile.close()

file_to_save = os.path.join("analysis","election_analysis.txt")

# Use with statement to open text file

with open(file_to_save,"w") as txt_file:

     # Write data to the file
     # txt_file.write("Hello World")

     # txt_file.write("Arapahoe")
     # txt_file.write("Denver")
     # txt_file.write("Jefferson")

     txt_file.write("Counties in the Election\n______________________\nArapahoe\nDenver\nJefferson")
