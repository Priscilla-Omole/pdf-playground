from pypdf import PdfReader, PdfWriter
import sys

# path = sys.argv[1]
# directory = sys.argv[2]

stamp = PdfReader("wtr.pdf").pages[0]

writer = PdfWriter(clone_from=["dummy.pdf"])
for page in writer.pages:
    page.merge_page(stamp, over=False)

writer.write("out-watermark.pdf")
