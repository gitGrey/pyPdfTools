##!/usr/bin/env python

import os
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
    unknown = 0
    portrait = 1
    landscape = 2

class eRunMode(Enum):
    sections = 0
    test = 1
    
    
def getPageOrientation(pageMediaBox):
    
    #pdf = PdfFileReader(open('YourPDFname.pdf', 'rb'))
    #page = pdf.getPage(0).mediaBox
    page = pageMediaBox

    ret = ePageFormat.unknown
    
    if page.getUpperRight_x() - page.getUpperLeft_x() > page.getUpperRight_y() -  page.getLowerRight_y():
        print("This Page Orientation: 'Landscape'")
        ret = ePageFormat.landscape
    else:
        print("This Page Orientation: 'Portrait'")
        ret = ePageFormat.portrait

    return ret


def printMediaBox(page):
    (BL_x, BL_y, TR_x, TR_y) = page.mediaBox
    
    print("Rectangle")
    print("   Bottom Left Corner (BL_x, BL_y) : %d , %d" % (BL_x, BL_y))
    print("   Top Right Corner   (TR_x, TR_y) : %d , %d" % (TR_x, TR_y))
    
def printMediaBoxCorners(page):
    print("Rectangle Corner Coords:")
    print("   UL (x,y) %s" % str(page.mediaBox.upperLeft))
    print("   UR (x,y) %s" % str(page.mediaBox.upperRight))
    
    print("   LL (x,y) %s" % str(page.mediaBox.lowerLeft))
    print("   LR (x,y) %s" % str(page.mediaBox.lowerRight))    

paper_sizes = { (842, 1191): 'A3',
                (595,  842): 'A4',
                (420,  595): 'A5',
                (729, 1032): 'B4',
                (516,  729): 'B5',
                (612,  792): 'Letter',
                (612, 1008): 'Legal' }



print("#")
print("# Extract Sections from Page to new File")
print("#")

# read from console
#input = PdfFileReader(sys.stdin)
fn_in = "ex1.pdf"
#fn_in = "ex2.pdf"

if not os.path.exists(fn_in):
    print("nothing to do, file not found: %s" % fn_in)
    print("exit now :-)")
    sys.exit()


input = PdfFileReader(fn_in)

print("")
print("Input File:")
print("===========")
print("   - file name: %s" % fn_in)
print("   - pages    : %d" % input.numPages)
print("   - layout   : %s" % input.pageLayout)    

info=input.getDocumentInfo()
if len(info)>=0:
    print("")
    print("Input PDF File Properties")
    print("=========================")
    print("   - title    = %s" % info.title) 
    print("   - subject  = %s" % info.subject)
    print("   - author   = %s" % info.author)
    print("   - creator  = %s" % info.creator)
    print("   - producer = %s" % info.producer)
    
    
pageNum=0
pages=input.getNumPages()

output = PdfFileWriter()
output2 = PdfFileWriter()

runMode= eRunMode.sections
#runMode= eRunMode.test

#for p in [input.getPage(i) for i in range(0, pages)]:
for i in range(0, pages):
  
     
    pageNum+=1
    print("")  
    print("Working on Page : %02d / %02d"  % (pageNum, pages))
       
    p = input.getPage(i)
      
    pF = getPageOrientation(p.mediaBox)
    
    printMediaBox(p)
    
    printMediaBoxCorners(p)
    
    if 1:
        box = p.mediaBox
        size = (box[2] - box[0], box[3] - box[1])
        print("")
        print("Trying to guess paper size:")
        print("===========================")
        print("   %s seems like: %s" % (size, paper_sizes[size]))
    
    if 1:
        pageRotation= p.get('/Rotate')
        print("")
        print("Trying to get page rotation")
        print("===========================")
        print("   Page Rotation   : %d-Deg" % pageRotation)
       
            
        if runMode==eRunMode.sections:
            
            (BL_x, BL_y, TR_x, TR_y) = p.mediaBox
            
            #
            # define your sections 
            # in x and y here     
            #
            xCnt=2
            yCnt=3
            
            xCnt=3
            yCnt=3
            
            #xCnt=4
            #yCnt=4
            
            #xCnt=10
            #yCnt=10

            n=0
            tCnt = xCnt*yCnt
                        
            pw=TR_x - BL_x
            ph=TR_y - BL_y
            
            fact=(1/72)*2.54
            print("")
            print("Page Size (point): %d x %d" % (pw,ph))
            print("Page Size (inch) : %.1f x %.1f" % (pw/72, ph/72))
            print("Page Size (cm)   : %.1f x %.1f" % (pw*fact, ph*fact))
            
            print("")
            print("You get finally: %dx%d = %d Sections per Page" % (xCnt, yCnt, tCnt))
            print("Your final file will have then %d pages" % (tCnt*pages)) 
            
            dx=int(TR_x/xCnt)
            dy=int(TR_y/yCnt)
            
            print("")
            print("Section Size (point): %d x %d" % (dx, dy))
            print("Section Size (inch) : %.1f x %.1f" % (dx/72, dy/72))
            print("Section Size (cm)   : %.1f x %.1f" % (dx*fact, dy*fact))
            
            for j in range(1, yCnt+1):
                
                for i in range(0, xCnt):
                    n+=1
                    print("")
                    print("Working On Sheet: %d / %d - section: %d / %d" % (pageNum, pages, n, tCnt))
                    
                    px = copy.deepcopy(p)
                    px.mediaBox.lowerLeft=(i*dx, TR_y-(j*dy))
                    px.mediaBox.upperRight=((i+1)*dx, TR_y-((j-1)*dy))
                    #printMediaBox(px)
                    output.addPage(px)            
                    
        if runMode==eRunMode.test:
            (BL_x, BL_y, TR_x, TR_y) = p.mediaBox
            px = copy.deepcopy(p)
            px.mediaBox.lowerLeft=(100,100)
            px.mediaBox.upperRight=(200,200)
            printMediaBox(px)
            output.addPage(px)             
            
            
            
            

# new pdf file object
fn        = "out.pdf"
now       = datetime.datetime.now()
now_date  = time.strftime("%Y%m%d") 
now_time  = time.strftime("%H%M%S") 
fn        = now_date + "_" + now_time + "_" + fn

newFile = open(fn, 'wb') 
output.write(newFile)

#fn        = now_date + "_" + now_time + "_" + "out2.pdf"
#newFile2 = open(fn, 'wb') 
#output2.write(newFile2)

size = os.path.getsize(fn)

print("")
print("# New File : %s" % fn)
print("# File Size: %.2fkB" % float(size/1024))
print("# Done")
print("#")