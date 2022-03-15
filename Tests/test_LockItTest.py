from Pages.ProductPage import ProductPage
from Tests.BasePage import BasePage


class Business(BasePage):

    def test_clone_it(self):
        # Click Product Option
        b = ProductPage(self.driver)
        b.product_page_option()
        b.lock_it()
        self.driver.quit()
       # b.lock_an()
