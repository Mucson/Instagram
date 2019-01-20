import configparser

from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Chrome(executable_path=r"C:\Users\chromedriver.exe")
    context.driver.implicitly_wait(10)

    parser = configparser.ConfigParser()
    parser.read("behave.ini")
    context.config = parser


def before_scenario(context, scenario):
    context.driver.delete_all_cookies()


#def after_all(context):
    #context.driver.quit()
