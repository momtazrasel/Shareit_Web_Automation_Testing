# import time
from Pages.BusinessPage import BusinessPage
from Pages.OverviewPage import OverviewPage
from Tests.BasePage import BasePage


class Business(BasePage):

    def test_Connect(self):
        f = BusinessPage(self.driver)
        f.business_page_option()
        f.content_page_option()
        f.first_name()
        f.last_name()
        f.country_code()
        f.bd_code()
        f.mobile_no()
        f.email()
        f.company()
        f.job_title()
        f.select_industry()
        f.select_industry_option()
        f.select_company_region()
        f.company_region()
        f.message()
        f.submit_button()
        self.driver.quit()
