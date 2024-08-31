from selenium.webdriver.common.by import By

class pollingPage():
    def __init__(self, driver):
        self.driver = driver
        self.polling_product = (By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div[2]/div/a[1]')
        self.polling_textgambar = (By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div[2]/div/a[2]')
        self.question_textbox = (By.XPATH, '//*[@id="question"]')
        self.product1 = (By.XPATH, '//*[@id="form-journal"]/div[2]/div[2]/div/ul/li[1]/div[2]/input')
        self.product2 = (By.XPATH, '//*[@id="form-journal"]/div[2]/div[2]/div/ul/li[2]/div[2]/input')
        self.search_result1 = (By.XPATH, '//*[@id="form-journal"]/div[2]/div[2]/div/ul/li[1]/div[3]')
        self.search_result2 = (By.XPATH, '//*[@id="form-journal"]/div[2]/div[2]/div/ul/li[2]/div[3]')
        self.date = (By.XPATH, '//*[@id="dateEndCheck"]/div/div[1]/input')
        self.enddate = (By.XPATH, '//*[@id="dateEndCheck"]/div/div[2]/div/span[39]')
        self.submit_button = (By.XPATH, '//*[@id="form-journal"]/div[2]/div[4]/div[2]/input')

    def choose_pollingproduct(self):
        self.driver.find_element(*self.polling_product).click()
    
    def choose_pollingtextgambar(self):
        self.driver.find_element(*self.polling_textgambar).click()
    
    def input_question(self, question):
        self.driver.find_element(*self.question_textbox).send_keys(question)
    
    def input_product1(self, product1):
        self.driver.find_element(*self.product1).send_keys(product1)
    
    def input_product2(self, product2):
        self.driver.find_element(*self.product2).send_keys(product2)
    
    def click_product1(self):
        self.driver.find_element(*self.search_result1).click()
    
    def click_product2(self):
        self.driver.find_element(*self.search_result2).click()
    
    def click_date(self):
        self.driver.find_element(*self.date).click()
    
    def click_enddate(self):
        self.driver.find_element(*self.enddate).click()

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()


    

    
