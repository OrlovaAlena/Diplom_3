# import allure
# import helper
# from data import Urls
# import requests
#
# from src.endpoints import API_URL, CREATE_USER
#
#
# @allure.step('Создать данные для пользователя')
# def create_user_data():
#     return helper.generate_random_string(6)
#
#
# @allure.step('Создать пользователя')
# def create_user(user_data):
#     return requests.post(API_URL + CREATE_USER, json=user_data)
#
#
# @allure.step("Получить токен пользователя")
# def get_access_token(user_response):
#     return user_response.json().get("accessToken")
#
#
# @allure.step("Удалить пользователя")
# def delete_user(access_token):
#     headers = {"Authorization": access_token}
#     return requests.delete(Urls.BASE_URL + Urls.DELETE_USER_ENDPOINT, headers=headers)
