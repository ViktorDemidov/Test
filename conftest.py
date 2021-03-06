from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# @pytest.fixture()
# def get_chrome_options():
#options = chrome_options()
# options.add_argument('chrome') # Use headless if you do not need a browser UI
# options.add_argument('--start-maximized')
# options.add_argument('--windows-size=800,600')
# return options


@pytest.fixture()
def browser():
    browser = webdriver.Chrome("C:\chromedriver.exe")
    browser.maximize_window()
    browser.get("https://4lapy.ru/")
    yield browser
    browser.quit()
