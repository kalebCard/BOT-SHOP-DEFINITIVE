from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
import sys

class TestWebNavigation(unittest.TestCase):
    def setUp(self):
        self.driver = None
        self.category_option = 1

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_web_navigation(self):
        self.start_browser()
        self.open_link()
        self.close_popups()
        self.category_selector(self.category_option)
        self.wait_seconds(5)

    def start_browser(self):
        chrome_options = Options()
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.63 Safari/537.36")
        chrome_options.add_argument("--incognito")
        
        try:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            self.driver.maximize_window()
        except WebDriverException as e:
            print("Error al iniciar el navegador:", e)
            sys.exit(1)

    def open_link(self):
        self.driver.get('https://www.shein.com.co/')

    def wait_seconds(self, seconds):
        time.sleep(seconds)
        
    def close_popups(self):
        xpath_list = {"close_cookie": "//*[@id='onetrust-reject-all-handler']",
                    "close_offer": "//*[@class='sui-icon-common__wrap btn-default']"}
        for element_name, xpath in xpath_list.items():
            try:
                xpath_browser = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
                xpath_browser.click()
                print("Clicked", element_name)
            except Exception as e:
                print("Error clicking", element_name, ":", e)

    def category_selector(self, options):
        xpath_list= {"women_clothing": "/html/body/div[1]/header/div[3]/div[1]/div/div[3]/nav/div[2]/div/a[3]",
                    "men_clothing": "/html/body/div[1]/header/div[3]/div[1]/div/div[3]/nav/div[2]/div/a[7]"}
        if options == 1:
            xpath=xpath_list["women_clohting"]
        elif options == 2:
            xpath=xpath_list["momen_clohting"]

        try:
            xpath_browser = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            xpath_browser.click()
            self.wait_seconds(5)
        except Exception as e:
            print("Error category selection", ":", e)

    def scrap_page(self):
        xpath_list= {"url_clothing": "//*[@class='product-card multiple-row-card j-expose__product-item product-item-ccc']"}
        for element_name, xpath in xpath_list.items():
            try:
                xpath_browser = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
                xpath_browser.click()
                print("Clicked", element_name)
                self.wait_seconds(5)
            except Exception as e:
                print("Error clicking", element_name, ":", e)

if __name__ == "__main__":
    unittest.main()
