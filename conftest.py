import pytest
import requests

from data import BASE_URL
from helpers import (
    register_new_courier_and_return_login_password,
    generate_courier_data
)


@pytest.fixture
def courier():
    courier_data = register_new_courier_and_return_login_password()

    response = requests.post(
        f"{BASE_URL}/api/v1/courier/login",
        json={
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
    )

    courier_id = response.json()["id"]

    yield courier_data

    requests.delete(f"{BASE_URL}/api/v1/courier/{courier_id}")


@pytest.fixture
def new_courier_data():
    courier_data = generate_courier_data()

    yield courier_data

    response = requests.post(
        f"{BASE_URL}/api/v1/courier/login",
        json={
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
    )

    if response.status_code == 200:
        courier_id = response.json()["id"]
        requests.delete(f"{BASE_URL}/api/v1/courier/{courier_id}")