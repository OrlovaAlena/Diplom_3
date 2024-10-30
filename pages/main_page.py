# import allure
# from pages.base_page import BasePage
# from src.elements import Elements
#
#
# class MainPage(BasePage):
#
#
#     @allure.step("Открыть в браузере страницу 'Stellar Burger'")
#     def open(self, url):
#         self.open_page(url)


from pages.base_page import BasePage
#
import allure

from pages.personal_account_page import PersonalAccountPage
from src.data import Urls
from src.elements import Elements
from src.locators import MainPageLocators


class MainPage(BasePage):

    def clik_to_ingredient(self):
        self.click_to_element(Elements.FLUORESCENT_BUN)
        self.wait_for_visible(Elements.MODAL_TITLE)

    def get_ingredient_id_url(self):
        return self.get_attribute(Elements.FLUORESCENT_BUN, 'href')

    def close_modal_window(self):
        self.click_to_element(Elements.MODAL_CLOSE_BUTTON)

    def check_if_modal_open(self):
        return self.find_element(Elements.MODAL).get_attribute('class')

    def add_ingredient_to_order(self):
        self.drag_and_drop_element(Elements.FLUORESCENT_BUN,Elements.ORDER)



