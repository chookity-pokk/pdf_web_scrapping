import pdfplumber as pdp
import difflib
import os

path = "/home/hank/Downloads/GD-1.5H-spec-dwg-revE.pdf"
path2 = "/home/hank/Development/pdf_parse/pdf_web_scrapping/a.txt"
path3 = "/home/hank/Development/pdf_parse/pdf_web_scrapping/b.txt"

with open(path3) as f1:
    f1_text = f1.read()

with open(path2) as f2:
    f2_text = f2.read()

def open_pdf():
    with pdp.open(path) as pdf:
        first_page = pdf.pages[0]
        print(first_page.extract_text(),file=open("output.txt","a"))

for line in difflib.unified_diff(f1_text, f2_text, fromfile='file1', tofile='file2', lineterm=''):
    print(line,file=open("diff.txt", "a"))
try:
    if os.stat("diff.txt").st_size == 0:
        print("There is no difference between the files")
    else:
        print("These files have differences")
except:
    print("These files are the same")
