import allure

import requests

from pages.base_page import BasePage
from src.endpoints import API_URL, CREATE_USER, USER


@allure.step('Создать пользователя')
def create_user(user_data):
    return requests.post(API_URL + CREATE_USER, json=user_data)


@allure.step("Получить токен пользователя")
def get_access_token(user_response):
    return user_response.json().get("accessToken")


@allure.step("Удалить пользователя")
def delete_user(access_token):
    headers = {"Authorization": access_token}
    return requests.delete(BasePage.URL + USER, headers=headers)
