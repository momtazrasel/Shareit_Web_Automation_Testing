from Pages.ProductPage import ProductPage
from Tests.BasePage import BasePage


class Business(BasePage):

    def test_share_it(self):
        # Click Business Option
        b = ProductPage(self.driver)
        b.product_page_option()
        b.share_it()
        b.android()
        self.driver.quit()
