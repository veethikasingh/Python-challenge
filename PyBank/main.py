# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
#Variables
#List
Profit_loss=[]
Total_amt=[]
avg_amt=[]
totalamount = 0
totalmonth = 0
diff_amount = 0
avg_amount = 0
prev_amount = 0
rowcount = 0
avg_change = 0
max_change = 0
min_change = 0


csvpath = 'Resources/budget_data.csv'
outfile = 'Analysis/financial_analysis.txt'

#read file

with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
     csvreader = csv.reader(csvfile, delimiter=',')

     #print(csvreader)
    # Read the header row first (skip this step if there is no header)
     csv_header = next(csvreader)
    
     # Read each row of data after the header
    
     for row in csvreader:
   
       #total amount is added for the 2nd column to the variable totalamount
       #total month is a rowcount 
        totalamount = totalamount + int(row[1])
        totalmonth = totalmonth + 1
        # diff between curent value and previous value
        diff_amount = 0
        diff_amount = int(row[1]) - prev_amount
        # store current value for next row
        
        # append to 3 lists 
        # Profit Loss contains all the calculated rows
        # Total amount is for the numbers only to get max and minimum
        # avg amt  is to remove the first row as that remains unchanged for avg
        Profit_loss.append([row[0],diff_amount])
        Total_amt.append(diff_amount)
        avg_amt.append(diff_amount)
        #Store current calue for next iteration
        prev_amount = int(row[1])
        
        
    # Output totals
     print ("Financial Analysis")
     print ("Total Month :",totalmonth)
     print ("Total $:",totalamount)
     #print (Profit_loss)  
    # Sort this to get maxx and min value ascending
     Total_amt.sort()  
     #print (Total_amt)
    # 1st line is minimum
     min_change = [Total_amt[0]]
    # print (min_change)
    # Last line is maximum
     max_change = [Total_amt[-1]]
    # print(max_change)

     # Omit first line as that remains unchanged
     # average = total sum of values/total number of lines
     avg_amt.pop(0)
     rowcount = len(avg_amt)
     #print (rowcount)
     avg_change = sum(avg_amt)/rowcount
     print ("Average Change:$",round(avg_change,2))


    # Read the max and min value in Profit Loss list and output that line
     for i in (Profit_loss):
        if (i[1] == max_change[0]):
           print ("Greatest Increase in Profits:",i)
           maxrow = (i)
     for i in (Profit_loss):
     
        if (i[1] == min_change[0]):
           print ("Greatest Increase in Profits:",i)
           minrow = (i)
# write to file
with open(outfile, "w", newline='') as datafile:
            datafile.write("Financial Analysis")
            datafile.write("\n Total Months :")
            datafile.write(str(totalmonth))
            datafile.write("\n Total :$")
            datafile.write(str(totalamount))
            datafile.write("\n Average Change :$")
            datafile.write(str(round(avg_change,2)))
            datafile.write("\n Greatest Increase in Profits :")
            datafile.write(str(maxrow))    
            datafile.write("\n Greatest Decrease in Profits :")
            datafile.write(str(minrow))     

datafile.close()            
