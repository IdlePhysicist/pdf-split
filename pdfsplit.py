#!/usr/bin/python

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_pdf', type=str, help='Input file')
parser.add_argument('-r', help='Range of pages to go to new file, ex. -r 1-5')
args = parser.parse_args()
input_pdf  = args.input_pdf.strip('.pdf')
page_range = args.r.split('-') # Makes a list of the range! ex. [1,5]

os.system("""
    gs -q -dQUIET -dBATCH -dNOPAUSE \
    -sstdout=%stderr \
    -sOutputFile={input_pdf}-{Fpage}-{Lpage}.pdf \
    -dFirstPage={Fpage} -dLastPage={Lpage} \
    -sDEVICE=pdfwrite {input_pdf}.pdf 2>/dev/null"""
    .format(Fpage=page_range[0], Lpage=page_range[1], input_pdf=input_pdf))
