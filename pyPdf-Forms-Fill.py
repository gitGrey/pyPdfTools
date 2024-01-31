

import os
import time
import datetime

from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.constants import FieldFlag


print("it is maybe good idea that you perform a 'read-form' first")
print("to get the name of the TextBox which will be filled later on")

fn = "Form-Test.pdf"
#fn = "20230705-122812-Form-Test-FormFilled.pdf"

reader = PdfReader(fn)
writer = PdfWriter()

page = reader.pages[0]

fields = reader.get_fields()

print(fields)

for k, v in fields.items():
    #print(k, v)
    
    keyLen = len(k)
    print(k)
    print("=" * keyLen)
    print(v)
    print("")
    
    if ("Text" in k):
        # from Adobe PDF Spec
        # / Ff = integer value carries various characteristics of the field (table 221)
        for a, b in v.items():
            # from Adobe PDF Spec
            # /FT = Field Type
            # /T = Text String
            # /V = Field Value
            
            print(a) # field name
            print(b) # field value        
        
    
    if ("Check Box" in k):
        
        for a, b in v.items():
            # from Adobe PDF Spec
            # /FT = Field Type
            # /T = Text String
            # /V = Field Value
            
            print(a) # field name
            print(b) # field value
        



writer.add_page(page)

writer.update_page_form_field_values(
    #writer.pages[0], {"fieldname": "some filled in text"}
    writer.pages[0], {"Text9": "some filled in text"} # Table 221 in Adobe PDF Spec
)

writer.update_page_form_field_values(
    # Yes = Checked
    # Off = not checked
writer.pages[0], {"Check Box34": "1"} 
)

fnInNoExt = os.path.splitext(fn)[0]
print(fnInNoExt)

fnOut = fnInNoExt + "-FormFilled.pdf"

now       = datetime.datetime.now()
now_date  = time.strftime("%Y%m%d") 
now_time  = time.strftime("%H%M%S") 
fnOut = now_date + "-" + now_time + "-" + fnOut

print("")
print("Input-File  : %s" % fn)
print("Output-File : %s" % fnOut) 

# write "output" to PyPDF2-output.pdf
with open(fnOut, "wb") as output_stream:
    writer.write(output_stream)
    
    
print("")    
print("#")
print("# Done")
print("#")
    