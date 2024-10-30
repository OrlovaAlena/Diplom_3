import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#
class BasePage:

    URL = 'https://stellarburgers.nomoreparties.site/'

    def __init__(self, driver):
        self.driver = driver

    def wait_for_url(self, url):
        return WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    # def wait_and_find_element(self, locator, timeout=5):
    #     WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
    #     return self.driver.find_element(*locator)

    def open_page(self, url):
        self.driver.get(url)

    # def is_element_present(self, locator, timeout=1):
    #     try:
    #         WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
    #         return True
    #     except TimeoutException:
    #         return False

    def click_to_element(self, locator):
        self.wait_for_visible(locator)
        self.find_element(locator).click()

    def wait_for_visible(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    def fill_input(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_attribute(self, locator, attribute):
        self.find_element(*locator).get_attribute(attribute)

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source_element, target_element):
        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_element).pause(5)
        action.perform()
#
#     def get_text(self, locator):
#         return self.find_element(locator).text
#
#     def scroll_page(self, locator):
#         element = self.find_element(locator)
#         self.driver.execute_script("arguments[0].scrollIntoView();", element)
#         self.wait_for_visible(locator)
