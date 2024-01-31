#!/usr/bin/env python

import os
import sys
import copy
import time
import datetime

# to install (Win or Linux)
# pip install PyPDF2
import PyPDF2

#from PyPDF2 import PdfFileWriter, PdfFileReader  # old
from PyPDF2 import PdfWriter, PdfReader   # new

# pyPDF2 Naming adjustments
# https://pypdf2.readthedocs.io/en/3.0.0/user/migration-1-to-2.html#naming-adjustments


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

original = "ex3.pdf"

# define crop here
left     = 100
top      = 101
right    = 102
bottom   = 103

# cb = crop box
cb_x = 100
cb_y = 100
cb_w = 400 
cb_h = 200

exists=1

if not exists:
    print("nothing to do, file not found: %s" % original)
    print("exit now :-)")
    sys.exit()

#input = PdfFileReader(original)
input = PdfReader(original)



#output = PdfFileWriter()
output = PdfWriter()

#info=input.getDocumentInfo()
info=input.metadata
if len(info)>=0:
    print("Input PDF File Properties")
    print("=========================")
    print("   - title    = %s" % info.title) 
    print("   - subject  = %s" % info.subject)
    print("   - author   = %s" % info.author)
    print("   - creator  = %s" % info.creator)
    print("   - producer = %s" % info.producer)


pageCnt=1
#pages=input.getNumPages()
pages=len(input.pages)

for i in range(0, pages):
    
    print("")   
    print("Working on Page : %02d / %02d"  % (pageCnt, pages))
    print("")
    pageCnt+=1   
    
    #page = input.getPage(i)   
    page = input.pages[i]
   
    (w, h) = page.mediabox.lower_left
    print("Page Size MediaBox (LL): %d %d" % (w, h))    
    print("Page Size MediaBox (LL): %.2f %.2f" % (w, h))    
    print("")
    
    (w, h) = page.mediabox.lower_right
    print("Page Size MediaBox (LR): %d %d" % (w, h))
    print("Page Size MediaBox (LR): %.2f %.2f" % (w, h))
    print("")    
    
    (w, h) = page.mediabox.upper_left
    print("Page Size MediaBox (UL): %d %d" % (w, h))
    print("Page Size MediaBox (UL): %.2f %.2f" % (w, h))
    print("")    
    
    (w, h) = page.mediabox.upper_right
    print("Page Size MediaBox (UR): %d %d" % (w, h))
    print("Page Size MediaBox (UR): %.2f %.2f" % (w, h))
    print("")
    
    # Default value: same as mediabox
    page_x, page_y = page.cropbox.upper_left
    print("CropBox (UL): %d %d" % (page_x, page_y))    
    print("CropBox (UL): %.2f %.2f" % (page_x, page_y))
    print("")
    
     # convert PyPDF2.FloatObjects into floats
    myUpperLeft =[page_x.as_numeric(), page_y.as_numeric()]
        
    new_upperLeft  = (  myUpperLeft[0] + cb_x,   myUpperLeft[1] - cb_y)
    new_lowerRight = (new_upperLeft[0] + cb_w, new_upperLeft[1] - cb_h)    
        
    #pn = page    
    pn = copy.deepcopy(page)
      
    #ur_px = pn.mediaBox.getUpperRight_x()
    #ur_py = pn.mediaBox.getUpperRight_y()
    
    #ll_px = pn.mediaBox.getLowerLeft_x()
    #ll_py = pn.mediaBox.getLowerLeft_y()
    
    #print("Debug " + str(pn.mediabox.upper_right))
    
    ur_px = pn.mediabox.upper_right[0]
    ur_py = pn.mediabox.upper_right[1]
    
    ll_px = pn.mediabox.lower_left[0]
    ll_py = pn.mediabox.lower_left[1]
    
    ur = (ur_px - right, ur_py - top)
    ll = (ll_px + left,  ll_py + bottom)
    
    print("New Crop Box1: LL(x,y): %.2f %.2f" % (ll[0], ll[1]))
    print("New Crop Box1: UR(x,y): %.2f %.2f" % (ur[0], ur[1]))
    print("")
    
    print("New Crop Box2: UL(x,y): %.2f %.2f" % (new_upperLeft[0],   new_upperLeft[1]))
    print("New Crop Box2: LR(x,y): %.2f %.2f" % (new_lowerRight[0], new_lowerRight[1]))
    print("")
              
    #pn.mediaBox.upperRight = ur
    #pn.mediaBox.lowerLeft  = ll 
    
    #pn.mediabox.upper_right = ur
    #pn.mediabox.lower_left  = ll     
     
    #print("Media Box Size: %s " % pn.mediaBox)
    #print("Media Box Size: %s " % pn.mediabox)
    
    page.cropbox.upper_left  = new_upperLeft
    page.cropbox.lower_right = new_lowerRight    
    
    pn.cropbox.upper_left  = new_upperLeft
    pn.cropbox.lower_right = new_lowerRight    
         
    output.add_page(pn)    
    #output.add_page(page)

fnInFn  = "-"
fnInExt = "-"

(fnInFn, fnInExt) = os.path.splitext(original)

# new pdf file object
fn        = fnInFn + "-cropped.pdf"
now       = datetime.datetime.now()
now_date  = time.strftime("%Y%m%d") 
now_time  = time.strftime("%H%M%S") 
fn        = now_date + "_" + now_time + "_" + fn

newFile = open(fn, 'wb') 
output.write(newFile)
output.close()

size = os.path.getsize(fn)

print("")
print("# New File : %s" % fn)
print("# File Size: %.2fkB" % float(size/1024))
print("# Done")
print("#")

