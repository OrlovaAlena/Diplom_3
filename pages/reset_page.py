import allure

from pages.base_page import BasePage
from src.elements import Elements


class ResetPasswordPage(BasePage):

    URL = 'https://stellarburgers.nomoreparties.site/reset-password'

    @allure.step('Кликнуть на иконку')
    def eye_icon_click(self):
        self.click_to_element(Elements.EYE_ICON)

    @allure.step('Проверить активность поля ввода пароля')
    def check_if_field_password_input_active(self):
        return self.find_element(Elements.PASSWORD_INPUT).get_attribute('type')
