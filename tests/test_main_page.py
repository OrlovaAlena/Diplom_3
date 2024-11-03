import allure

from pages.base_page import BasePage
from pages.header import Header
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderPage
from pages.personal_account_page import PersonalAccountPage
from src.requests_user_api import delete_user


class TestMainPage:

    @allure.title('Переход в личный кабинет по кнопке')
    def test_navigate_to_personal_account_by_button(self, driver):
        login_page = LoginPage(driver)
        header = Header(driver)
        login_page.open()
        access_token = login_page.authorize_user()
        header.click_account_button()

        delete_user(access_token)

        assert header.get_current_url() == PersonalAccountPage.URL

    @allure.title('Переход на страницу конструктора по кнопке')
    def test_navigate_to_constructor(self, driver):
        login_page = LoginPage(driver)
        header = Header(driver)
        login_page.open()
        header.click_to_constructor_button()

        assert header.get_current_url() == BasePage.URL

    @allure.title('Переход на страницу ленты заказов по кнопке')
    def test_navigate_to_order_list(self, driver):
        header = Header(driver)
        header.click_to_order_list_button()

        assert header.get_current_url() == OrderPage.URL

    @allure.title('При клике на ингредиент открывается модальное окно с деталями')
    def test_ingredient_modal_open(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_ingredient()

        assert 'opened' in main_page.check_if_modal_open()

    @allure.title('Модальное окно закрывается по клику на крестик')
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_ingredient()
        main_page.click_close_button()

        assert 'opened' not in main_page.check_if_modal_open()

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер ингредиента')
    def test_counter_increase(self, driver):
        main_page = MainPage(driver)
        count_before = main_page.check_counter()
        main_page.add_ingredient_to_order()
        count_after = main_page.check_counter()

        assert count_before == '0'
        assert count_before < count_after

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_create_order_with_authorized_user(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        access_token = login_page.authorize_user()
        main_page = MainPage(driver)
        main_page.add_ingredient_to_order()
        main_page.create_order()

        delete_user(access_token)

        assert main_page.check_the_order_create_sign() and main_page.check_the_close_button()
