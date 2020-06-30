#Import required modules
import os
import csv

#Path to csv data file
PyPoll_file_path = os.path.join("..", "Resources", "election_data.csv")

#Declaring global variables
candidates = []
unique_candidate = set()
winner = ()

#Open input csv and read columns of interest into our lists
with open(PyPoll_file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
                    
    #Determine unique candidates
    for columns in csvreader:
        candidates.append(columns[2])
        unique_candidate.add(columns[2])
                
    #Determine total number of votes
    vote_total = len(candidates)
    
def details():
    #for candidate in candidates:
    max_vote_count=0
    for x in unique_candidate:
        count = candidates.count(x)
        vote_percentage = (count/vote_total)*100
        rounded_percentage= "{:.3f}".format(vote_percentage)
        if(max_vote_count<count):
            max_vote_count=count
            winner = str(x)
        print(f"{x}: {rounded_percentage}% ({count})")
    return winner

print("Election Results")
print("----------------------------")
print(f"Total Votes: {vote_total}")
print("----------------------------")
winner=details()
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

with open("PyPoll.txt", "w", newline='') as final_csvfile:
    final_csvfile.write("Election Results\n")
    final_csvfile.write("----------------------------\n")
    final_csvfile.write(f"Total Votes: {vote_total}\n")
    final_csvfile.write("----------------------------\n")
    final_csvfile.write(f"{details}\n")
    final_csvfile.write("----------------------------\n")
    final_csvfile.write(f"Winner: {winner}\n")
    final_csvfile.write("----------------------------\n")