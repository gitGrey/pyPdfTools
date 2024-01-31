# importing required modules
import os
import sys
import PyPDF2
import subprocess

def trimStr(theStr):
    if 1:
        #remove unwanted cr, lf,
        theStr = theStr.replace('\r', "")
        theStr = theStr.replace('\n', "")
        theStr = theStr.replace('\r\n', "")

    return theStr

print("#")
print("# Check PDF Files if OCR-Layer exists")
print("#")

currentDirectoryName = os.getcwd()
searchDir = os.path.join(currentDirectoryName, "fuel-data-org")
searchDir = r".\KmlBuilder\bin\Debug\AppSupport\7z.exe"
searchDir = r"C:\Users\kzs0z1\Documents\220320-Pdf-Print-Batch\pdf09"
searchDir = r"D:\stefan-home-KnowHow\230705-Pdf-Print-Batch\pdf12"
searchDir = r"D:\actia-normen"
searchDir = r"noocr"
#searchDir = r"D:\stefan-home-KnowHow\230705-Pdf-Print-Batch"

exists = os.path.exists(searchDir)

if not exists:
    print("nothing to do, path not found: %s" % fn_in)
    print("exit now :-)")
    sys.exit()

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

firstTime = True

i=0
for filename in fileList:
    i+=1
    print("%s - Scanning File: - %s" % (i, filename))

    fn_in = "20230707-072443-shs2.pdf-crop.pdf"
    fn_in = filename

    #fn_in=trimStr(fn_in)

    exists = os.path.isfile(fn_in)

    if not exists:
        print("nothing to do, file not found: %s" % fn_in)
        print("exit now :-)")
        sys.exit()

    # creating a pdf file object
    pdfFileObj = open(fn_in, 'rb')

    pageNum=0
    try:
        # creating a pdf reader object
        pdfReader = PyPDF2.PdfReader(pdfFileObj)

        pages = len(pdfReader.pages)
    except:
        continue

    # printing number of pages in pdf file
    print("Num of Pages: %d" % pages)

    totalText = ""

    for p in range(0, pages):

        pageNum+=1

        # we only check first page
        if pageNum > 1:
            break

        print("")
        print("Working on Page : %02d / %02d"  % (pageNum, pages))


        # extracting text from page
        try:
            # creating a page object
            pageObj = pdfReader.pages[p]

            text = pageObj.extract_text()
        except:
            #print("PDF with no OCR Layer found")
            #print("-- > " + fn_in )
            continue



        if 0:
            #remove unwanted cr, lf,
            text = text.replace('\r', "")
            text = text.replace('\n', "")
            text = text.replace('\r\n', "")

        totalText += text

        if 0:
            # write a file which contains
            # the text of the current page
            fn_out = (fn_in + "-text-page-%03d" % pageNum) + ".txt"
            file_id = open(fn_out,"w+")
            file_id.write(text)

        if 0:
            # write a file which contains
            # the text of all pages
            fn_out = (fn_in + "-text-all-pages") + ".txt"
            file_id = open(fn_out, "w+")
            file_id.write(totalText)
            
            
        if 0:
            if text == "":
        
                print("PDF with no OCR Layer found")
                print("-- > " + fn_in )

                # write a file which contains
                # the "no OCR Filenames"
                fn_out = ("noOcrPdfFiles") + ".bat"
                if firstTime:
                    file_id = open(fn_out, "w+") #, encoding="UTF8") #UTF8 Encoding for ä,ö,ü, ...
                    firstTime = False
                    file_id.write("@echo off" + "\n")
                    file_id.write("chcp 1252"  + "\n") # codepage umstellen
                else:
                    file_id = open(fn_out, "a") #, encoding="UTF8")

                file_id.write("copy " + chr(34) + fn_in + chr(34) + " D:\\noOcr\\" + "\n")


        if 1:
            if text == "":
                # now we do ocr with ocrMyPdf Library
                # a valid command for ocrmypdf looks like:
                #
                # ocrmypdf -l deu in.pdf out.pdf
                #
                # eng = english
                # deu = deutsch
                #

                # next lines we try to derive from the
                # filename the document language
                lang = "eng"
                if "din".lower() in fn_in.lower():
                    lang="deu"
                if "vdv".lower() in fn_in.lower():
                        lang="deu"
                if "iso".lower() in fn_in.lower():
                    lang="eng"

                fn_ocr_pdf = os.path.splitext(os.path.basename(fn_in))[0]
                fn_ocr_pdf = fn_ocr_pdf + "-ocr.pdf"
                
                fn_ocr_pdf = "ocr/" + fn_ocr_pdf
                # we have to wrap filenames which include space in '
                ocrCmd = "ocrmypdf -l " + lang + " '" + fn_in + "' '" + fn_ocr_pdf + "'"
                print("The Command which is used (see line below):")
                print(ocrCmd)
                os.system(ocrCmd)



        print("%s" % text)


# closing the pdf file object
pdfFileObj.close()

print("#")
print("# Done")
print("#")
