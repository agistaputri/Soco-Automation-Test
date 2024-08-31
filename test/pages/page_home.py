from selenium.webdriver.common.by import By
from test_login import test_login

class homePage():
    def __init__(self, driver):
        self.driver = driver
        self.uploadphoto_button = (By.XPATH, '//*[@id="v-photo-poll-1"]')
        self.collection_button = (By.XPATH, '//*[@id="v-photo-poll-2"]')
        self.review_button = (By.XPATH, '//*[@id="rootContainer"]/div/div[2]/div/div[2]/div[1]/ul/li[3]')
        self.polling_button = (By.XPATH, '//*[@id="v-photo-poll-0"]/a')
    
    
    def open_home_page(self, username, password):
        test_login(self.driver, username, password)
        # After logging in, navigate to the home page
        # driver.get("https://example.com/home")
        
    def menu_polling(self):
        self.driver.find_element(*self.polling_button).is_displayed
        self.driver.find_element(*self.polling_button).click()
    
    
    