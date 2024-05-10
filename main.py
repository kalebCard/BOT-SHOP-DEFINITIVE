import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestWebNavigation(unittest.TestCase):
    def setUp(self):
        self.driver = None

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_web_navigation(self):
        self.start_browser()
        self.open_link()
        self.clicker()
        self.wait_seconds(5)

    def start_browser(self):
        chrome_options = Options()
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.63 Safari/537.36")
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.implicitly_wait(10)

    def open_link(self):
        self.driver.get('https://www.shein.com.co/')

    def wait_seconds(self, seconds):
        time.sleep(seconds)
        
    def clicker(self):
        xpath_list=[("close_cookie","//*[@id='onetrust-reject-all-handler']"),("close_offer", "//*[@class='sui-icon-common__wrap btn-default']")]
        counter=0
        while counter < 2:
            try:
                self.wait_seconds(5)
                xpath_route = xpath_list[1][counter]  
                xpath_browser = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_route)))
                xpath_browser.click()
            finally:
                print ("cliker", xpath_list[0][counter])
                counter+=1
        
if __name__ == "__main__":
    unittest.main()
