from page.main_page import MainPage


def test_open_page(browser):
    page = MainPage(browser)
    page.auth_page()
