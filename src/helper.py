import requests

from pages.base_page import BasePage
from src.data import Data
from src.endpoints import CREATE_USER

import random
import string


def generate_random_string(n):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(n))
    return random_string


def create_new_user():
    name = generate_random_string(8)
    email = generate_random_string(7) + Data.EMAIL
    password = generate_random_string(6)

    login_pass = []

    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(BasePage.URL + CREATE_USER, data=payload)
    if response.status_code == 200:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(name)
        token = response.json()['accessToken']
        login_pass.append(token)

    return login_pass
