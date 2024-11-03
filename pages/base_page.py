import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    URL = 'https://stellarburgers.nomoreparties.site/'

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание адреса страницы')
    def wait_for_url(self, url):
        return WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))

    @allure.step('Получить адрес страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Найти элемент')
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    @allure.step('Открыть страницу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
        self.wait_for_visible(locator)
        self.find_element(locator).click()

    @allure.step('Ожидание появления элемента')
    def wait_for_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Заполнить инпут')
    def fill_input(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получить аттрибут')
    def get_attribute(self, locator, attribute):
        self.find_element(*locator).get_attribute(attribute)

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source_locator, target_locator):
        source_element = self.find_element(source_locator)
        target_element = self.find_element(target_locator)
        action = ActionChains(self.driver).drag_and_drop(source_element, target_element)
        action.perform()

    @allure.step('Получить текст')
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step('Ожидание исчезновения элемента')
    def wait_for_invisibility(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.invisibility_of_element_located(locator))
