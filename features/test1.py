import time

from selenium import webdriver

from features.pages.login_page import LoginPage
from features.pages.main_page import MainPage
from features.pages.search_results_page import SearchResultsPage

driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.instagram.com/accounts/login/")

login_page = LoginPage(driver)
login_page.enter_username("login-login")
login_page.enter_password("password")
login_page.click_login()

main_page = MainPage(driver)
main_page.click_not_now_button()
main_page.type_in_search_field("fitness")
main_page.click_result("#fitness")

search_result_page = SearchResultsPage(driver)