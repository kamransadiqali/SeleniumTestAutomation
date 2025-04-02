from selenium.webdriver.common.by import By

class Login:
    def __init__(self,driver):
        self.driver = driver

        self.text_username_xpath = "//input[@placeholder='Username']"
        self.text_password_xpath = "//input[@placeholder='Password']"
        self.button_login_xpath = "//button[normalize-space()='Login']"
        self.text_invalid_xpath = "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"

    def input_username(self, Username):
        self.driver.find_element(By.XPATH, self.text_username_xpath).send_keys(Username)
    def input_password(self, Password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(Password)
    def click_button(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
    def invalid_message(self):
        return self.driver.find_element(By.XPATH, self.text_invalid_xpath).text


