import allure

from pages.header import Header
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from src.data import Data
from src.requests_user_api import delete_user


class TestPersonalAccount:

    @allure.title('Проверка перехода к истории заказов')
    def test_navigate_to_order_history(self, driver):
        login_page = LoginPage(driver)
        header = Header(driver)
        personal_account = PersonalAccountPage(driver)
        login_page.open()
        access_token = login_page.authorize_user()
        header.click_account_button()
        personal_account.order_history_click()

        delete_user(access_token)

        assert Data.ORDER_HISTORY_URL in personal_account.get_current_url()

    @allure.title('Проверка выхода из аккаунта через личный кабинет')
    def test_logout_with_button(self, driver):
        login_page = LoginPage(driver)
        header = Header(driver)
        personal_account = PersonalAccountPage(driver)

        login_page.open()
        access_token = login_page.authorize_user()
        header.click_account_button()
        personal_account.exit_from_account()

        delete_user(access_token)

        assert personal_account.get_current_url() == LoginPage.URL
