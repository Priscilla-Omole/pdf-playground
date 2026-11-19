import sys
from pypdf import PdfWriter

inputs = sys.argv[1:]
merger = PdfWriter()

def pdf_combiner(pdf_list):
    for pdf in pdf_list:
        merger.append(pdf)
        print(pdf)
    merger.write("output-basic.pdf")


pdf_combiner(inputs)