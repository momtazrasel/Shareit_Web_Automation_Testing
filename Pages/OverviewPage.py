import time

# from selenium.webdriver.common.by import By
# from Locators.locators import OverviewPageLocators
from Locators.locators import BusinessPageLocators
from Pages.HomePage import HomePage


class OverviewPage(HomePage):
    def __init__(self, driver):
        self.locatorOverviewPageLocators = None
        self.locator = BusinessPageLocators
        #self.locator = OverviewPageLocators
        self.driver = driver
        super(OverviewPage, self).__init__(driver)

    def overview_page(self):
        time.sleep(5)
        self.find_element(*self.locator.click_business_xpath).click()
        self.find_element(*self.locator.click_overview_xpath).click()
