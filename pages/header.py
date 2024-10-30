from pages.base_page import BasePage

import allure

from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from src.data import Urls
from src.elements import Elements
from src.locators import MainPageLocators


class Header(BasePage):
    @allure.step('Кликнуть по кнопке "Личный кабинет"')
    def click_account_button(self):
        self.click_to_element(Elements.PERSONAL_ACCOUNT)
        self.wait_for_url(PersonalAccountPage.URL)

    def click_to_constructor_button(self):
        self.click_to_element(Elements.CONSTRUCTOR)

    def click_to_order_list_button(self):
        self.click_to_element(Elements.ORDER_LIST)
