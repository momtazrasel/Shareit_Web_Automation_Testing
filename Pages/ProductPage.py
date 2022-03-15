import time
# from lib2to3.pgen2 import driver

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from Locators.locators import BusinessPageLocators
from Locators.locators import ProductPageLocators
from Pages.HomePage import HomePage
# from Pages.OverviewPage import OverviewPageLocators


class ProductPage(HomePage):
    def __init__(self, driver):
        self.locator = ProductPageLocators
        self.locator = ProductPageLocators
        self.driver = driver
        super(ProductPage, self).__init__(driver)

    def product_page_option(self):
        time.sleep(2)
        self.find_element(*self.locator.click_product_option).click()

    def share_it(self):
        time.sleep(2)
        self.find_element(*self.locator.share_it_xpath).click()

    def android(self):
        time.sleep(2)
        self.find_element(*self.locator.android_xpath).click()

    def clone_it(self):
        time.sleep(2)
        self.find_element(*self.locator.clone_it_xpath).click()

    def lock_it(self):
        time.sleep(2)
        self.find_element(*self.locator.lock_it_xpath).click()

    def lock_an(self):
        time.sleep(2)
        self.find_element(*self.locator.lock_android).click()

    def lis_it(self):
        time.sleep(2)
        self.find_element(*self.locator.listen_it_xpath).click()

    def clean_it(self):
        time.sleep(2)
        self.find_element(*self.locator.clean_it_xpath).click()

    def language(self):
        time.sleep(3)
        self.find_element(*self.locator.language_xpath).click()

    # def android(self):
    #     time.sleep(2)
    #     self.find_element(*self.locator.android_xpath).click()
