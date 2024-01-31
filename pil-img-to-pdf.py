
import os
import sys
import copy
import time
import datetime 

from PIL import Image

#
# the simple way 
#

#image_1 = Image.open(r'C:\Users\Ron\Desktop\Test\view_1.png')
#image_2 = Image.open(r'C:\Users\Ron\Desktop\Test\view_2.png')
#image_3 = Image.open(r'C:\Users\Ron\Desktop\Test\view_3.png')
#image_4 = Image.open(r'C:\Users\Ron\Desktop\Test\view_4.png')

#im_1 = image_1.convert('RGB')
#im_2 = image_2.convert('RGB')
#im_3 = image_3.convert('RGB')
#im_4 = image_4.convert('RGB')

#image_list = [im_2, im_3, im_4]

#im_1.save(r'C:\Users\Ron\Desktop\Test\my_images.pdf', save_all=True, append_images=image_list)


currentDirectoryName = os.getcwd()
print("Current Directory %s" % currentDirectoryName)
searchDir = os.path.join(currentDirectoryName, "fuel-data-org")
searchDir = r"C:\Users\shs\Pictures\aaa-screenshots\1"
searchDir = r"C:\Users\shs\Documents\230707-EOL-AOL1454-N-FET\py\Eval-AOL-vs-ISC-LM5116-Stiched"
searchDir = r"D:\actia-py-scripts\keyboard"
#searchDir = r"C:\Users\shs\Documents\230801-Cicor-IVECO-DSUB\steckzyklen-tester-docs\test-data-for-amphenol-10090926-P264XLF"
#searchDir = r"C:\Users\shs\Documents\230801-Cicor-IVECO-DSUB\steckzyklen-tester-docs\test-data-for-amphenol-10090926-P266XLF"

dirContent = os.listdir(searchDir)


fileList = []
imgList  = []

for obj in dirContent:
    
    objIsDir  = os.path.isdir(obj)
    objExt    = os.path.splitext(obj)[1]
    objExt    = objExt.lower()
    
    #print("%s %s" % (objIsDir, objExt))
    
    if ( objIsDir ):
        # do nothing with directories
        pass
    else:
        allowed=False
        
        if ( ".png" in objExt ):
            print("allowed")
            #allowed=True
        elif ( ".gif" in objExt ):
            print("allowed")
            allowed=True    
        elif ( ".jpg" in objExt ):
            print("allowed")
            #allowed=True                
            
        else:
            pass  
        
        if (allowed):
            theFile  = obj
            #print("unsorted: - %s" % theFile)
            theFile =  os.path.join(searchDir, obj)
            fileList.append(theFile)
            print("File found (unsorted): " + theFile)                            
        

sorted(fileList, reverse=False) # sort numerically in ascending order

i=0
for filename in fileList:
    i+=1
    print("%s - Append File: - %s" % (i, filename))
    
    img     = Image.open(filename)
    img_rgb = img.convert('RGB')
    
    if (i==1):
        img1_rgb = img_rgb
    else:
        imgList.append(img_rgb)

    
now = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
print("File-Prefix %s" % now)

outP  = searchDir
outFn = now + "-Img-PDF.pdf"    

outFfn = os.path.join(outP, outFn) 

img1_rgb.save(outFfn, save_all=True, append_images=imgList)
    
print("# New File here:")
print("%s" % outFfn)
print("# Script Done !!!")
print("#")