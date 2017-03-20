# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
import re

input_file = csv.DictReader(open('football.csv'))
min_diff,team_name  = None, None

for row in input_file:
    diff = int(row['Goals']) -  int(row['Goals Allowed'])
    if min_diff == None or min_diff > diff:
        min_diff = diff
        team_name = row['Team']

print ("Team with least difference in goals is %s." %team_name)

