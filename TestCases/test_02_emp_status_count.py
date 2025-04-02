import time
import pytest
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import Dashboard
from selenium.webdriver import ActionChains
from PageObjects.EmployeeStatusPage import EmpStatus
from Utilities.logger import logclass
import configparser
config = configparser.ConfigParser()
config.read("Utilities/inputs.properties")

@pytest.mark.usefixtures("setup")
class Testempstatus:
    def test_04(self):
        lg = Login(self.driver)
        db = Dashboard(self.driver)
        es = EmpStatus(self.driver)
        lg.input_username(config.get("credential","correct_username"))
        lg.input_password(config.get("credential","correct_password"))
        lg.click_button()
        # ActionChains(self.driver).move_to_element(db.hover_admin()).perform()
        db.hover_admin()
        time.sleep(5)
        # ActionChains(self.driver).move_to_element(db.hover_job()).perform()
        db.hover_job()
        time.sleep(5)
        # ActionChains(self.driver).move_to_element(db.hover_emp_status()).click()
        db.hover_emp_status()
        time.sleep(2)
        es.click_add_status_button()
        es.input_new_status("Automation")
        es.click_save_button()