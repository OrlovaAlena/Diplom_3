import allure

from pages.base_page import BasePage
from src.elements import Elements


class PersonalAccountPage(BasePage):

    @allure.step('Клик на кнопку истории заказов')
    def order_history_click(self):
        self.click_to_element(Elements.ORDER_HISTORY)

    @allure.step('Выход из аккаунта')
    def exit_from_account(self):
        self.click_to_element(Elements.EXIT)
        self.wait_for_visible(Elements.CONFIRM_LOGIN_BUTTON)

    @allure.step('Получение номера заказа')
    def get_order_number(self):
        return self.get_text(Elements.FIRST_ORDER_NUM)
