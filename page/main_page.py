from selenium.webdriver.support.wait import WebDriverWait

from conftest import browser
from .locators import LoginPageLocators
from .base_page import BasePage
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC




class MainPage(BasePage):
    def auth_page(self):
        iframe = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="fl-535861"]'))).click()
        browser.switch_to.frame(iframe)
        msg = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="close"]')))
        msg.click()

#        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
 #       self.browser.find_element(*LoginPageLocators.AUTH_BUTTON).send_keys(str('89653800019'))
#        self.browser.find_element(*LoginPageLocators.PASSWORD_BUTTON).send_keys(str('Test2020'))
 #       self.browser.find_element(*LoginPageLocators.ENTER_BUTTON).click()
