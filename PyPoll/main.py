# Import Dependencies
import os
import csv

# Define csv path
election_csv = os.path.join("election_data.csv")

# Create variable to track the number of votes cast
vote_counter = 0

# Create lists to store data
election = {}

# Open csv
with open(election_csv, newline="") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header row
    next(csvreader)
    
    # Loop through csv
    for row in csvreader:
        vote_counter = vote_counter + 1
        if row[2] in election.keys():
            election[row[2]] = election[row[2]] + 1
        else:
            election[row[2]] = 1
        
# Create lists to store candidates and their corresponding vote counts
candidates = []
num_votes = []

# Dump the dictionary keys and values into individual lists
for key, value in election.items():
    candidates.append(key)
    num_votes.append(value)

# Create a list to store the voting percentages
vote_percent = []

# Calculate the percentage of each item relative to total votes
for votes in num_votes:
    vote_percent.append(round(votes/vote_counter * 100, 1))

# Zip the candidates, number of votes, and voting percentage into tuples
results = list(zip(candidates, num_votes, vote_percent))

# Create a list to store the winner of the election
winner_list = []

for item in results:
    if max(num_votes) == item[1]:
        winner_list.append(item[0])

# Turn the winner list into a string of the winner's name
winner = winner_list[0]

# Print election results to terminal
print(f'\nElection Results \n------------------------- \nTotal Votes: ' +str(vote_counter) + '\n-------------------------')
for item in results:
    print(item[0] + f': ' + str(item[2]) +'% (' + str(item[1]) + ')')
print(f'------------------------- \nWinner: '+ winner +'\n-------------------------')

# Print results to a text file
with open("PyPoll.txt", "w") as txtfile:
    txtfile.writelines(f'\nElection Results \n------------------------- \nTotal Votes: ' +str(vote_counter) + '\n-------------------------\n')
    for item in results:
        txtfile.writelines(item[0] + f': ' + str(item[2]) +'% (' + str(item[1]) + ')\n')
    txtfile.writelines(f'------------------------- \nWinner: '+ winner +'\n-------------------------')