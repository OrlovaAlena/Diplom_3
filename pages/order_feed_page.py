import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.main_page import MainPage
from src.elements import Elements


class OrderPage(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/feed'

    @allure.step('Открыть страницу заказа')
    def open(self):
        self.open_page(self.URL)
        self.wait_for_visible(Elements.ORDER_HEADER_SIGN)

    def click_order_card(self, order_num):
        self.click_to_element(self.find_order_card_by_order_num(order_num))

    def find_order_card_by_order_num(self, order_num):
        return By.XPATH, f'{Elements.ORDER_CARD}{order_num}{Elements.END}'

    def check_order_modal_open(self):
        return self.find_element(Elements.MODAL_ORDER_DETAILS)

    def check_order_number_on_modal(self):
        return self.get_text(Elements.MODAL_ORDER_NUMBER)

    def check_card_exists(self, order_num):
        return self.find_element(self.find_order_card_by_order_num(order_num))

    def get_total_counter(self):
        return self.get_text(Elements.ALL_TIME_COUNTER)

    def get_daily_counter(self):
        return self.get_text(Elements.DAY_COUNTER)

    def check_order_in_progress(self):
        return self.get_text(Elements.ORDERS_IN_PROGRESS)

    def wait_for_order(self):
        return self.wait_for_invisibility(Elements.ALREADY_DONE)
