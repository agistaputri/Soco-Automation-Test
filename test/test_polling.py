import time
from selenium import webdriver
from pages.page_home import homePage
from pages.page_polling import pollingPage


def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()

def test_polling():
    home_page = homePage(driver)
    home_page.open_home_page("agistaputri20@gmail.com", "agistahidayatillah")
    time.sleep(5)
    home_page.menu_polling()
    time.sleep(3)
    polling_page = pollingPage(driver)
    polling_page.choose_pollingproduct()
    time.sleep(3)
    polling_page.input_question("Untuk oily skin bagus yang mana?")
    time.sleep(3)
    polling_page.input_product1("carasun cushion")
    time.sleep(3)
    polling_page.click_product1()
    time.sleep(3)
    polling_page.input_product2("neo cushion")
    time.sleep(3)
    polling_page.click_product2()
    time.sleep(3)
    polling_page.click_date()
    time.sleep(3)
    polling_page.click_enddate()
    time.sleep(3)
    polling_page.click_submit()
    time.sleep(5)

def test_teardown():
    driver.quit()
    

