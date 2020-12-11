from selenium import webdriver
import pdfplumber as pdp
import difflib
import os
import time
"""
This might be a good place to use a class
and make an oop script. 

WIP @ oop_scraping.py
"""
# Linux path
# chrome_path = "/home/hank/Downloads/chrome_driver/chromedriver"

#Windows path
chrome_path = r"C:\Program Files (x86)\chromedriver.exe"

options = (webdriver.ChromeOptions())

# Should add the preferences from the default profile.
options.add_argument("user-data-dir=C:\\Users\\Hank\\AppData\\Local\\Google\\Chrome\\User Data")

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


def scrape():
    url = "https://gdchillers.com/product-documentation/"
    driver.get(url)
# scrape()

def single_stage():
    url = "https://gdchillers.com/product-documentation/"
    driver.get(url)
    for i in range(1,7):
        driver.find_element_by_xpath(f'//*[@id="content"]/div/div/main/div/div/div[1]/div/div/div/ul/li[{i}]').click()
        time.sleep(1)
    
single_stage()

def multi_stage():
    for i in range(1,6):
        driver.find_element_by_xpath(f'/html/body/div[1]/div/div/main/div/div/div[2]/div/div/div/ul/li[{i}]').click()
        time.sleep(1)
multi_stage()    

def vas():
    for i in range(1,8):
        driver.find_element_by_xpath(f'/html/body/div[1]/div/div/main/div/div/div[3]/div/div/div/ul/li[{i}]').click()
        time.sleep(1)
vas()        
    
def low_temp():
    for i in range(1,10):
        driver.find_element_by_xpath(f'/html/body/div[1]/div/div/main/div/div/div[4]/div/div/div/ul/li[{i}]').click()
        time.sleep(1)
low_temp()

def tandem():
    for i in range(1,10):
        driver.find_element_by_xpath(f'/html/body/div[1]/div/div/main/div/div/div[5]/div/div/div/ul/li[{i}]').click()
        time.sleep(1)
tandem()
        
def modular():
    for i in range(1,5):
        driver.find_element_by_xpath(f'/html/body/div[1]/div/div/main/div/div/div[6]/div/div/div/ul/li[{i}]').click()
        time.sleep(1)
modular()
        
def exp_mod():
    for i in range(1,9):
        driver.find_element_by_xpath(f'/html/body/div[1]/div/div/main/div/div/div[7]/div/div/div/ul/li[{i}]').click()
        time.sleep(1)
exp_mod()
        
def fire_n_ice():
    for i in range(1,10):
        driver.find_element_by_xpath(f'/html/body/div[1]/div/div/main/div/div/div[8]/div/div/div/ul/li[{i}]').click()
        time.sleep(1)
fire_n_ice()
        
def heaters():
    for i in range(1,8):
        driver.find_element_by_xpath(f'/html/body/div[1]/div/div/main/div/div/div[9]/div/div/div/ul/li[{i}]').click()
        time.sleep(1)
    driver.close()
heaters()        
    
    
# Linux paths
# path = "/home/hank/Downloads/GD-1.5H-spec-dwg-revE.pdf"
# path2 = "/home/hank/Development/pdf_parse/pdf_web_scrapping/a.txt"
# path3 = "/home/hank/Development/pdf_parse/pdf_web_scrapping/b.txt"

# Use .split() to split the words so I am not getting
# the difference in words and not letters.

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


#This still needs to be fixed.
def dir_walk():
    lists = os.walk(save_path)
    for path, dir, filenames in lists:
        for filename in filenames:
            if filename.endswith('.xlsx'):
                doc = os.path.join(path, filename)
                print(doc)
