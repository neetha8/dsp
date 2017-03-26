# coding: utf-8

# In[6]:

import csv 
import sys
import re 

degrees_count, tiltes_count, domains_count = {}, {}, {}

f = open('faculty.csv')
csv_file = csv.reader(f, delimiter = ',')
next(csv_file)

for row in csv_file:
    degree = re.sub('[.]','',row[1]).strip()
    # if there are muliple degrees
    degrees = re.split('\s',degree)
    if len(degrees) > 1:
        for degree in degrees:
            if degree not in degrees_count:
                degrees_count[degree] = 0
            degrees_count[degree] +=1 
            continue
    if degree not in degrees_count:
        degrees_count[degree] = 0
    degrees_count[degree] +=1 
degrees_count   


# In[3]:

f = open('faculty.csv')
csv_file = csv.reader(f, delimiter = ',')
next(csv_file)

tiltes_count = {}
for row in csv_file:
    # Get the title
    title = re.split(r'\bof\b', row[2])[0]
    if title not in tiltes_count:
        tiltes_count[title] = 0
    tiltes_count[title] +=1 
tiltes_count    


# In[7]:

f = open('faculty.csv')
csv_file = csv.reader(f, delimiter = ',')
next(csv_file)
emails = []
domain_names = []
for row in csv_file:
    emails.append(row[3])
    domain_names.append(re.split(r'@', row[3])[1])
print (emails)    
print (set(domain_names))

