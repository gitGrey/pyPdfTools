##!/usr/bin/env python

import sys
import time
import datetime 
import subprocess

from PyPDF2 import PdfWriter, PdfReader
from PyPDF2.generic import AnnotationBuilder
from PyPDF2.generic import RectangleObject

fnIn = "ex3.pdf"
#fnIn = "myBlueBox.pdf"
fnIn ="shs2.pdf"

print("INFO:")
print("=====")
print("page origin for coordinates is from PDF to PDF different")
print("x and y axis can be swapped")
print("PyPDF2 Doc's: Typically, that is the lower-left corner.")
print("")

print("Workflow")
print("Step 10: - check where page origin is")
print("           is it lower-left corner (unten links)")
print("           or is it lower right corner (unten rechts).")
print("           set xLL and yLL to 0/0")
print("")
print("Step 20: - check if x and y axes are swapped")
print("           try to identify with the variable here")
print("           in this script called = 'swapAxes'")

reader = PdfReader(fnIn)
writer = PdfWriter()

pageNum = 0


xLL=320
yLL=220

cropBoxW = 90
cropBoxH = 150

xUR=xLL + cropBoxW
yUR=yLL + cropBoxH

swapAxes = 0
#swapAxes = 1

findPageOrigin = 0
#findPageOrigin = 1
if (findPageOrigin):
    # to find page origin
    xLL=0
    yLL=0



#setOriginToLowerLeft=0
#setOriginToLowerLeft=1

# this helps for positioning our cropping area
addTestPageToSeeRectangle = 0
#addTestPageToSeeRectangle = 1


if (1):
    # Inout Error Checking
    
    if (xLL == xUR):
        sys.exit("\nError, xLL and xUR cannot have same value, - EXIT now")
    elif (xLL > xUR):
        sys.exit("\nError, xLL must be smaller than xUR, - EXIT now")
    
    if (yLL == yUR):
        sys.exit("\nError, yLL and yUR cannot have same value, - EXIT now")
    elif (yLL > yUR):
        sys.exit("\nError, yLL must be smaller than yUR, - EXIT now")
    
    if (xUR < xLL):
        sys.exit("\nError, xUR < xLL is not allowed, - EXIT now")
    
    if (yUR < yLL):
        sys.exit("\nError, yUR < yLL is not allowed, - EXIT now")


# get the first page of the document
mypage = reader.pages[0]

# readout th epage size, to get idea where origin is:

pageW = 0 
pageH = 0 

if (1):
    
    print("")
    
    (w, h) = mypage.mediabox.lower_left
    print("Page Size MediaBox (LL): %d %d" % (w, h))    
    print("Page Size MediaBox (LL): %.2f %.2f" % (w, h))    
    print("")
    
    (w, h) = mypage.mediabox.lower_right
    print("Page Size MediaBox (LR): %d %d" % (w, h))
    print("Page Size MediaBox (LR): %.2f %.2f" % (w, h))
    print("")    
    
    (w, h) = mypage.mediabox.upper_left
    print("Page Size MediaBox (UL): %d %d" % (w, h))
    print("Page Size MediaBox (UL): %.2f %.2f" % (w, h))
    print("")    
    
    (w, h) = mypage.mediabox.upper_right
    print("Page Size MediaBox (UR): %d %d" % (w, h))
    print("Page Size MediaBox (UR): %.2f %.2f" % (w, h))
    print("")
    
    pageW = w
    pageH = h


if (xUR> pageW) and (yUR>pageH):
    print("Box out of Page")

#if (setOriginToLowerLeft):
    #xLL = xLL + w
    #yLL = yLL
    
    #xUR = xLL - cropBoxW
    #yUR = yLL + cropBoxH

if (swapAxes):
    tmp = xLL
    xLL = yLL
    yLL = tmp
    
    tmp = xUR
    xUR = yUR
    yUR = tmp


myRect=0
myRect= RectangleObject([float(xLL), float(yLL), float(xUR), float(yUR)])

