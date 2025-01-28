import csv 

data = open('c:/Users/nkypri01/Downloads/MyPythonExercises/15_CSV_files/example.csv',encoding="utf-8")   #open the file and define encoding standard
csv_data = csv.reader(data)                 # read and write tabular data in CSV format
data_lines = list(csv_data)                 # reformat the csv into a python object list of lists

# print(data_lines)

print(len(data_lines))          # returns rows + header

for line in data_lines[:5]:     # return the first 5 records
    print(line)

print(data_lines[1][3])         # return the email of the first record


all_emails = []                 # return only the emails (for the first 10 records)       
for line in data_lines[1:10]:
    all_emails.append(line[3])
print(all_emails)


## WRITE TO A NEW FILE ## 

file_to_output = open('c:/Users/nkypri01/Downloads/MyPythonExercises/15_CSV_files/to_save_file.csv','w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')               # other common delimiters are ';' and '\t'

csv_writer.writerow(['a','b','c'])                                  # write a single row 
csv_writer.writerows([['1','2','3'],['4','5','6']])                 # write multiple rows

file_to_output.close()


## WRITE TO EXISTING FILE ##

f = open('c:/Users/nkypri01/Downloads/MyPythonExercises/15_CSV_files/to_save_file.csv','a',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['new','new','new'])
f.close()

