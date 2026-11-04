import pytest

from helpers import (
    register_new_courier_and_return_login_password,
    generate_courier_data,
    login_courier,
    delete_courier
)


@pytest.fixture
def courier():
    courier_data = register_new_courier_and_return_login_password()

    response = login_courier(
        courier_data["login"],
        courier_data["password"]
    )

    courier_id = response.json()["id"]

    yield courier_data

    delete_courier(courier_id)


@pytest.fixture
def new_courier_data():
    courier_data = generate_courier_data()

    yield courier_data

    response = login_courier(
        courier_data["login"],
        courier_data["password"]
    )

    if response.status_code == 200:
        courier_id = response.json()["id"]
        delete_courier(courier_id)