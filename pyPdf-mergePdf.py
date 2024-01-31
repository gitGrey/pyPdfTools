##!/usr/bin/env python

import os
import sys
import copy
import time
import datetime 

# in case of SSL-Cetrificates Warnings and Fetch Problems:
# pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org PyPDF2

#from PyPDF2 import PdfFileMerger, PdfFileReader
from PyPDF2 import PdfMerger, PdfFileReader
from PyPDF2 import PdfMerger, PdfReader

currentDirectoryName = os.getcwd()
searchDir = os.path.join(currentDirectoryName, "fuel-data-org")
searchDir = r".\KmlBuilder\bin\Debug\AppSupport\7z.exe"
searchDir = r"C:\Users\kzs0z1\Documents\200105-CES2020-Trip\191215-Reise-LasVegas\Belege"
searchDir = r"C:\Users\kzs0z1\Documents\190320-Pdf-Print-Batch"
searchDir = r"C:\Users\kzs0z1\Documents\220320-Pdf-Print-Batch\pdf09"
searchDir = r"D:\stefan-home-KnowHow\230705-Pdf-Print-Batch\pdf12"
dirContent = os.listdir(searchDir)


fileList=[]

for obj in dirContent:
    
    objIsDir  = os.path.isdir(obj)
    objExt    = os.path.splitext(obj)[1]
    objExt    = objExt.lower()
    
    #print("%s %s" % (objIsDir, objExt))
    
    if ( objIsDir ):
        # do nothing with directories
        pass
    else:
        if ( ".pdf" in objExt ):
            theFile  = obj
            #print("unsorted: - %s" % theFile)
            theFile =  os.path.join(searchDir, obj)
            fileList.append(theFile)
            print("File found (unsorted): " + theFile)                
            
        else:
            pass   

sorted(fileList, reverse=False) # sort numerically in ascending order

#merger = PdfFileMerger() # old and deprecated
merger = PdfMerger()

# https://stackoverflow.com/questions/17104926/pypdf-merging-multiple-pdf-files-into-one-pdf
i=0
for filename in fileList:
    i+=1
    print("%s - Append File: - %s" % (i, filename))
    #merger.append(PdfFileReader(open(filename, 'rb')))
    merger.append(PdfReader(open(filename, 'rb')))


now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
print("File-Prefix %s" % now)

outFfn = now + "-document-output.pdf"
merger.write(outFfn)
    
print("# New File here: %s" % outFfn)
print("# Script Done !!!")
print("#")
