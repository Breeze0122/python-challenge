# 0. Open file as csv import

import csv
import os
import operator
from collections import Counter
    # Def the variable 
row_count=0
unique_candidates = Counter()
vote_count = 0
#with open('/Users/breeze/Desktop/BootCamp/Bootcamp/Challenges/Python-Challenge/python-challenge/PyPoll/Resources/election_data.csv',mode='r',encoding='UTF-8') as csv_file:
with open('.''/Resources/election_data.csv',mode='r',encoding='UTF-8') as csv_file:
    csv_reader= csv.DictReader(csv_file)

    for row in csv_reader:
        # 1. Calculate the total number of votes cast
        row_count+=1
        # 2. Complete list of candidates who received votes create a dictionary to add the candidates and  sume the votes
        candidates=row['Candidate']
        unique_candidates[candidates]+=1

list=''''''
for candidates, count in unique_candidates.items():
        # 3.1 The percentage of votes each candidate won
        # 4. Calculate the total number of votes each candidate won
        list=  list +'''

'''+ f'{candidates} : {"{:,.3%}".format(count/row_count)}   ({"{:,.2f}".format(count)})'

        # 5. Calculate the winner of the election based on popular vote sorting using lambda function. I tried with the sort or sorter operator but it failed.
        
        sorted_list = sorted(unique_candidates, key=lambda x: (x[1]),reverse=True)
        winner = sorted_list[0]




#6. Print Results

Sub1= """ 
_______________________________________
"""

Result= f""" Election Results
______________________________________

Total Votes : {"{:,}".format(row_count)}
{Sub1}
{list}
{Sub1}
Winner: {winner}
{Sub1}
"""
print(Result)

#7. Export in a txt file the Result

with open('PyPoll_Results.txt',mode='w',encoding='UTF=8') as csv_file:
     csv_file.write(Result)





