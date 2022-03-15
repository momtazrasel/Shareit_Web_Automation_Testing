# import time
from Pages.BusinessPage import BusinessPage
# from Pages.OverviewPage import OverviewPage
from Tests.BasePage import BasePage


class Overview(BasePage):

    def test_Solution(self):
        a = BusinessPage(self.driver)
        a.business_page_option()
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
        self.driver.quit()
