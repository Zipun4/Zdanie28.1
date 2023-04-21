import pytest
import time
from selenium import webdriver


@pytest.fixture(autouse=True)
def browser():
    driver = webdriver.Chrome(executable_path='chrDrive.exe')

    yield driver
    driver.quit()
