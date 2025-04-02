import pytest
from selenium import webdriver
import configparser
config = configparser.ConfigParser()
config.read("Utilities/inputs.properties")


@pytest.fixture
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    request.cls.driver = webdriver.Chrome(options=options)
    request.cls.driver.get(config.get("Url","base_url"))
    request.cls.driver.implicitly_wait(2)
    yield
    request.cls.driver.quit()