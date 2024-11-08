import allure

from pages.base_page import BasePage
from src.elements import Elements
from src.urls import Url


class Header(BasePage):

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_account_button(self):
        self.click_to_element(Elements.PERSONAL_ACCOUNT)
        self.wait_for_url(Url.PERSONAL_ACCOUNT)

    @allure.step('Клик по кнопке "Конструктор"')
    def click_to_constructor_button(self):
        self.click_to_element(Elements.CONSTRUCTOR)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_to_order_list_button(self):
        self.click_to_element(Elements.ORDER_LIST)
        self.wait_for_visible(Elements.ORDER_HEADER_SIGN)
