import configparser
import allure

from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
    context.driver.implicitly_wait(10)

    parser = configparser.ConfigParser()
    parser.read("behave.ini")
    context.config = parser


def before_scenario(context, scenario):
    context.driver.delete_all_cookies()


def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="screenshot",
                      attachment_type=allure.attach_type.PNG)


def after_all(context):
    context.driver.quit()
