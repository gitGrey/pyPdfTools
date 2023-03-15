# importing required modules 
import os
import sys
import PyPDF2 

print("#")
print("# Get Text From PDF File")
print("#")

fn_in = "ex1.pdf"
fn_in = "ex2.pdf"
fn_in = "ex3.pdf"
fn_in = "vega10.pdf"
fn_in = "hochwasserdaten.pdf"
fn_in = "56177_1_01-FP6-Processor-FuncDataSheet.pdf"

exists = os.path.isfile(fn_in)

if not exists:
    print("nothing to do, file not found: %s" % fn_in)
    print("exit now :-)")
    sys.exit()

# creating a pdf file object 
pdfFileObj = open(fn_in, 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# printing number of pages in pdf file 
print("Num of Pages: %d" % pdfReader.numPages) 
 
pageNum=0
pages = pdfReader.getNumPages()  

for i in range(0, pages):  
    
    pageNum+=1
    print("")  
    print("Working on Page : %02d / %02d"  % (pageNum, pages))    
    
    # creating a page object 
    pageObj = pdfReader.getPage(i) 
      
    # extracting text from page 
    text = pageObj.extractText() 
    
    if 0:
        #remove unwanted cr, lf,
        text = text.replace('\r', "")
        text = text.replace('\n', "")
        text = text.replace('\r\n', "")
        
    if 1:
        # write a file which contains 
        # the text of the current page 
        fn_out = (fn_in + "-text-page-%03d" % pageNum) + ".txt"
        file_id = open(fn_out,"w+")
        file_id.write(text)
    
    print("%s" % text) 

  
# closing the pdf file object 
pdfFileObj.close() 

print("#")
print("# Done")
print("#")
