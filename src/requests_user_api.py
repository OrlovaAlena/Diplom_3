import allure
import requests

from pages.base_page import BasePage
from src.endpoints import USER


@allure.step("Удалить пользователя")
def delete_user(access_token):
    headers = {"Authorization": access_token}
    return requests.delete(BasePage.URL + USER, headers=headers)
