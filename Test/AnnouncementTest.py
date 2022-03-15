from Pages.ProductPage import ProductPage
from Pages.SRC_Page import SRCPage
from Tests.BasePage import BasePage


class Business(BasePage):

    def test_announcement(self):
        # Click Business Option
        b = SRCPage(self.driver)
        b.src()
        b.announcement_src()
        b = ProductPage(self.driver)
        b.language()
