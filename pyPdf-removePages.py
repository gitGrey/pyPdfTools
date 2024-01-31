##!/usr/bin/env python

# importing required modules 
import os
import time1
import PyPDF2 
import datetime 

#A simple script to remove extra pages from a PDF doc.
#Requires python3 and PyPDF2

from PyPDF2 import PdfFileWriter, PdfFileReader

fnIn="ADP_OSP_IO_Blade-200129.pdf"

output = PdfFileWriter()
input1 = PdfFileReader(open(fnIn, "rb"))

(fnInFn, fnInExt) = os.path.splitext(fnIn)

# print how many pages input1 has, because why not:
print ("Using File: %s " % fnIn)
print ("Input has %d pages." % input1.getNumPages())
# ask user
print("List the page numbers you want to delete. Sep. by spaces. (Type Numbers and end with ENTER)")

skippages = [int(x) for x in input().split()]

for idx,x in enumerate(input1.pages):
    if(idx+1 in skippages):
        print("Skipping page: "+str(idx+1))
    else:
        output.addPage(input1.getPage(idx))

print ("Output has %d pages." % output.getNumPages())

fnOut = fnInFn + "-rem.pdf"

now       = datetime.datetime.now()
now_date  = time.strftime("%Y%m%d") 
now_time  = time.strftime("%H%M%S") 
fnOut = now_date + "-" + now_time + "-" + fnOut

print("Started Writing Final PDF File")
outputStream = open(fnOut, "wb")
output.write(outputStream)
outputStream.close()
print("Stopped Writing Final PDF File")

print("")
print("#")
print("# Ready")
print("# File created: %s" % fnOut)