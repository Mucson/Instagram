from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class LoginPage(BasePage):
    field_username = (By.XPATH, "//input[@name='username']")
    field_password = (By.NAME, "password")
    button_login = (By.XPATH, "//button[@type='submit']")
    label_error = (By.ID, "slfErrorAlert")

    def _verify_page(self):
        self.on_this_page(self.field_username, self.field_password, self.button_login)

    def enter_username(self, username):
        self.type_in(self.field_username, username)

    def enter_password(self, password):
        self.type_in(self.field_password, password)

    def click_login(self):
        self.click_on(self.button_login)

    def get_error_text(self):
        return self.get_text(self.label_error)
