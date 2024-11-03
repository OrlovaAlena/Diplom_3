from pages.base_page import BasePage

import allure

from pages.login_page import LoginPage
from pages.order_feed_page import OrderPage
from pages.personal_account_page import PersonalAccountPage
from src.elements import Elements


class Header(BasePage):

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_account_button(self):
        self.click_to_element(Elements.PERSONAL_ACCOUNT)
        self.wait_for_url(PersonalAccountPage.URL)

    @allure.step('Клик по кнопке "Конструктор"')
    def click_to_constructor_button(self):
        self.click_to_element(Elements.CONSTRUCTOR)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_to_order_list_button(self):
        self.click_to_element(Elements.ORDER_LIST)
        self.wait_for_visible(Elements.ORDER_HEADER_SIGN)
