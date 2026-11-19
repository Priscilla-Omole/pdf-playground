from pypdf import PdfReader, PdfWriter
import sys

# path = sys.argv[1]
# directory = sys.argv[2]

stamp = PdfReader("wtr.pdf").pages[0]

writer = PdfWriter(clone_from="twopage.pdf")
for page in writer.pages:
    page.merge_page(stamp, over=True)

writer.write("out-stamp-two-page.pdf")
