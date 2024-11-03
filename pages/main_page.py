import allure

from pages.base_page import BasePage
from src.elements import Elements


class MainPage(BasePage):

    @allure.step('Открыть страницу')
    def open(self):
        self.open_page(BasePage.URL)

    @allure.step('Клик по ингредиенту')
    def click_to_ingredient(self):
        self.click_to_element(Elements.FLUORESCENT_BUN)
        self.wait_for_visible(Elements.MODAL_TITLE)

    @allure.step('Клик по кнопке закрытия модального окна')
    def click_close_button(self):
        self.click_to_element(Elements.MODAL_CLOSE_BUTTON)

    @allure.step('Ожидание завершения загрузки')
    def _wait_for_loading_ends(self):
        self.wait_for_invisibility(Elements.LOADING_ANIMATION)

    @allure.step('Закрыть модальное окно')
    def close_modal_window(self):
        self._wait_for_loading_ends()
        self.click_close_button()

    @allure.step('Проверить открытие модального окна')
    def check_if_modal_open(self):
        return self.find_element(Elements.MODAL).get_attribute('class')

    @allure.step('Добавить ингредиент в заказ')
    def add_ingredient_to_order(self):
        self.drag_and_drop_element(Elements.FLUORESCENT_BUN, Elements.ORDER)

    @allure.step('Проверить счетчик')
    def check_counter(self):
        return self.get_text(Elements.COUNTER_FLOUR_BUN)

    @allure.step('Клик на кнопку создания заказа')
    def create_order(self):
        self.click_to_element(Elements.CREATE_ORDER_BUTTON)

    @allure.step('Проверить наличие кнопки закрытия модального окна')
    def check_the_close_button(self):
        return self.find_element(Elements.MODAL_CLOSE_BUTTON)

    @allure.step('Проверить наличие заголовка модального окна с оформленным заказом')
    def check_the_order_create_sign(self):
        return self.find_element(Elements.ORDER_CREATED_SIGN)

    @allure.step('Получение номера заказа')
    def _get_order_number(self):
        self._wait_for_loading_ends()
        self.wait_for_invisibility(Elements.ORDER_NUMBER_DEFAULT)
        return self.get_text(Elements.ORDER_NUMBER)

    @allure.step('Создание заказа')
    def make_order(self):
        self.add_ingredient_to_order()
        self.create_order()
        return self._get_order_number()
