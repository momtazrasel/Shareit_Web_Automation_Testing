from Pages.ProductPage import ProductPage
from Tests.BasePage import BasePage


class Business(BasePage):

    def test_clone_it(self):
        # Click Business Option
        b = ProductPage(self.driver)
        b.product_page_option()
        b.clone_it()
        #b.android()
