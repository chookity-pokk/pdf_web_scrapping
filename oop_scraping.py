from selenium import webdriver
import pdfplumber as pdp
import difflib
import os
import time

"""
So I think I need to also have another function
to run through to pdf's that we have and convert
those into txt files then compare them.
"""

class pdf_comparing:
    # Linux path
    # chrome_path = "/home/hank/Downloads/chrome_driver/chromedriver"

    # Windows path
    chrome_path = r"C:\Program Files (x86)\chromedriver.exe"

    options = webdriver.ChromeOptions()

    # Should add the preferences from the default profile.
    options.add_argument(
        "user-data-dir=C:\\Users\\Hank\\AppData\\Local\\Google\\Chrome\\User Data"
    )

    prefs = {"download.default_directory": r"C:\Users\Hank\Documents\Random Python Scripts\pdf\pdf_web_scrapping\pdfs"}
    
    options.add_argument("--no-sandbox")

    options.add_experimental_option("prefs", prefs)
    
    options.add_argument(
        "--log-level=3"
    )  # This should get rid of a depreciation error.

    options.add_argument("--disable-dev-shm-usage")

    options.add_argument("disable-infobars")

    options.add_argument("--disable-extensions")

    options.add_argument(
        "--remote-debugging-port=9222"
    )  # This fixed an issue with autodevport or something

    # applies the above changes to the webdriver
    driver = webdriver.Chrome(chrome_path, options=options)
    url = "https://gdchillers.com/product-documentation/"
    driver.get(url)

    @property
    def collection(self):
        """
        This will grab all the pdfs from the website
        """
        # single_stage
        for i in range(1, 7):
            self.driver.find_element_by_xpath(
                f'//*[@id="content"]/div/div/main/div/div/div[1]/div/div/div/ul/li[{i}]'
            ).click()
            time.sleep(0.5)

        # multi_stage
        for i in range(1, 6):
            self.driver.find_element_by_xpath(
                f"/html/body/div[1]/div/div/main/div/div/div[2]/div/div/div/ul/li[{i}]"
            ).click()
            time.sleep(0.5)

        # vertical air
        for i in range(1, 8):
            self.driver.find_element_by_xpath(
                f"/html/body/div[1]/div/div/main/div/div/div[3]/div/div/div/ul/li[{i}]"
            ).click()
            time.sleep(0.5)

        # low temp
        for i in range(1, 10):
            self.driver.find_element_by_xpath(
                f"/html/body/div[1]/div/div/main/div/div/div[4]/div/div/div/ul/li[{i}]"
            ).click()
            time.sleep(0.5)

        # tandem
        for i in range(1, 10):
            self.driver.find_element_by_xpath(
                f"/html/body/div[1]/div/div/main/div/div/div[5]/div/div/div/ul/li[{i}]"
            ).click()
            time.sleep(0.5)

        # modular
        for i in range(1, 5):
            self.driver.find_element_by_xpath(
                f"/html/body/div[1]/div/div/main/div/div/div[6]/div/div/div/ul/li[{i}]"
            ).click()
            time.sleep(0.5)

        # expansion module
        for i in range(1, 9):
            self.driver.find_element_by_xpath(
                f"/html/body/div[1]/div/div/main/div/div/div[7]/div/div/div/ul/li[{i}]"
            ).click()
            time.sleep(0.5)

        # fire and ice
        for i in range(1, 10):
            self.driver.find_element_by_xpath(
                f"/html/body/div[1]/div/div/main/div/div/div[8]/div/div/div/ul/li[{i}]"
            ).click()
            time.sleep(0.5)

        # heaters
        for i in range(1, 8):
            self.driver.find_element_by_xpath(
                f"/html/body/div[1]/div/div/main/div/div/div[9]/div/div/div/ul/li[{i}]"
            ).click()
            time.sleep(0.5)

        # Gives a few extra seconds to help the download finish.
        time.sleep(5)
        print("You have successfully downloaded the pdfs.")
        # this will close the browser
        self.driver.close()

    @property
    def open_pdf(self):
        """
        This will turn all the pdfs (local and from the website)
        into text files.
        """
        # This will open up the downloaded pdfs and turn them into txt files
        save_path = r"C:\Users\Hank\Documents\Random Python Scripts\pdf\pdf_web_scrapping\pdfs"
        lists = os.walk(save_path)
        for path, dir, filenames in lists:
            for filename in filenames:
                doc = os.path.join(path, filename)
                with pdp.open(doc) as pdf:
                    first_page = pdf.pages[0]
                    print(first_page.extract_text(), file=open("website_output.txt", "a", encoding="utf-8"))
                # Might want to make this go beforehand so it'll break up the sections
                with open("website_output.txt", 'a', encoding="utf-8") as text:
                    text.write(f"{filename}\n")
                print(f"{filename} converted from pdf to txt.")

        # This opens up the local pdfs and converts them into txt files.
        pathy = r"C:\Users\Hank\Documents\Testom\PDFS"
        listed = os.walk(pathy)
        for path, fir, filenames in listed:
            for filename in filenames:
                doc = os.path.join(path, filename)
                with pdp.open(doc) as pdf:
                    first_page = pdf.pages[0]
                    print(first_page.extract_text(), file=open("local_output.txt", "a", encoding="utf-8"))
                with open("local_output", 'a', encoding='utf-8') as text:
                    text.write(f"{filename} finished\n")
                print(f"{filename} converted from pdf to txt.")


        
    @property
    def compare():
        """
        This compares the two text files generated from 
        the open_pdf function and tell us if there are any differences
        and if so, what they are.
        """
        # this also needs to be fixed.
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


#pc = pdf_comparing()
# pc.collection # This downloads all the pdf's from the website
# pc.open_pdf # This takes the pdf's and converts them to text
# pc.compare # This will compare the sets of pdf's
print(help(pdf_comparing))