# add page 1 from reader to output document, unchanged:
if (addTestPageToSeeRectangle):
    writer.add_page(reader.pages[pageNum])

# add page 2 from reader, but rotated clockwise 90 degrees:
#writer.add_page(reader.pages[pageNum].rotate(90))

# add page 3 from reader, but crop it to half size:
page3 = reader.pages[pageNum]

#page3.mediabox.upper_right = ( page3.mediabox.right / 2,
#                               page3.mediabox.top   / 2 )

#page3.mediabox.lower_left = ( page3.mediabox.right / 3,
#                               page3.mediabox.top  / 3 )

#page3.mediabox.upper_right = ( page3.mediabox.right / 3,
#                               page3.mediabox.top   / 3 )

page3.mediabox = myRect
#page3.rotate(270)

writer.add_page(page3)

if (0):    
    # Draw a Rectangle
    
    # rect(xLL, yLL, xUR, yUR)
    # Stefan has added interior color, the we see the rectangle :-)
    annotation1 = AnnotationBuilder.rectangle(
        #rect=(50, 65, 100, 250),
        myRect,
        interiour_color="ff0000",
        # interiour_color=none # for transparent background
    )
    writer.add_annotation(page_number=0, annotation=annotation1)

if (1):
    
    # works, but we have a white box on white ground :-(
    # Stefan has added a border, the we see the rectangle :-)
    
    
    #See the PDF spec for details
    # a value of [0 0 1 [3 2]]
    # speifies a border 1 unit wide, with square corners, drawn with 3-units dashes alternating with 2 unit gaps
    myBorder1 = [0, 0, 1, [3, 2]]
    
    # Add the line
    annotation2 = AnnotationBuilder.link(
        #rect=(50, 65, 100, 250),
        myRect,
        url="https://martin-thoma.com/",
        border=myBorder1
    )
    writer.add_annotation(page_number=0, annotation=annotation2)


if (0):
    
    # works
    
    # Create the annotation and add it
    
    # rect(xLL, yLL, xUR, yUR)
    
    annotation3 = AnnotationBuilder.free_text(
        "Hello World\nThis is the second line!",
        #rect=(50, 65, 100, 250),
        rect=myRect,
        font="Arial",
        bold=True,
        italic=True,
        font_size="20pt",
        font_color="00ff00",
        border_color="0000ff",
        background_color="cdcdcd",
        # background_color=none # for transparent background
    )

    writer.add_annotation(page_number=0, annotation=annotation3)

if (0):    
    
    # official example, but ???
    # ==> produces Error :-(
    #     Incorrect first char in NameObject:(None)
    #     Incorrect first char in NameObject:(None)    
    
    # Add the line
    annotation4 = AnnotationBuilder.line(
        p1=(50, 65),
        p2=(100, 250),
        #rect=(50, 65, 100, 250),        
        rect = myRect,
        text="Hello World - \n Line2",
        title_bar = "by py script",
    )
    writer.add_annotation(page_number=0, annotation=annotation4)
    

if (0):    
        # some text
        
        # rect(xLL, yLL, xUR, yUR)
        annotation5 = AnnotationBuilder.text(
            text = "Hello World",
            #rect=(50, 65, 100, 250),
            rect= myRect,
            open=1,
            flags=1,
        )
        writer.add_annotation(page_number=0, annotation=annotation5)    


# add some Javascript to launch the print window on opening this PDF.
# the password dialog may prevent the print dialog from being shown,
# comment the the encription lines, if that's the case, to try this out:
# writer.add_js("this.print({bUI:true,bSilent:false,bShrinkToFit:true});")

fnOut = fnIn + "-crop.pdf"

now       = datetime.datetime.now()
now_date  = time.strftime("%Y%m%d") 
now_time  = time.strftime("%H%M%S") 
fnOut = now_date + "-" + now_time + "-" + fnOut

# write to document-output.pdf
with open(fnOut, "wb") as fp:
    writer.write(fp)
    
subprocess.Popen(fnOut, shell=True)

print("# ready")