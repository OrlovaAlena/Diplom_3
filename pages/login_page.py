import allure
from pages.base_page import BasePage
from src import helper
from src.elements import Elements


class LoginPage(BasePage):

    URL = 'https://stellarburgers.nomoreparties.site/login'

    @allure.step('Создание пользователя')
    def create_user(self):
        return helper.create_new_user()

    @allure.step('Открыть страницу логина')
    def open(self):
        self.open_page(self.URL)

    @allure.step('Кликнуть на "Восстановить пароль"')
    def forgot_password_click(self):
        self.click_to_element(Elements.RESTORE_PASSWORD_BUTTON)
        self.wait_for_visible(Elements.RESTORE_PASSWORD_SIGN)

    @allure.step('Авторизация пользователя')
    def authorize_user(self):
        data = self.create_user()
        self.fill_input(Elements.PASSWORD_INPUT, data[1])
        self.fill_input(Elements.EMAIL_INPUT, data[0])
        self.click_to_element(Elements.CONFIRM_LOGIN_BUTTON)
        self.wait_for_url(BasePage.URL)
