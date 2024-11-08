import allure
from pages.base_page import BasePage
from src.elements import Elements
from src.urls import Url


class LoginPage(BasePage):

    @allure.step('Открыть страницу логина')
    def open(self):
        self.open_page(Url.LOGIN)

    @allure.step('Кликнуть на "Восстановить пароль"')
    def forgot_password_click(self):
        self.click_to_element(Elements.RESTORE_PASSWORD_BUTTON)
        self.wait_for_visible(Elements.RESTORE_PASSWORD_SIGN)

    @allure.step('Заполнение формы авторизации')
    def authorize_user(self, password, email):
        self.fill_input(Elements.PASSWORD_INPUT, password)
        self.fill_input(Elements.EMAIL_INPUT, email)
        self.click_to_element(Elements.CONFIRM_LOGIN_BUTTON)
        self.wait_for_url(Url.BASE_PAGE)
