import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()