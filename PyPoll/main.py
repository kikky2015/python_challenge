import os
import csv

#Path to collect data from the Resources folder
election_csv = os.path.join("Resources", "election_data.csv")

#initializing variables
all_votes=0
count=0
candidates={}
winner_votes=0

#open csv file
with open(election_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

 # Read the header row first 
    csv_header = next(csvreader)
   
    for row in csvreader:
        all_votes += 1
       
        candidate = row[2]
        if candidate in candidates:
           candidates[candidate] += 1
        else:
            candidates[candidate] = 1
        
        
# Calculate and print the results for each candidate
for candidate, votes in candidates.items():
    percentage = (votes / all_votes) * 100
    candidates[candidate] = { "votes": votes, "percentage": percentage }
       
    # Track the winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

#print to terminal
print ()
print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {all_votes}")
print("-------------------------------------")
for candidate, data in candidates.items():
    votes = data["votes"]
    percentage = data["percentage"]
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------------------")
print(f"Winner: {winner}")
print("------------------------------------")

#Specifying the folder path and file name for the results
folder_path = "C:\\Users\\HP\\Desktop\\Lessons_BootCamp\\wk3\\HW3\\python_challenge\\PyPoll\\Analysis"
file_name = "election_results.txt"
full_path = os.path.join(folder_path, file_name)

# Print results analysis to file
with open(full_path, 'w') as file:
            
        file.write("Election Results\n")
        file.write("-------------------------------------\n")
        file.write(f"Total Votes: {all_votes}\n")
        file.write("-------------------------------------\n")
        for candidate, data in candidates.items():
            votes = data["votes"]
            percentage = data["percentage"]
            file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        file.write("-------------------------------------\n")
        file.write(f"Winner: {winner}\n")
        file.write("-------------------------------------\n")