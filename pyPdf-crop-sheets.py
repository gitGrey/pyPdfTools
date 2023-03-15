#!/usr/bin/env python

import os
import sys
import copy
import time
import datetime

# to install (Win or Linux)
# pip install PyPDF2
import PyPDF2

from PyPDF2 import PdfFileWriter, PdfFileReader

#if __name__ == '__main__' and len(sys.argv) > 5 and sys.argv[1][-3:].upper() == 'PDF':
    
    #original = sys.argv[1]
    #target   = original[:-4] + '.cropped.pdf'
    #left     = int(sys.argv[2])
    #top      = int(sys.argv[3])
    #right    = int(sys.argv[4])
    #bottom   = int(sys.argv[5])


print("#")
print("# Crop Page to content")
print("#")

original = "ex1.pdf"
target   = "cropped.pdf"

# define crop here
left     = 140
top      = 60
right    = 55
bottom   = 60

if not exists:
    print("nothing to do, file not found: %s" % original)
    print("exit now :-)")
    sys.exit()

input = PdfFileReader(original)

output = PdfFileWriter()

info=input.getDocumentInfo()
if len(info)>=0:
    print("Input PDF File Properties")
    print("=========================")
    print("   - title    = %s" % info.title) 
    print("   - subject  = %s" % info.subject)
    print("   - author   = %s" % info.author)
    print("   - creator  = %s" % info.creator)
    print("   - producer = %s" % info.producer)


pageCnt=1
pages=input.getNumPages()

for i in range(0, pages):
    
    print("")   
    print("Working on Page : %02d / %02d"  % (pageCnt, pages))
    pageCnt+=1   
    
    page = input.getPage(i)   
   
    (w, h) = page.mediaBox.upperRight
    print("Page Size: %d %d" % (w, h))
    
    pn = page    
    #pn = copy.deepcopy(page)
      
    ur_px = pn.mediaBox.getUpperRight_x()
    ur_py = pn.mediaBox.getUpperRight_y()
    
    ll_px = pn.mediaBox.getLowerLeft_x()
    ll_py = pn.mediaBox.getLowerLeft_y()
    
    ur = (ur_px - right, ur_py - top)
    ll = (ll_px + left,  ll_py + bottom)
    
    print("Crop Box: LL/UR: %s %s" % (ll, ur))
          
    pn.mediaBox.upperRight = ur
    pn.mediaBox.lowerLeft  = ll 
     
    print("Media Box Size: %s " % pn.mediaBox)
     
    output.addPage(pn)    




# new pdf file object
fn        = "cropped.pdf"
now       = datetime.datetime.now()
now_date  = time.strftime("%Y%m%d") 
now_time  = time.strftime("%H%M%S") 
fn        = now_date + "_" + now_time + "_" + fn

newFile = open(fn, 'wb') 
output.write(newFile)

size = os.path.getsize(fn)

print("")
print("# New File : %s" % fn)
print("# File Size: %.2fkB" % float(size/1024))
print("# Done")
print("#")

