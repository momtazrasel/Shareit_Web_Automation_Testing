import time
# from lib2to3.pgen2 import driver

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from Locators.locators import BusinessPageLocators
from Locators.locators import BusinessPageLocators
from Pages.HomePage import HomePage


# from Pages.OverviewPage import OverviewPageLocators


class BusinessPage(HomePage):
    def __init__(self, driver):
        self.locator = BusinessPageLocators
        self.locator = BusinessPageLocators
        self.driver = driver
        super(BusinessPage, self).__init__(driver)

    def business_page_option(self):
        time.sleep(4)
        self.find_element(*self.locator.click_business_xpath).click()

    def overview_page_option(self):
        time.sleep(4)
        self.find_element(*self.locator.click_overview_xpath).click()

    def solution_page_option(self):
        time.sleep(4)
        self.find_element(*self.locator.click_solution_xpath).click()

    def success_stories_page_option(self):
        time.sleep(4)
        self.find_element(*self.locator.click_success_stories_xpath).click()

    def region_field(self):
        time.sleep(4)
        self.find_element(*self.locator.region_xpath).click()

    def region_select(self):
        time.sleep(4)
        self.find_element(*self.locator.select_region_xpath).click()

    def industry_field(self):
        time.sleep(4)
        self.find_element(*self.locator.industry_xpath).click()

    def industry_select(self):
        time.sleep(4)
        self.find_element(*self.locator.industry_select).click()

    def objective_field(self):
        time.sleep(4)
        self.find_element(*self.locator.objective_xpath).click()

    def objective_select(self):
        time.sleep(4)
        self.find_element(*self.locator.objective_select_xpath).click()

    def content_page_option(self):
        time.sleep(4)
        self.find_element(*self.locator.click_content_xpath).click()

    def first_name(self):
        time.sleep(4)
        self.find_element(*self.locator.first_name_xpath).send_keys("Momtaz")

    def last_name(self):
        time.sleep(4)
        self.find_element(*self.locator.last_name_xpath).send_keys("Rasel")

    def country_code(self):
        time.sleep(4)
        self.find_element(*self.locator.select_country_code).click()

    def bd_code(self):
        time.sleep(4)
        self.find_element(*self.locator.select_bd_code).click()

    def mobile_no(self):
        time.sleep(4)
        self.find_element(*self.locator.mobile_no_xpath).send_keys("1794558666")

    def email(self):
        time.sleep(4)
        self.find_element(*self.locator.email_xpath).send_keys("momtazrasel8@gmail.com")

    def company(self):
        time.sleep(4)
        self.find_element(*self.locator.company_xpath).send_keys("QUPS")

    def job_title(self):
        time.sleep(4)
        self.find_element(*self.locator.job_title_xpath).send_keys("SQA Intern")

    def select_industry(self):
        time.sleep(4)
        self.find_element(*self.locator.industry_select_xpath).click()

    def select_industry_option(self):
        time.sleep(4)
        self.find_element(*self.locator.select_industry_xpath).click()

    def select_company_region(self):
        time.sleep(4)
        self.find_element(*self.locator.select_company_region).click()

    def company_region(self):
        time.sleep(4)
        self.find_element(*self.locator.company_region_xpath).click()

    def message(self):
        time.sleep(4)
        self.find_element(*self.locator.message_xpath).send_keys("i am here for learning purpose")

    def submit_button(self):
        time.sleep(4)
        self.find_element(*self.locator.submit_button_xpath).click()

    def test_solution(self):
        time.sleep(3)
        self.find_element(*self.locator.click_solution_xpath).click()

    # def check_box(self):
    #     time.sleep(3)
    #     self.find_element(*self.locator.check_box_xpath).click()

    # def checked(self):
    #     time.sleep(1)
    #     self.find_element(*self.locator.checked_xpath).click()