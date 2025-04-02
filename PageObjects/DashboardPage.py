from selenium.webdriver.common.by import By

class Dashboard:
    def __init__(self,driver):
        self.driver = driver

        self.text_dashboard_xpath = "//h6[normalize-space()='Dashboard']"
        self.button_admin_xpath = "//a[@class='oxd-main-menu-item active']"
        self.button_job_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[2]/span[1]"
        self.button_employment_status_xpath = "//a[normalize-space()='Employment Status']"

    def wellcome_msg(self):
        return self.driver.find_element(By.XPATH, self.text_dashboard_xpath).text
    def hover_admin(self):
        self.driver.find_element(By.XPATH, self.button_admin_xpath).click()
    def hover_job(self):
        self.driver.find_element(By.XPATH, self.button_job_xpath).click()
    def hover_emp_status(self):
        self.driver.find_element(By.XPATH, self.button_employment_status_xpath).click()
