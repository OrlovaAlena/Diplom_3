import allure

from pages.header import Header
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from src.data import Data


class TestPersonalAccount:

    @allure.title('Проверка перехода к истории заказов')
    def test_navigate_to_order_history(self, driver):
        login_page = LoginPage(driver)
        header = Header(driver)
        personal_account = PersonalAccountPage(driver)
        login_page.open()
        login_page.authorize_user()
        header.click_account_button()
        personal_account.order_history_click()

        assert Data.ORDER_HISTORY_URL in personal_account.get_current_url()

    @allure.title('Проверка выхода из аккаунта через личный кабинет')
    def test_logout_with_button(self, driver):
        login_page = LoginPage(driver)
        header = Header(driver)
        personal_account = PersonalAccountPage(driver)
        login_page.open()
        login_page.authorize_user()
        header.click_account_button()
        personal_account.exit_from_account()

        assert personal_account.get_current_url() == LoginPage.URL
