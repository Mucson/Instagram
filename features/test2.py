import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://vk.com/login")

field_username = driver.find_element_by_id("email")
field_password = driver.find_element_by_id("pass")

button_login = driver.find_element_by_id("login_button")


def enter_username(text):
    field_username.clear()
    field_username.send_keys(text)


def enter_password(text):
    field_password.clear()
    field_password.send_keys(text)


def click_login():
    button_login.click()


def verifity_allert__for(username, password):
    enter_username(username)
    enter_password(password)
    time.sleep(1)


verifity_allert__for("pyautomation", "1234asd")
verifity_allert__for("as2224", "1234xcff")
verifity_allert__for("login24", "12341s")
verifity_allert__for("try777", "1234234")

driver.quit()
