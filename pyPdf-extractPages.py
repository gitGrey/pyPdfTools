##!/usr/bin/env python

# importing required modules 
import os
import time
import PyPDF2 
import datetime 

#A simple script to remove extra pages from a PDF doc.
#Requires python3 and PyPDF2

from PyPDF2 import PdfWriter, PdfReader

fnIn = "MageDok-T101C-1920x1200-UserManual.pdf"

output = PdfWriter()
input1 = PdfReader(open(fnIn, "rb"))

(fnInFn, fnInExt) = os.path.splitext(fnIn)

pages = len(input1.pages)

# print how many pages input1 has, because why not:
print ("Using File: %s " % fnIn)
print ("Input has %d pages." % pages)
# ask user
print("List the page numbers to extract. Sep. by spaces. (Type Numbers and end with ENTER)")
# example
# 25 26 27 28 29 30 46 48 49 50 52
skippages = [int(x) for x in input().split()]

for idx,x in enumerate(input1.pages):
    if(idx+1 in skippages):
        output.add_page(input1.pages[idx])
    else:
        print("Skipping page : "+str(idx+1))

print ("Output has %d pages." % len(output.pages))

fnOut = fnInFn + "-ext.pdf"

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