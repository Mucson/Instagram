from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class MainPage(BasePage):

    button_not_now = (By.XPATH, "//button[text()='Не сейчас']")
    field_search = (By.XPATH, "//input[@placeholder = 'Поиск']")

    def _verify_page(self):
        self.on_this_page(self.field_search)

    def click_not_now_button(self):
        self.click_on(self.button_not_now)

    def type_in_search_field(self, text):
        self.type_in(self.field_search, text)

    def click_result(self, text):
        button = (By.XPATH, "//span[text()='{}']".format(text))
        self.click_on(button)