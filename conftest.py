import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.base_page import BasePage


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    driver = None
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
    elif request.param == 'chrome':
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()

    driver.get(BasePage.URL)
    yield driver
    driver.quit()
