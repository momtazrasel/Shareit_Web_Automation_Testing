from Pages.NewsRoomPage import NewsRoomPage
from Tests.BasePage import BasePage


class Business(BasePage):

    def test_newsroom(self):
        # Click Business Option
        b = NewsRoomPage(self.driver)
        b.newsroom()
        b.click_all_option()
        b.click_one_post()
        b.click_twitter()
        #b.android()
        self.driver.quit()