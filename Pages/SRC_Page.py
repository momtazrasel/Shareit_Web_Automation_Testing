import time
# from lib2to3.pgen2 import driver

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from Locators.locators import BusinessPageLocators
from Locators.locators import SRCLocators
from Pages.HomePage import HomePage


# from Pages.OverviewPage import OverviewPageLocators


class SRCPage(HomePage):
    def __init__(self, driver):
        self.locator = SRCLocators
        self.locator = SRCLocators
        self.driver = driver
        super(SRCPage, self).__init__(driver)

    def src(self):
        time.sleep(2)
        self.find_element(*self.locator.src_xpath).click()

    def overview_src(self):
        time.sleep(2)
        self.find_element(*self.locator.overview_xpath).click()

    def vulnerability_src(self):
        time.sleep(2)
        self.find_element(*self.locator.vulnerability_xpath).click()

    def announcement_src(self):
        time.sleep(2)
        self.find_element(*self.locator.announcement_xpath).click()
