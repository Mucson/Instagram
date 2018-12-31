from behave import step, when, then

from features.pages.base_page import BasePage
from features.pages.login_page import LoginPage


@step("I open login page")
def step_impl(context):
    context.driver.get("https://www.instagram.com/accounts/login/")


@step('I type "{username}" in username field')
def step_impl(context, username):
    login_page = LoginPage(context.driver)
    login_page.enter_username(username)


@when('I type "{password}" in password field')
def step_impl(context, password):
    login_page = LoginPage(context.driver)
    login_page.enter_password(password)


@when("I click login button")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_login()


@when("I log in")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.enter_username(context.config.get("user", "username"))
    login_page.enter_password(context.config.get("user", "password"))
    login_page.click_login()


@then('I see validation for message "{text}"')
def step_impl(context, text):
    login_page = LoginPage(context.driver)
    for row in context.table:
        login_page.enter_username(row["username"])
        login_page.enter_password(row["password"])
        login_page.click_login()
        base_page = BasePage(context.driver)
        base_page.see_element_with_text(text)
