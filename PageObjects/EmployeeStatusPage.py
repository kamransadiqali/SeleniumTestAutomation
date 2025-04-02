from selenium.webdriver.common.by import By

class EmpStatus:
    def __init__(self,driver):
        self.driver = driver

        self.button_addstatus_xpath = "//button[normalize-space()='Add']"
        self.input_name_xpath = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
        self.button_save_xpath = "//button[normalize-space()='Save']"

    def click_add_status_button(self):
        self.driver.find_element(By.XPATH, self.button_addstatus_xpath).click()
    def input_new_status(self, Name):
        self.driver.find_element(By.XPATH, self.input_name_xpath).send_keys(Name)
    def click_save_button(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()