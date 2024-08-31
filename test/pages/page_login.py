from selenium.webdriver.common.by import By

class loginPage():
    def __init__(self, driver):
        self.driver = driver
        self.login_button = (By.CLASS_NAME, 'login-mobile__button')
        self.username_textbox = (By.ID, 'username')
        self.password_textbox = (By.XPATH, '//*[@id="form-login"]/div[2]/div/input')
        self.submit_button = (By.CLASS_NAME, 'formaction')

    def open_page(self, url):
        self.driver.get(url)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
    
    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()


