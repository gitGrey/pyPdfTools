from PyPDF2 import PdfReader

reader = PdfReader("MageDok-T156A-4k-UserManual.pdf")

page = reader.pages[0]
count = 0

for image_file_object in page.images:
    
    fn = str(count) + image_file_object.name
    print(fn)
    with open(fn, "wb") as fp:
        fp.write(image_file_object.data)
        count += 1
        
        
print ("ready")