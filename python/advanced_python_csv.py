import csv

lst_emails = []
f = open('faculty.csv')
csv_file = csv.reader(f)

# skip the header row
next(csv_file)
# add emails to the list 
for row in csv_file:
    lst_emails.append(row[3])  
# write emails list to emails.csv
with open("emails.csv", "w") as f:
    writer = csv.writer(f)
    for email in lst_emails:
        writer.writerow([email]) 
