import allure

from pages.login_page import LoginPage
from pages.reset_page import ResetPasswordPage
from pages.restore_page import RestorePasswordPage


class TestForgotPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_navigate_by_restore_password_button(self, driver):
        login_page = LoginPage(driver)
        forgot_pass = RestorePasswordPage(driver)
        login_page.open()
        login_page.forgot_password_click()

        assert forgot_pass.get_current_url() == RestorePasswordPage.URL

    @allure.title('Ввод почты и клик по кнопке восстановления')
    def test_restore_password_with_email(self, driver):
        restore = RestorePasswordPage(driver)

        restore.open()
        restore.set_email()
        restore.click_restore_button()

        assert restore.get_current_url() == ResetPasswordPage.URL

    @allure.title('Клик по иконке показать/скрыть пароль делает поле активным')
    def test_activate_pass_field_by_the_eye_sign(self, driver):
        reset = ResetPasswordPage(driver)
        restore = RestorePasswordPage(driver)

        restore.open()
        restore.set_email()
        restore.click_restore_button()

        assert 'password' in reset.check_if_field_password_input_active()
        reset.eye_icon_click()
        assert 'text' in reset.check_if_field_password_input_active()
