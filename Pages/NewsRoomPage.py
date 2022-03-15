import time
# from lib2to3.pgen2 import driver

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from Locators.locators import BusinessPageLocators
from Locators.locators import NewsRoomLocators
from Pages.HomePage import HomePage


# from Pages.OverviewPage import OverviewPageLocators


class NewsRoomPage(HomePage):
    def __init__(self, driver):
        self.locator = NewsRoomLocators
        self.locator = NewsRoomLocators
        self.driver = driver
        super(NewsRoomPage, self).__init__(driver)

    def newsroom(self):
        time.sleep(4)
        self.find_element(*self.locator.newsroom_xpath).click()

    def click_all_option(self):
        time.sleep(4)
        self.find_element(*self.locator.click_all_xpath).click()

    def click_one_post(self):
        time.sleep(4)
        self.find_element(*self.locator.click_post_xpath).click()

    def click_twitter(self):
        time.sleep(4)
        self.find_element(*self.locator.click_twitter_xpath).click()

    def click_facebook(self):
        time.sleep(4)
        self.find_element(*self.locator.click_facebook_xpath).click()

    def click_see_more(self):
        time.sleep(4)
        self.find_element(*self.locator.see_more_xpath).click()

    def click_company_option(self):
        time.sleep(4)
        self.find_element(*self.locator.company_xpath).click()

    def click_industry_option(self):
        time.sleep(4)
        self.find_element(*self.locator.industry_xpath).click()

    def click_insight_option(self):
        time.sleep(4)
        self.find_element(*self.locator.insight_xpath).click()
