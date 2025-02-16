'''
# UNZIP exercise file
import shutil 

directory_to_unzip='c:/Users/nkypri01/Downloads/MyPythonExercises/unzip_me_for_instructions'

shutil.unpack_archive('unzip_me_for_instructions.zip','exe_unzipped','zip')
'''

# Change CWD
import os

path = os.getcwd()                                                          # Get cwd
print(path)

dir_list = os.listdir(path)             
print("Files and directories in '", path, "' :")
print(dir_list)                                                             # Print all files in directory

os.chdir('Downloads/MyPythonExercises/exe_unzipped/extracted_content')      # Change cwd

path = os.getcwd()

print(path)

with open('Instructions.txt') as f:                                         # Open instructions file
    content = f.read()
    print(content)


## SOLVE EXERCISE ## 
import re

def search(file,pattern= r'\d{3}-\d{3}-\d{4}'):
    f = open(file,'r')
    text = f.read()
    
    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ''

import os
results = []
for folder , sub_folders , files in os.walk(os.getcwd()):
    
    for f in files:
        full_path = folder+'\\'+f
         
        results.append(search(full_path)) 
for r in results:
    if r != '':
        print(r.group())