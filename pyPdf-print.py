##!/usr/bin/env python

import sys
import copy
import time
import datetime 

# to install (Win or Linux)
# pip install PyPDF2
import PyPDF2

from PyPDF2 import PdfFileWriter, PdfFileReader

from enum import Enum

class ePageFormat(Enum):
    portrait = 1
    landscape = 2


#input = PdfFileReader(sys.stdin)
fn_in = "ex2.pdf"
input = PdfFileReader(fn_in)

print("Input File: %s" % fn_in)
print("   - pages: %d" % input.numPages)
print("   - layout : %s" % input.pageLayout)    

info=input.getDocumentInfo()
if len(info)>=0:
    print("   - title    = %s" % info.title) 
    print("   - subject  = %s" % info.subject)
    print("   - author   = %s" % info.author)
    print("   - creator  = %s" % info.creator)
    print("   - producer = %s" % info.producer)
    
page=1   
pages=input.getNumPages()

output = PdfFileWriter()

pageFormat=ePageFormat.portrait
pageFormat=ePageFormat.landscape

#for p in [input.getPage(i) for i in range(0, pages)]:
for i in range(0, pages):
    p = input.getPage(i)
       
    print("Working on Page : %02d / %d" % (page, pages))
    page+=1
       
    if pageFormat == ePageFormat.landscape:
    
        p1 = copy.copy(p)
        (w, h) = p1.mediaBox.upperRight
        theSize = (w, h/2)
        #  left half section/page 
        p1.mediaBox.upperRight = theSize 
    
        p2 = copy.copy(p)
        # right right half section/page 
        p2.mediaBox.lowerRight = theSize
    
        output.addPage(p1)
        output.addPage(p2)
        
            
    if pageFormat == ePageFormat.portrait:
    
        p1 = copy.copy(p)
        (w, h) = p1.mediaBox.upperRight
        theSize = (w/2, h/2)
        # top left quater section 
        p1.mediaBox.lowerRight = theSize 
    
        p2 = copy.copy(p)
        # top right quater section 
        p2.mediaBox.lowerLeft = theSize
    
        p3 = copy.copy(p)
        # bot left quater section 
        p3.mediaBox.upperRight = theSize
    
        p4 = copy.copy(p)
        # bot right quater section 
        p4.mediaBox.upperLeft = theSize
    
        output.addPage(p1)
        output.addPage(p2)
        
        output.addPage(p3)
        output.addPage(p4)
    

# new pdf file object
fn        = "out.pdf"
now       = datetime.datetime.now()
now_date  = time.strftime("%Y%m%d") 
now_time  = time.strftime("%H%M%S") 
fn        = now_date + "_" + now_time + "_" + fn

newFile = open(fn, 'wb') 
output.write(newFile)

print("#")
print("# Done - %s" % fn)
print("#")