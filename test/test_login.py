import time
from selenium import webdriver
from pages.page_login import loginPage

def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()


def test_login(driver, username, password):
    login_page = loginPage(driver)
    login_page.open_page("https://www.soco.id")
    time.sleep(5)
    login_page.click_login()
    time.sleep(3)
    login_page.enter_username(username)
    time.sleep(5)
    login_page.enter_password(password)
    time.sleep(5)
    login_page.click_submit()
    time.sleep(5)

def test_teardown():
    driver.quit()
