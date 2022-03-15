from Pages.SRC_Page import SRCPage
from Tests.BasePage import BasePage


class Business(BasePage):

    def test_overview(self):
        # Click Business Option
        b = SRCPage(self.driver)
        b.src()
        b.overview_src()
        self.driver.quit()