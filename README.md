# Election Analysis with Python and VScode
## Overview of Election Audit
The purpose of the election audit is to determine the election winner for a local Congressional race in Colorado. To do so, we will analyze and process a set of voting data, which contains voter counts across multiple counties in Colorado. To do so, we will be implementing Python within the vscode processer to do things such as, read and extract data from a file, use structures such as for loops and if statements to sort and understand the data and write the data to the terminal and a text file. 

__Figure 1: Python notebook__
## Election Audit Results
### Observations
The following election outcomes were assessed by our python code:
- The total number of votes cast in this congressional election was 369,711. This number will be used to scale our outcomes to determine what percentage of votes each candidate recieved and percentage by county
- The largest mumber of votes belonged to Denver county by far, which aligns with the population density of these three respective counties. 
- A breakdown of the outcome is provided in the text file. To summarize, the mumber of votes shows that one candidate, Diana Degette (D), won by a landslide 74 percent. The second place candidate was Charles Casper Stockham (R) at 23 percent and Raymon Anthony Doane (L) at 3 percent. The votes per county added up to denver county having 83 percent of the total votes, followed by Jefferson county (11 percent) and Arapahoe (7 percent).
- Diana Degette was the clear winner.

__Figure 2: Election Results__
### Summary 
In summary, the code provided is complete and able to be adapted to other types of data, for example, in different counties, or for looking at more counties at a time. Two examples of how the script could be modifed would be to include a demographic category (such as age group of the voter) in the analysis by adding a seperate entry in the dictionary, and also looking at voter outcomes over several election years by introducing nested for loops.
