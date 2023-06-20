import os
import csv

#Path to collect data from the Resources folder
#budget_csv = open('C:\Users\HP\Desktop\Lessons_BootCamp\wk3\HW3\python_challenge\PyBank\Resources\budget_data.csv')
budget_csv = os.path.join("Resources", "budget_data.csv")

#initializing
total_months=0
net_profits=0
old_profit_loss=0
change=[]
dates=[]


with open(budget_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

 # Read the header row first 
    csv_header = next(csvreader)

        # Read each row of data after the header
    for row in csvreader:
        
    # Increment the total number of months for each row
        total_months += 1      

    # Net profits
        net_profits =net_profits + int(row[1])
    
        # Monitor the changes in Profit/Losses
        if total_months > 1:
            change.append(int(row[1]) - old_profit_loss)
       
        # Update the old Profit/Loss value
        old_profit_loss = int(row[1])

        # Track the dates
        dates.append(row[0])    

# Average change in Profit/Losses
average_change = sum(change) / len(change)

# Greatest increase and decrease in Profit/Losses
greatest_increase = max(change)
greatest_decrease = min(change)

#To assign dates
greatest_increase_date = dates[change.index(greatest_increase)+1]
greatest_decrease_date = dates[change.index(greatest_decrease)+1]

#Specifying the folder path and file name for the results
folder_path = "C:\\Users\\HP\\Desktop\\Lessons_BootCamp\\wk3\\HW3\\python_challenge\\PyBank\\Analysis"
file_name = "bank_data.txt"
full_path = os.path.join(folder_path, file_name)

# Print results analysis to file
with open(full_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_profits}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")