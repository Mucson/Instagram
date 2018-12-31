from behave import when

from features.pages.main_page import MainPage


@when("I click now button")
def click_not_now_button(context):
    main_page = MainPage(context.driver)
    main_page.click_not_now_button()