import allure
import time

from pages.base_page import BasePage
from src import requests_user_api
from src.elements import Elements


class MainPage(BasePage):

    def open(self):
        self.open_page(BasePage.URL)

    def click_to_ingredient(self):
        self.click_to_element(Elements.FLUORESCENT_BUN)
        self.wait_for_visible(Elements.MODAL_TITLE)

    def click_close_button(self):
        self.click_to_element(Elements.MODAL_CLOSE_BUTTON)

    def close_modal_window(self):
        self.wait_for_loading_end()
        self.click_close_button()

    def check_if_modal_open(self):
        return self.find_element(Elements.MODAL).get_attribute('class')

    def add_ingredient_to_order(self):
        self.drag_and_drop_element(Elements.FLUORESCENT_BUN, Elements.ORDER)

    def check_counter(self):
        return self.get_text(Elements.COUNTER_FLOUR_BUN)

    def create_order(self):
        self.click_to_element(Elements.CREATE_ORDER_BUTTON)

    def check_the_close_button(self):
        return self.find_element(Elements.MODAL_CLOSE_BUTTON)

    def check_the_order_create_sign(self):
        return self.find_element(Elements.ORDER_CREATED_SIGN)

    def wait_for_order_num(self):
        self.wait_for_invisibility(Elements.ORDER_NUMBER_DEFAULT)

    def get_order_number(self):
        self.wait_for_loading_end()
        self.wait_for_order_num()
        return self.get_text(Elements.ORDER_NUMBER)

    def wait_for_loading_end(self):
        self.wait_for_invisibility(Elements.LOADING_ANIMATION)

    def make_order(self):
        self.add_ingredient_to_order()
        self.create_order()
        return self.get_order_number()
