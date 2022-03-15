from Pages.ProductPage import ProductPage
from Tests.BasePage import BasePage


class Business(BasePage):

    def test_listen_it(self):
        # Click Business Option
        b = ProductPage(self.driver)
        b.product_page_option()
        b.lis_it()
        self.driver.quit()
        #b.android()
