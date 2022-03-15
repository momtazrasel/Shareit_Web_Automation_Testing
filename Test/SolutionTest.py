# import time
from Pages.BusinessPage import BusinessPage
from Pages.OverviewPage import OverviewPage
from Tests.BasePage import BasePage


class Overview(BasePage):

    def test_Solution(self):
        a = BusinessPage(self.driver)
        a.business_page_option()
        b = BusinessPage(self.driver)
        b.solution_page_option()
