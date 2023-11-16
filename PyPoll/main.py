import os

# Module for reading CSV files
import csv
import json

#List
totalvotes = 0
winner = ""
eachvote = 0
eachper = 0
candidate = ''
csvpath = 'Resources/election_data.csv'
outfile = 'Analysis/election_results.txt'
textvote = "Total Votes  : "
textwinner = "Winner is :  "
percentsign = '%'

#read file 
with open(csvpath) as csvfile:
     #reader_obj = csv.DictReader(csvfile)
    # CSV reader specifies delimiter and variable that holds contents
     csvreader = csv.reader(csvfile, delimiter=',')
     #skip header
     csv_header = next(csvreader)
     #define dictionary
     data_vote = {}

     #get count for eac row
     for row in csvreader:
             
          if row[2] not in data_vote:
             data_vote[row[2]] = 1
          else:
             data_vote[row[2]] += 1
     # Get sum of votes        
     totalvotes = sum (data_vote.values())
     # print output
     print ("Election Results")
     print ("______________________")
     print ("Total Votes: ", totalvotes)
     print ("______________________")
     #write to text file as f string
with open(outfile, "w", newline='') as datafile:

     datafile.write("Election Reults")
     datafile.write(f"\n{ textvote + str(totalvotes)}")

     #calculate percentage for each candidate whch is key
     for key,val in data_vote.items():
          print (key)
          print (val)
          per_val = ((val)/totalvotes) * 100
          round (per_val,3)
          print (round(per_val,3)) 
          eachper = (round(per_val,3))
          #print (val)
          
          datafile.write(f"\n {key} { str(val)}  {str(eachper)+ percentsign }")
          
     #print (data_vote)    used in analysis
     #get max value row and winner
     winner = (max(data_vote,key=data_vote.get))
     datafile.write(f"\n{textwinner + (winner)}")
 
print ("______________________")
print ("Winner is:  "+(winner))  

#close file
datafile.close()
    