# import time

from Pages.BusinessPage import BusinessPage
from Tests.BasePage import BasePage


class Business(BasePage):

    def test_Business(self):
        # Click Business Option
        b = BusinessPage(self.driver)
        b.business_page_option()
        # Click Overview Option
        c = BusinessPage(self.driver)
        c.overview_page_option()
        # Click Business Option
        b = BusinessPage(self.driver)
        b.business_page_option()
        # Click Solution Option
        d = BusinessPage(self.driver)
        d.solution_page_option()
        # Click Business Option
        b = BusinessPage(self.driver)
        b.business_page_option()
        # Click Success_Stories Option
        e = BusinessPage(self.driver)
        e.success_stories_page_option()
        # Click Region Field
        r = BusinessPage(self.driver)
        r.region_field()
        # Region Select
        r = BusinessPage(self.driver)
        r.region_select()
        # Industry Field
        i = BusinessPage(self.driver)
        i.industry_field()
        # Industry Select
        i = BusinessPage(self.driver)
        i.industry_select()
        # Objective Field
        i = BusinessPage(self.driver)
        i.objective_field()
        # Objective Select
        j = BusinessPage(self.driver)
        j.objective_select()
        # Click Business Option
        b = BusinessPage(self.driver)
        b.business_page_option()

        # Click Content Option
        f = BusinessPage(self.driver)
        f.content_page_option()
        # First Name
        f = BusinessPage(self.driver)
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
       # f.check_box()
       # f.checked()

