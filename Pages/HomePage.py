# from telnetlib import EC

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from Locators.locators import BusinessPageLocators


class HomePage(object):
    def __init__(self, driver: object, base_url: object = "") -> object:
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_all_element(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def send_keys(self, *locator):
        self.driver.find_element(*locator).send_keys()
