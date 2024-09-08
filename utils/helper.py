from datetime import datetime, timedelta
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class CommonOps:


    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(self.driver,20)

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator, return_text=False):
        element = self.find_element(locator).click()
        if return_text:
            return element.text

    def enter_text(self, locator, text, sleep_time=0):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        time.sleep(sleep_time)
        element.send_keys(Keys.ENTER)

    @staticmethod
    def calculate_date(days_from_today):
        return (datetime.now() + timedelta(days=days_from_today)).strftime("%A %d %B %Y")
