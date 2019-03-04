#!/usr/bin/python

import os
import argparse

def gs(input_pdf, first, last):
    working_dir = os.getcwd()
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
input_pdf  = args.input_pdf.strip('.pdf')#.replace('(', '_').replace(')', '_').replace(' ', '_')
if not args.i:
    page_range = args.r.split('-') # Makes a list of the range! ex. [1,5]
    gs(input_pdf, page_range[0], page_range[1])
else:
    for page in xrange(1, args.i + 1): gs(input_pdf, page, page)
