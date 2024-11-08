import allure

from pages.header import Header
from pages.main_page import MainPage
from pages.order_feed_page import OrderPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderPage:

    @allure.title('Проверка открытия карточки заказа')
    def test_open_order_details(self, driver, create_user_and_delete):
        main_page = MainPage(driver)
        order_num = main_page.make_order()
        order_page = OrderPage(driver)
        order_page.open()
        order_page.click_order_card(order_num)

        assert order_page.check_order_modal_open()
        assert order_num in order_page.check_order_number_on_modal()

    @allure.title('Проверка отображения заказов из личного кабинета в общей ленте заказов')
    def test_order_from_history_list_is_on_order_feed_page(self, driver, create_user_and_delete):
        main_page = MainPage(driver)
        main_page.make_order()
        main_page.close_modal_window()
        header = Header(driver)
        header.click_account_button()
        personal_account = PersonalAccountPage(driver)
        personal_account.order_history_click()
        order_num_history = personal_account.get_order_number()
        order_page = OrderPage(driver)
        order_page.open()

        assert order_page.check_card_exists(order_num_history)

    @allure.title('Проверка увеличения общего счетчика после создания заказа')
    def test_total_counter_rises_after_order(self, driver, create_user_and_delete):
        order_page = OrderPage(driver)
        order_page.open()
        counter_before = order_page.get_total_counter()
        main_page = MainPage(driver)
        main_page.open()
        main_page.make_order()
        main_page.close_modal_window()
        order_page.open()
        counter_after = order_page.get_total_counter()

        assert counter_before < counter_after

    @allure.title('Проверка увеличения дневного счетчика после создания заказа')
    def test_daily_counter_rises_after_order(self, driver, create_user_and_delete):
        order_page = OrderPage(driver)
        order_page.open()
        counter_before = order_page.get_daily_counter()
        main_page = MainPage(driver)
        main_page.open()
        main_page.make_order()
        main_page.close_modal_window()
        order_page.open()
        counter_after = order_page.get_daily_counter()

        assert counter_before < counter_after

    @allure.title('Проверка попадания в список заказов в работе, после создания заказа')
    def test_order_get_to_in_progress_list(self, driver, create_user_and_delete):
        main_page = MainPage(driver)
        order_num = main_page.make_order()
        order_page = OrderPage(driver)
        order_page.open()

        assert order_page.check_order_in_progress() == '0' + order_num
