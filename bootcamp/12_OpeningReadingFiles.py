
## OPENING AND READING FILES 

# Create a practice file
# File will be created in your current working directory. Use 'pwd' to check it and if necessary change it. 
f = open('practice.txt','w+')
f.write('test - 2')
f.close()

## Listing Files in a Directory
import os

os.getcwd()                                                                     # Get current working directory
os.listdir()                                                                    # Get list of items in current directory
os.listdir("c:/Users/nkypri01/Downloads/MyPythonExercises/")                    # Get list of items in specified directory

print(os.listdir("c:/Users/nkypri01/Downloads/MyPythonExercises/"))

## Change Directory

os.chdir('Downloads/MyPythonExercises/exe_unzipped/extracted_content')
path = os.getcwd()
print(path)



## Move files to different locations. (Keep in mind, there are permission restrictions)

import shutil

# shutil.move('practice.txt',"c:/Users/nkypri01/Downloads/")



## Deleting Files
'''
The os module provides 3 methods for deleting files:

os.unlink(path) which deletes a file at the path your provide
os.rmdir(path) which deletes a folder (folder must be empty) at the path your provide
shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders contained in the path. 

All of these methods can not be reversed! Which means if you make a mistake you won't be able to recover the file. 

Instead we will use the send2trash module. A safer alternative that sends deleted files to the trash bin instead of permanent removal.


Install the send2trash module with:

>> pip install send2trash
'''

import send2trash

# send2trash.send2trash('practice.txt')



## Walking through a directory

'''
os.walk(path) 

displays the file names in the specified directory tree by traversing the tree either in top-down or bottom-up approach.
For each directory in the tree, it produces a 3-tuple that contains the directory path, a list of sub-directories inside the current directory, and filenames.
'''

for folder , sub_folders , files in os.walk("c:/Users/nkypri01/Downloads/"):        # tuple unpacking
    
    print("Currently looking at folder: "+ folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
    
    print('\n')
    
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
    print('\n')