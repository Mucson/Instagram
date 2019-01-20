from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class SearchResultsPage(BasePage):
    label_top_posts = (By.XPATH, "//div[text() = 'Лучшие публикации']")

    def _verify_page(self):
        self.on_this_page(self.label_top_posts)

    def get_header_text(self):
        return self.get_text(self.label_top_posts)
