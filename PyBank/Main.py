import os
import csv

#Path to csv data file
PyBank_file_path = os.path.join("Resources", "budget_data.csv")

# list for storing the columns in our output file

x = 0
Net_Total = 0
total_change = 0
greatest_inc = 0
greatest_dec = 0
greatest_inc_mth = ''
greatest_dec_mth = ''
month = []

# open input csv and read columns of interest into our lists
with open(PyBank_file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    
    for column in csvreader:
        month.append(column[0])
        
        x = x+1
        Net_Total = Net_Total + int(column[1])

        if x > 1:
            change = int(column[1]) - previous
            total_change = total_change + change
             
            if greatest_inc < change:
                greatest_inc = change
                greatest_inc_mth = x-1
 
            if greatest_dec > change:
                greatest_dec = change
                greatest_dec_mth = x-1
            
        previous = int(column[1])
    average_change = total_change/(x-1)
    average_change = round(average_change,2)

print("Financial Analysis")
print("----------------------------")
print(f"total months: {x}")
print(f"net total: ${Net_Total}")
print(f"average change: ${average_change}")
print(f"greatest_inc: {month[greatest_inc_mth]} (${greatest_inc})")
print(f"greatest_dec: {month[greatest_dec_mth]} (${greatest_dec})")

with open("PyBank.txt", "w", newline='') as final_csvfile:
    final_csvfile.write("Financial Analysis\n")
    final_csvfile.write("----------------------------\n")
    final_csvfile.write(f"Total Months: {x}\n")
    final_csvfile.write(f"Total: ${Net_Total}\n")
    final_csvfile.write(f"Average Change: ${average_change}\n")
    final_csvfile.write(f"Greatest Increase in Profits: {month[greatest_inc_mth]} (${greatest_inc})\n")
    final_csvfile.write(f"Greatest Decrease in Profits: {month[greatest_dec_mth]} (${greatest_dec})\n")
