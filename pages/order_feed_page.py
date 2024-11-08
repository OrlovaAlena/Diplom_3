import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from src.elements import Elements
from src.urls import Url


class OrderPage(BasePage):

    @allure.step('Открыть страницу заказа')
    def open(self):
        self.open_page(Url.ORDER)
        self.wait_for_visible(Elements.ORDER_HEADER_SIGN)

    @allure.step('Клик по карточке заказа в ленте')
    def click_order_card(self, order_num):
        self.click_to_element(self.find_order_card_by_order_num(order_num))

    @allure.step('Нахождение карточки заказа по номеру')
    def find_order_card_by_order_num(self, order_num):
        return By.XPATH, f'{Elements.ORDER_CARD}{order_num}{Elements.END}'

    @allure.step('Проверка открытия модального окна заказа')
    def check_order_modal_open(self):
        return self.find_element(Elements.MODAL_ORDER_DETAILS)

    @allure.step('Проверка номера заказа в модальном окне')
    def check_order_number_on_modal(self):
        return self.get_text(Elements.MODAL_ORDER_NUMBER)

    @allure.step('Проверка существования карточки на странице')
    def check_card_exists(self, order_num):
        return self.find_element(self.find_order_card_by_order_num(order_num))

    @allure.step('Получение данных счетчика заказов')
    def get_total_counter(self):
        return self.get_text(Elements.ALL_TIME_COUNTER)

    @allure.step('Получение данных счетчика заказов за день')
    def get_daily_counter(self):
        return self.get_text(Elements.DAY_COUNTER)

    @allure.step('Получение номера заказа из списка заказов в работе')
    def check_order_in_progress(self):
        self.wait_for_order()
        return self.get_text(Elements.ORDERS_IN_PROGRESS)

    @allure.step('Ожидание появления списка заказов в работе')
    def wait_for_order(self):
        return self.wait_for_invisibility(Elements.ALREADY_DONE)
