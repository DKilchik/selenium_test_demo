from pages.base_page import BasePage

def test_hello_world(browser):
    link = 'http://automationpractice.com'
    page = BasePage(browser, link)
    page.open()
    assert True