from PyPDF2 import PdfReader



fn = "Form-Test.pdf"
#fn = "20230705-122812-Form-Test-FormFilled.pdf"

reader = PdfReader(fn)

fields = reader.get_form_text_fields()
#print(fields)

for k, v in fields.items():
    #print(k, v)
    
    keyLen = len(k)
    print(k)
    print("=" * keyLen)
    print(v)
    print("")

print("")    
print("#")
print("# Done")
print("#")
    