from selenium import webdriver
import pdfplumber as pdp
import difflib
import os
import time


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

    options.add_argument("--no-sandbox")

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
            time.sleep(.5)

        # multi_stage
        for i in range(1, 6):
            self.driver.find_element_by_xpath(
                f"/html/body/div[1]/div/div/main/div/div/div[2]/div/div/div/ul/li[{i}]"
            ).click()
            time.sleep(.5)

        # vertical air
        for i in range(1, 8):
            self.driver.find_element_by_xpath(
                f"/html/body/div[1]/div/div/main/div/div/div[3]/div/div/div/ul/li[{i}]"
            ).click()
            time.sleep(.5)

        # low temp
        for i in range(1, 10):
            self.driver.find_element_by_xpath(
                f"/html/body/div[1]/div/div/main/div/div/div[4]/div/div/div/ul/li[{i}]"
            ).click()
            time.sleep(.5)

        # tandem
        for i in range(1, 10):
            self.driver.find_element_by_xpath(
                f"/html/body/div[1]/div/div/main/div/div/div[5]/div/div/div/ul/li[{i}]"
            ).click()
            time.sleep(.5)

        # modular
        for i in range(1, 5):
            self.driver.find_element_by_xpath(
                f"/html/body/div[1]/div/div/main/div/div/div[6]/div/div/div/ul/li[{i}]"
            ).click()
            time.sleep(.5)

        # expansion module
        for i in range(1, 9):
            self.driver.find_element_by_xpath(
                f"/html/body/div[1]/div/div/main/div/div/div[7]/div/div/div/ul/li[{i}]"
            ).click()
            time.sleep(.5)

        # fire and ice
        for i in range(1, 10):
            self.driver.find_element_by_xpath(
                f"/html/body/div[1]/div/div/main/div/div/div[8]/div/div/div/ul/li[{i}]"
            ).click()
            time.sleep(.5)

        # heaters
        for i in range(1, 8):
            self.driver.find_element_by_xpath(
                f"/html/body/div[1]/div/div/main/div/div/div[9]/div/div/div/ul/li[{i}]"
            ).click()
            time.sleep(.5)
            
        # Gives a few extra seconds to help the download finish.
        time.sleep(5)
        # this will close the browser
        self.driver.close()

    @property
    def open_pdf(self):
        lists = os.walk(save_path)
        for path, dir, filenames in lists:
            for filename in filenames:
                doc = os.path.join(path, filename)
                with pdp.open(doc) as pdf:
                    first_page = pdf.pages[0]
                    print(first_page.extract_text(), file=open('output.txt', "a"))
                # if filename.endswith('.xlsx'):
                    # doc = os.path.join(path, filename)
                    # print(doc)

    @property
    def compare():
        #this also needs to be fixed.
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

pc = pdf_comparing()
pc.collection
