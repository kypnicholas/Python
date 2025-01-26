## INDIVIDUAL FILES

import zipfile

# Create Files to Compress
f = open("new_file.txt",'w+')
f.write("Here is some text")
f.close()

# Zipping Files
comp_file = zipfile.ZipFile('comp_file.zip','w')                        # Create the zip file
comp_file.write("new_file.txt",compress_type=zipfile.ZIP_DEFLATED)      # Compress and write our text file to our zip file
comp_file.close()

# Extracting from Zip Files
zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall("extracted_content")                                 # you can also use extract() to only grab individual files.



## extract or archive MULTIPLE FILES ##

import shutil                   # The shutil library can accept an archive format: one of "zip", "tar", "gztar", "bztar", or "xztar".

directory_to_zip='c:/Users/nkypri01/Downloads/MyPythonExercises/Other_ToCompress'

# Just fill in the output_filename and the directory to zip
shutil.make_archive('example_zipped','zip',directory_to_zip)

# Extracting a zip archive
shutil.unpack_archive('example_zipped.zip','example_unzipped','zip')        # Notice how the parameter/argument order is slightly different here
