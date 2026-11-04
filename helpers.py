import random
import string
import requests

from data import BASE_URL


def generate_courier_data():
    login = ''.join(random.choices(string.ascii_lowercase, k=10))
    password = ''.join(random.choices(string.ascii_lowercase, k=10))
    first_name = ''.join(random.choices(string.ascii_lowercase, k=10))

    return {
        "login": login,
        "password": password,
        "firstName": first_name
    }


def register_new_courier_and_return_login_password():
    courier_data = generate_courier_data()

    response = requests.post(
        f"{BASE_URL}/api/v1/courier",
        json=courier_data
    )

    assert response.status_code == 201

    return courier_data