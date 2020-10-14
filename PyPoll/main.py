import os
import csv

# Create a variable to hold total votes count
votes = 0 
# Create a list that will store 
candidate_list = []
# create a dictionary that will allow us to store the votes per candidate
candidate_votes = {}
# Create a path to read election data 
read_election_data = os.path.join("../PyPoll/Resources/election_data.csv")
# Assign the variable that will allow us to identify and highlight the winner
winner_votes = []


# Create a variable for our output file
analysis = "../PyPoll/analysis/election_results.csv"

with open(read_election_data,"r") as election_data:
    data_reader = csv.reader(election_data, delimiter=",")
    data_header = next(data_reader)
    
    # Create a Loop that will run to each row so we can identify candidates and assign votes
    for row in data_reader: 
    # Create a variable that identifies the candidate name in each row
        candidate_name = row[2]
    # Check if the current candidate is already in our candidate list
        if candidate_name not in candidate_list:
    # If the current candidate is not in the list, add it to the list
            candidate_list.append(candidate_name)
    # Sets a place for the new candidate in the candidate votes list on a zero counter   
            candidate_votes[candidate_name] = 0
    # Out of the 'If' statement assign a vote to the current candidate
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        votes = votes + 1
    # Creates a dictionary of values to hold only the votes of each candidate
    votes_count = candidate_votes.values()       
    # Identifies the maximum of all the candidate votes 
    winner_votes = max(votes_count) 
    
    # With this foor loop  we can run through the candidate votes dictionaty
    for candidate_name in candidate_votes: 
    # And through this if statement we identify the name of the candidate with higher votes
        if candidate_votes[candidate_name] == winner_votes:
            winner = candidate_name

    # Print the desired data
print(f"Election Results")
print(f"----------------------")
print(f"Total Votes: {votes} ")
print(f"----------------------")
    # Create a loop going through each name of the candidate list returning their votes and vote %
for candidate_name in candidate_votes:
    print( f"{candidate_name}:{round((candidate_votes[candidate_name]/(votes))*100,3)}% ({candidate_votes[candidate_name]})")
print(f"----------------------")
print(f"Winner:{winner}")
print(f"----------------------")

    # Print the text to the output file "election_analysis"
with open(analysis, 'w') as election_analysis:
    election_analysis.write(f"Election Results\n")
    election_analysis.write(f"----------------------\n")
    election_analysis.write(f"Total Votes: {votes} \n")
    election_analysis.write(f"----------------------\n")
    for candidate_name in candidate_votes:
        election_analysis.write( f"{candidate_name}:{round((candidate_votes[candidate_name]/(votes))*100,3)}% ({candidate_votes[candidate_name]})\n")
    election_analysis.write(f"----------------------\n")
    election_analysis.write(f"Winner:{winner}\n")
    election_analysis.write(f"----------------------\n")

