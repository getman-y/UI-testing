import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
