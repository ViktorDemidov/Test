from page.main_page import MainPage
import pytest



def test_open_page(browser):
    link = 'https://4lapy.ru/'
    page = MainPage(browser, link)
    page.auth_page()
