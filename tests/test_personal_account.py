import allure

from pages.header import Header
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from src.urls import Url


class TestPersonalAccount:

    @allure.title('Проверка перехода к истории заказов')
    def test_navigate_to_order_history(self, driver, create_user_and_delete):
        login_page = LoginPage(driver)
        header = Header(driver)
        personal_account = PersonalAccountPage(driver)
        login_page.open()
        header.click_account_button()
        personal_account.order_history_click()

        assert Url.ORDER_HISTORY in personal_account.get_current_url()

    @allure.title('Проверка выхода из аккаунта через личный кабинет')
    def test_logout_with_button(self, driver, create_user_and_delete):
        header = Header(driver)
        personal_account = PersonalAccountPage(driver)
        header.click_account_button()
        personal_account.exit_from_account()

        assert personal_account.get_current_url() == Url.LOGIN
