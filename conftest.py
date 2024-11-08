import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from src.helper import create_new_user
from src.requests_user_api import delete_user
from src.urls import Url


@pytest.fixture(params=['chrome'])
def driver(request):
    driver = None
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        # options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
    elif request.param == 'chrome':
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()

    driver.get(Url.BASE_PAGE)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def create_user_and_delete(driver):
    data = create_new_user()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.authorize_user(data[1], data[0])
    token = data[3]
    yield
    delete_user(token)
