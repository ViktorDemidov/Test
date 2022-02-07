from selenium.webdriver.common.by import By


class LoginPageLocators:
    BANNER_DISCOUNT = (By.XPATH, "//button[@class='close']")
    LOGIN_BUTTON = (By.XPATH, "//span[text()='Войти']")
    AUTH_BUTTON = (By.XPATH, "//input[@id='tel-email-authorization']")
    PASSWORD_BUTTON = (By.XPATH, "//input[@id='password-authorization']")
    ENTER_BUTTON = (By.XPATH, "//button[@id='websiteElement-authorization-loginButton']")
