from selenium import webdriver
import pdfplumber as pdp
import difflib
import os

"""
These all need to be made into functions so I can 
clean this code up. Because eventually what I will 
want to do is web scrape with selenium then convert
those pdf's into txt files and convert the local
pdfs into txt files so I can compare to see if they
are the same.
"""

chrome_path = "/home/hank/Downloads/chrome_driver/chromedriver"
options = (webdriver.ChromeOptions())

options.add_argument("--no-sandbox")

options.add_argument("--log-level=3")  # This should get rid of a depreciation error.

options.add_argument("--disable-dev-shm-usage")

options.add_argument("disable-infobars")

options.add_argument("--disable-extensions")

options.add_argument(
    "--remote-debugging-port=9222"
)  # This fixed an issue with autodevport or something

# applies the above changes to the webdriver
driver = webdriver.Chrome(chrome_path,options=options)


url = "https://gdchillers.com/product-documentation/"

def scrape(url):
    driver.get(url)
scrape()

path = "/home/hank/Downloads/GD-1.5H-spec-dwg-revE.pdf"
path2 = "/home/hank/Development/pdf_parse/pdf_web_scrapping/a.txt"
path3 = "/home/hank/Development/pdf_parse/pdf_web_scrapping/b.txt"


def open_pdf():
    with pdp.open(path) as pdf:
        first_page = pdf.pages[0]
        print(first_page.extract_text(), file=open("output.txt", "a"))


def compare():
    with open(path3) as f1:
        f1_text = f1.read()

    with open(path2) as f2:
        f2_text = f2.read()

    # Edit this fromfile and tofile to be more accurate. Should be a.txt and b.txt
    for line in difflib.unified_diff(
        f1_text, f2_text, fromfile="file1", tofile="file2", lineterm=""
    ):
        print(line, file=open("diff.txt", "a"))
    try:
        if os.stat("diff.txt").st_size == 0:
            print("There is no difference between the files")
        else:
            print("These files have differences")
    except:
        print("These files are the same")
