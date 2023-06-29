#Modules
import os
import csv

# Set path for file
csv_path = os.path.join('.', 'Resources', 'election_data.csv')

# Open the CSV
with open(csv_path, 'r') as csvfile:
    election_file = csv.reader(csvfile, delimiter=",")
    header = next(election_file)

    #Create empty lists and variables
    total_votes = 0
    votes = []
    candidates= []
    candidate_votes = []
    percent_votes = []

    #Print the first two rows (in this piece of code, I have printed the results along with the code)
    print("Election Results")
    print("------------------------------------------------------------------------------------------------------------")

    #Calculate total_votes & create a list (votes) containg the value of all the votes casted
    for row in election_file:
        total_votes += 1
        votes.append(row[2])

    #Print the total_votes
    print(f"Total Votes: {total_votes}")
    print("------------------------------------------------------------------------------------------------------------")

    #Find all the unique candidates and fill their names in a list ('candidates')
    name = votes[0]
    candidates.append(votes[0])
    for x in range(total_votes):
        if name != votes[x] and votes[x] not in candidates:
            name=votes[x]                
            candidates.append(name)
        else:
            name=name

    #Create a function to count the votes for each candidate, update respective lists and print the results
    def count(name):
        total = 0
        for i in range (total_votes):
            if name == votes[i]:
                total += 1
            else:
                total=total
        candidate_votes.append(total)
        per_votes = round(((total/total_votes)*100),3)
        percent_votes.append(per_votes)
        
        print(f"{candidates[v]} : {percent_votes[v]}% ({candidate_votes[v]})")
        
    #Call the function, to perform the same task on all the listed candidates
    for v in range(len(candidates)):
        name=candidates[v]
        count(name)

    #Once the votes are counted for each candidate, find the maximum votes, find the index for the maximum vote and corresponding candidate
    max_votes= max(candidate_votes)        
    max_vote_index = candidate_votes.index(max_votes)

    #Print out the winner
    print("---------------------------------------------------------------")
    print(f"Winner: {candidates[max_vote_index]}")
   
#create a text file named 'PyBank_analysis.txt' to store the result of analysis. '/n' is used to add the line in the text file
output_file = os.path.join('.', 'Analysis', 'PyPoll_analysis.txt')
with open(output_file,"w") as result_file:
    result_file.write("Election Results\n\n")
    result_file.write("----------------------------------------------------------\n\n")
    result_file.write(f"Total Votes: {total_votes}\n\n")
    result_file.write("----------------------------------------------------------\n\n")
    for v in range(len(candidates)):
       result_file.write(f"{candidates[v]} : {percent_votes[v]}% ({candidate_votes[v]})\n") 
       result_file.write("\n")
    result_file.write("----------------------------------------------------------\n\n")
    result_file.write(f"Winner: {candidates[max_vote_index]}\n\n")
    result_file.write("----------------------------------------------------------\n\n")
  