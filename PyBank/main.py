# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#List
Profit_loss=[]
totalamount = 0
totalmonth = 0
diff_percent = 0

csvpath = 'PyBank/Resources/budget_data.csv'

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

     # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

     # Read each row of data after the header
    
    for row in csvreader:
        #print(row)
        
        totalamount = totalamount + int(row[1])
        totalmonth = totalmonth + 1

    print (totalamount)
    print (totalmonth)



