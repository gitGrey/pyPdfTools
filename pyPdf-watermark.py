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

def watermark(input_pdf, output_pdf, watermark_pdf):
    watermark = PdfFileReader(watermark_pdf)
    watermark_page = watermark.getPage(0)

    pdf = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()

    for page in range(pdf.getNumPages()):
        pdf_page = pdf.getPage(page)
        pdf_page.mergePage(watermark_page)
        pdf_writer.addPage(pdf_page)

    with open(output_pdf, 'wb') as fh:
        pdf_writer.write(fh)

if __name__ == '__main__':
        
    fn_in = "ex1.pdf"
    
    # new pdf file object
    fn        = "watermark-out.pdf"
    now       = datetime.datetime.now()
    now_date  = time.strftime("%Y%m%d") 
    now_time  = time.strftime("%H%M%S") 
    fn_out        = now_date + "_" + now_time + "_" + fn    
        
    watermark(input_pdf=fn_in, output_pdf = fn_out, watermark_pdf='watermark.pdf')
    
    size = os.path.getsize(fn_out)
    
    print("")
    print("# New File : %s" % fn_out)
    print("# File Size: %.2fkB" % float(size/1024))
    print("# Done")
    print("#")    