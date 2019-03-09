#!/usr/bin/python
# coding=utf-8
"""

PDFSplit v0.3 (Quartz GUI)
IdlePhysicist, 2019

This code is an amalgamation of Ben Byram-Wigfield's SPLITPDF v2.0 which I use to learn to PDFKit Framework,
and my own ideas from my previous iterations of PDFSplit.

This will operate in a Automator workflow, which calls this Python script, which will in turn call an
AppleScript used to display a pop up window to as the user for input instuctions as to what functions the Python
script is to carry out.

Options (~Args):
    - Range of pages: -r <start page>-<end page>
    - Individual pages: -i [last page you want individually]

For option 2, the default will be to split every page to a new PDF doc in a new directory. Directory behaveiour
only occurs when >1 PDFs are being created.

"""
import os, sys
import Quartz as Quartz
from LaunchServices import (kUTTypeJPEG, kUTTypeTIFF, kUTTypePNG, kCFAllocatorDefault)
from CoreFoundation import (CFAttributedStringCreate, CFURLCreateFromFileSystemRepresentation, NSURL)

APPLE_SCRIPT = """
    
"""

class App(object):
    def __init__(self):
        pass

    def main(self):
        for filename in sys.argv[1:]:
            strip(filename)

    def createPDFDocumentWithPath(self,path):
        path = path.decode('utf-8')
        pdfURL = NSURL.fileURLWithPath_(path)
        if pdfURL:
            return Quartz.PDFDocument.alloc().initWithURL_(pdfURL)

    def getFilename(self, filepath):
        i=0
        newName = filepath
        while os.path.exists(newName):
            i += 1
            newName = filepath + " %02d"%i
        return newName

    def strip(self,filename):
        #
        pdf = createPDFDocumentWithPath(filename)
        numPages = pdf.pageCount()
        shortName = os.path.splitext(filename)[0]
        prefix = os.path.splitext(os.path.basename(filename))[0]
        metaDict = pdf.documentAttributes()
        folderName = getFilename(shortName)
        try:
            os.mkdir(folderName)
        except:
            print "Can't create directory '%s'"%(folderName)
            sys.exit()

        # For each page, create a file. Index starts at ZERO!!!
        # You won't get leading zeros in filenames beyond 99.
        for i in range (1, numPages+1):
            page = pdf.pageAtIndex_(i-1)
            if page:
                newDoc = Quartz.PDFDocument.alloc().initWithData_(page.dataRepresentation())
                outFile = folderName +"/" + prefix + " %03d.pdf"%i
                newDoc.writeToFile_withOptions_(outFile, metaDict)

if __name__ == "__main__":
    App().main()









'''

#!/usr/bin/python

import os
import argparse

def gs(input_pdf, first, last):
    working_dir = os.getcwd().replace(' ', '\ ')
    result = os.system("""gs -q -dQUIET -dBATCH -dNOPAUSE -sstdout=%stderr \
        -sOutputFile={input_pdf}-{Fpage}-{Lpage}.pdf -dFirstPage={Fpage} -dLastPage={Lpage} \
        -sDEVICE=pdfwrite {input_pdf}.pdf 2>/dev/null"""
        .format(Fpage=first, Lpage=last, input_pdf="/".join([working_dir, input_pdf]) ))
    if result: print("Something bad might have happened\nCheck file name for spaces\nGhostScript returned: {}".format(result))

parser = argparse.ArgumentParser()
parser.add_argument('input_pdf', type=str, help='Input file')
parser.add_argument('-r', help='Range of pages to go to new file, ex. -r 1-5')
parser.add_argument('-i', type=int, default=False, help='Individual pages to new file, ex. -i <Number of pages>')
args = parser.parse_args()
input_pdf  = args.input_pdf.strip('.pdf').replace('(', '_').replace(')', '_').replace(' ', '\ ')
if not args.i:
    page_range = args.r.split('-') # Makes a list of the range! ex. [1,5]
    gs(input_pdf, page_range[0], page_range[1])
else:
    for page in xrange(1, args.i + 1): gs(input_pdf, page, page)
'''
