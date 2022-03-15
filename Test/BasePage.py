import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage(unittest.TestCase):
    driver: WebDriver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/All Driver/chromedriver_win32/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("https://www.ushareit.com/")
        print("Tests Started")

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit()
        print("Tests Complete")



