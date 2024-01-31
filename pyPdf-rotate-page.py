#!/usr/bin/env python

##!/usr/bin/env python3


import os
import sys
import copy
import time
import datetime 

import PyPDF2

currentDirectoryName = os.getcwd()
searchDir = os.path.join(currentDirectoryName, "fuel-data-org")
searchDir = r".\KmlBuilder\bin\Debug\AppSupport\7z.exe"
searchDir = r"C:\Users\kzs0z1\Documents\200105-CES2020-Trip\191215-Reise-LasVegas\Belege"
searchDir = r"C:\Users\kzs0z1\Documents\190320-Pdf-Print-Batch"
searchDir = r"C:\Users\kzs0z1\Documents\190320-Pdf-Print-Batch\pdf05"
dirContent = os.listdir(searchDir)

#
# Get PDF Files from "searchDir"
#

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





i=0
for filename in fileList:
    i+=1
    print("%s - Rotate File: - %s" % (i, filename))

    pdfIn = open(filename, 'rb') # exchange the 'original.pdf' with a name of your file 
    pdfReader = PyPDF2.PdfFileReader(pdfIn)
    pdfWriter = PyPDF2.PdfFileWriter()

    for pageNum in range(pdfReader.numPages):
        page = pdfReader.getPage(pageNum)
        
        #page.rotateClockwise(90)
        page.rotateCounterClockwise(90)
        
        pdfWriter.addPage(page)
      
        (fnInFn, fnInExt) = os.path.splitext(filename)
        fnOut = fnInFn + "_rot.pdf"
        pdfOut = open(fnOut, 'wb')
        pdfWriter.write(pdfOut)
        pdfOut.close()
        pdfIn.close()
        
        
print("# Script Done !!!")
print("#")        