#!/usr/bin/env python

import time
import datetime 

from pathlib import Path
from typing import Union, Literal, List

from PyPDF2 import PaperSize
from PyPDF2 import PdfWriter, PdfReader
from PyPDF2.xmp import XmpInformation

def watermark(
    content_pdf: Path,
    stamp_pdf: Path,
    pdf_result: Path,
    page_indices: Union[Literal["ALL"], List[int]] = "ALL",
):
    reader = PdfReader(content_pdf)
    if page_indices == "ALL":
        page_indices = list(range(0, len(reader.pages)))

    writer = PdfWriter()
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox

        # You need to load it again, as the last time it was overwritten
        reader_stamp = PdfReader(stamp_pdf)
        image_page = reader_stamp.pages[0]

        image_page.merge_page(content_page)
        image_page.mediabox = mediabox
        writer.add_page(image_page)

    with open(pdf_result, "wb") as fp:
        writer.write(fp)
        

print("#")
print("# Watermark Underlay PDF File")
print("#")

fnIn = "ex1.pdf"        

input = PdfReader(fnIn)
#info=input.getDocumentInfo()
info=input.metadata
if len(info)>=0:
    print("Input PDF File Properties")
    print("=========================")
    print("   - title             = %s" % info.title) 
    print("   - subject           = %s" % info.subject)
    print("   - author            = %s" % info.author)
    print("   - creator           = %s" % info.creator)
    print("   - producer          = %s" % info.producer)
    print("   - creation date     = %s" % info.creation_date)
    print("   - modification date = %s" % info.modification_date)
    print("")



if (1):
    
    info_xmp=input.xmp_metadata
    print("Input PDF File XMP-Properties")
    print("=============================")    
    print("   - custom_properties = %s" % info_xmp.custom_properties)
    print("   - dc_contributor    = %s" % info_xmp.dc_contributor)
    print("   - dc_coverage       = %s" % info_xmp.dc_coverage)
    print("   - dc_creator        = %s" % info_xmp.dc_creator)
    print("   - dc_date           = %s" % info_xmp.dc_date)
    print("   - dc_description    = %s" % info_xmp.dc_description)
    print("   - dc_format         = %s" % info_xmp.dc_format)
    print("   - dc_identifier     = %s" % info_xmp.dc_identifier)
    print("   - dc_language       = %s" % info_xmp.dc_language)
    print("   - dc_publisher      = %s" % info_xmp.dc_publisher)
    print("   - dc_relation       = %s" % info_xmp.dc_relation)
    print("   - dc_rights         = %s" % info_xmp.dc_rights)
    print("   - dc_source         = %s" % info_xmp.dc_source)
    print("   - dc_subject        = %s" % info_xmp.dc_subject)
    print("   - dc_title          = %s" % info_xmp.dc_title)
    print("   - dc_type           = %s" % info_xmp.dc_type)
    print("")
    print("   - pdf_keywords      = %s" % info_xmp.pdf_keywords)
    print("   - pdf_pdfversion    = %s" % info_xmp.pdf_pdfversion)
    print("   - pdf_producer      = %s" % info_xmp.pdf_producer)
    #print("   - rdfRoot           = %s" % info_xmp.rdf_root)
    print("")
    print("   - xmp_create_date   = %s" % info_xmp.xmp_create_date)
    print("   - xmp_creator_tool  = %s" % info_xmp.xmp_creator_tool)
    print("   - xmp_metadata_date = %s" % info_xmp.xmp_metadata_date)
    print("   - xmp_modify_date   = %s" % info_xmp.xmp_modify_date)
    print("")
    print("   - xmpmm_document_id = %s" % info_xmp.xmpmm_document_id)
    print("   - xmpmm_instance_id = %s" % info_xmp.xmpmm_instance_id)
    print("")

  

A4_w = PaperSize.A4.width
A4_h = PaperSize.A4.height
print("PaperSize: %s %s" % (A4_w, A4_h))



fnWatermark = "watermark.pdf"

fnOut = fnIn + "-watermark-underlay.pdf"

now       = datetime.datetime.now()
now_date  = time.strftime("%Y%m%d") 
now_time  = time.strftime("%H%M%S") 
fnOut = now_date + "-" + now_time + "-" + fnOut
        
watermark(fnIn, fnWatermark, fnOut, "ALL")    

print("#")
print("# Ready")
print("#")

