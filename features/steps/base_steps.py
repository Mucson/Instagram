from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from behave import *

from features.pages.base_page import BasePage


@step('I click element with text "{text}"')
def step_impl(context, text):
    WebDriverWait(context.driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, "//*[text()] = '{}'".format(text)))).click()


@step('I see element with text "{text}"')
def step_impl(context, text):
    base_page = BasePage(context.driver)
    base_page.see_element_with_text(text)
