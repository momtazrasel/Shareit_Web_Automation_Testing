from Pages.ProductPage import ProductPage
from Tests.BasePage import BasePage


class Business(BasePage):

    def test_clean_it(self):
        # Click Business Option
        b = ProductPage(self.driver)
        b.product_page_option()
        b.clean_it()
        self.driver.quit()
        #b.android()
