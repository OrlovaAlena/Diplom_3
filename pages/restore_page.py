import allure

from pages.base_page import BasePage
from src.data import Data
from src.elements import Elements


class RestorePasswordPage(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/forgot-password'

    @allure.step('Открыть страницу восстановления пароля')
    def open(self):
        self.open_page(self.URL)

    @allure.step("Ввести почту в поле email")
    def set_email(self):
        input_email = self.wait_for_visible(Elements.EMAIL_INPUT)
        input_email.send_keys(Data.USER_EMAIL)

    @allure.step('Кликнуть по кнопке "Восстановить"')
    def click_restore_button(self):
        self.click_to_element(Elements.RESTORE_BUTTON)
        self.wait_for_visible(Elements.CONFIRM_BUTTON)
