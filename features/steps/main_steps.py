from behave import when

from features.pages.main_page import MainPage


@when("I click now button")
def click_not_now_button(context):
    main_page = MainPage(context.driver)
    main_page.click_not_now_button()


@when("I enter text in search field")
def enter_text_in_search_field(context):
    main_page = MainPage(context.driver)
    main_page.type_in_search_field("fitness")
    main_page.click_result("#fitness")
