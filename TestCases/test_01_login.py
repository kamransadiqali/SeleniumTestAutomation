import pytest
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import Dashboard
from Utilities.logger import logclass
import configparser
config = configparser.ConfigParser()
config.read("Utilities/inputs.properties")


@pytest.mark.usefixtures("setup")
class Testlogin(logclass):
    def test_01(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        log.info("Test Case 01")
        log.info("Test Case 1 Starting")
        # lg.input_username("Admin")
        lg.input_username(config.get("credential","correct_username"))
        log.info("Enter UserName")
        lg.input_password(config.get("credential", "correct_password"))
        log.info("Enter Password")
        lg.click_button()
        db = Dashboard(self.driver)
        if 'Dashboard' in db.wellcome_msg():
            assert True
            log.info("Test Case Pass")
        else:
            self.driver.save_screenshot('Screenshots/test_01.png')
            log.critical("Test Case 1 Fail")
            assert False

    def test_02(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        log.info("Test Case 02")
        log.info("Test Case 2 Starting")
        # lg.input_username("dmin")
        lg.input_username(config.get("credential", "incorrect_correct_username"))
        log.info("Enter Wrong UserName")
        lg.input_password(config.get("credential", "incorrect_correct_password"))
        log.info("Enter Wrong Password")
        lg.click_button()
        # if 'Invalid credentials' in self.driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text:
        if 'Invalid credentials' in lg.invalid_message():

            assert True
        else:
            self.driver.save_screenshot('Screenshots/test_02.png')
            log.critical("Test Case 2 Fail")
            assert False

    def test_03(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        log.info("Test Case 03")
        log.info("Test Case 3 Starting")
        lg.input_username(config.get("credential", "incorrect_correct_username"))
        log.info("Enter UserName")
        lg.input_password(config.get("credential", "incorrect_correct_password"))
        log.info("Enter Password")
        lg.click_button()
        if 'test message' in lg.invalid_message():
            assert True
        else:
            self.driver.save_screenshot('Screenshots/test_02.png')
            log.critical("Test Case 3 Fail")
            assert False
