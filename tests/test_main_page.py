import allure

from pages.base_page import BasePage
from pages.header import Header
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_list_page import OrderListPage
from pages.personal_account_page import PersonalAccountPage


class TestMainPage:

    @allure.title('Проверка перехода в личный кабинет по кнопке')
    def test_navigate_to_personal_account_by_button(self, driver):
        login_page = LoginPage(driver)
        header = Header(driver)
        login_page.open()
        login_page.authorize_user()
        header.click_account_button()

        assert header.get_current_url() == PersonalAccountPage.URL

    def test_navigate_to_constructor(self, driver):
        login_page = LoginPage(driver)
        header = Header(driver)
        login_page.open()
        header.click_to_constructor_button()

        assert header.get_current_url() == BasePage.URL

    def test_navigate_to_order_list(self, driver):
        login_page = LoginPage(driver)
        header = Header(driver)
        login_page.open()
        header.click_to_order_list_button()

        assert header.get_current_url() == OrderListPage.URL

    def test_ingredient_modal_open(self, driver):
        main_page = MainPage(driver)
        main_page.clik_to_ingredient()

        assert 'open' in main_page.check_if_modal_open()
        assert main_page.get_ingredient_id_url() in BasePage.URL

    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.clik_to_ingredient()
        main_page.close_modal_window()

        assert 'open' not in main_page.check_if_modal_open()

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_counter_increase(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.authorize_user()

