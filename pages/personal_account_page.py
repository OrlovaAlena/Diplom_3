import allure

from pages.base_page import BasePage
from src.elements import Elements


class PersonalAccountPage(BasePage):

    URL = 'https://stellarburgers.nomoreparties.site/account/profile'

    @allure.step('Открыть страницу логина')
    def open(self):
        self.open_page(self.URL)
        # self.wait_for_visible()

    def order_history_click(self):
        self.click_to_element(Elements.ORDER_HISTORY)

    def exit_from_account(self):
        self.click_to_element(Elements.EXIT)
        self.wait_for_visible(Elements.CONFIRM_LOGIN_BUTTON)

    def get_order_number(self):
        return self.get_text(Elements.FIRST_ORDER_NUM)
