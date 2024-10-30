import pytest

from selenium import webdriver

from pages.base_page import BasePage

# @pytest.mark.parametrize(params=['chrome', 'firefox'])
# @pytest.fixture()
# def browser(request):
#     # driver = None
#     if request.params == 'chrome':
#         driver = webdriver.Chrome()
#     else:
#         driver = webdriver.Firefox()
#
#     driver.get('https://stellarburgers.nomoreparties.site/')
#     yield driver
#     driver.quit()


@pytest.fixture(scope='function')
def driver():
    browser = webdriver.Chrome()
    browser.get(BasePage.URL)

    yield browser
    browser.quit()


# @pytest.fixture(params=['firefox', 'chrome'])
# def driver(request):
#     driver = None
#     if request.params == 'firefox':
#         options = webdriver.FirefoxOptions()
#         driver = webdriver.Firefox(options=options)
#         driver.maximize_window()
#     elif request.params == 'chrome':
#         options = Options()
#         options.add_argument("--no-sandbox")
#         driver = webdriver.Chrome(options=options)
#         driver.maximize_window()
#
#     driver.get(BasePage.URL)
#     yield driver
#     driver.quit()
