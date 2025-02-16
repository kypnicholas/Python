'''
Keep in mind that not every PDF file can be read with the PyPDF2 library.
This library can only read the text from a PDF document, it won't be able to grab images or other media files from a PDF.
'''

import PyPDF2

f = open('c:/Users/nkypri01/Downloads/MyPythonExercises/16_PDF_files/Working_Business_Proposal.pdf','rb')      # Notice we read it as a binary with 'rb'

pdf_reader = PyPDF2.PdfReader(f)                # Course suggested to use function PyPDF2.PdfFileReader() which is deprecated. Suggested new function PyPDF2.PdfReader()

print(len(pdf_reader.pages))                    # get number of pages

page_one = pdf_reader.pages[0]              
page_one_text = page_one.extract_text()         # READ the text from page 1
print(page_one_text)
f.close()


## WRITE TO A PDF FILE ## 
'''
No open source python program allows you to write to PDFs (because of the differences between the single string type of Python, 
and the variety of fonts, placements, and other parameters that a PDF could have.)

What we can do is copy pages and append pages to the end.
'''

import PyPDF2
f = open('c:/Users/nkypri01/Downloads/MyPythonExercises/16_PDF_files/Working_Business_Proposal.pdf','rb')  

pdf_reader = PyPDF2.PdfReader(f)                # We first read the original file
first_page = pdf_reader.pages(0)              # Get the first page

pdf_writer = PyPDF2.PdfWriter()                 # We created a writer
pdf_writer.addPage(first_page)                  # We added the first page to the writer

pdf_output = open("c:/Users/nkypri01/Downloads/MyPythonExercises/16_PDF_files/Some_New_Doc.pdf","wb")      # Open the new file 

pdf_writer.write(pdf_output)                    # Write the copied page to the new file 

f.close() 
pdf_output.close()
