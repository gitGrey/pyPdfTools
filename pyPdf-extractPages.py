##!/usr/bin/env python

# importing required modules 
import PyPDF2 

#A simple script to remove extra pages from a PDF doc.
#Requires python3 and PyPDF2

from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input1 = PdfFileReader(open("DxArchiver.pdf", "rb"))

# print how many pages input1 has, because why not:
print ("Input has %d pages." % input1.getNumPages())
# ask user
print("List the page numbers to extract. Sep. by spaces. (Type Numbers and end with ENTER)")

skippages = [int(x) for x in input().split()]

for idx,x in enumerate(input1.pages):
    if(idx+1 in skippages):
        output.addPage(input1.getPage(idx))
    else:
        print("Skipping page : "+str(idx+1))

print ("Output has %d pages." % output.getNumPages())
outputStream = open("PyPDF2-output.pdf", "wb")
output.write(outputStream)