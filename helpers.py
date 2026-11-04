import random
import string
import requests
import allure

from data import CREATE_COURIER_URL, LOGIN_COURIER_URL


def generate_courier_data():
    login = ''.join(random.choices(string.ascii_lowercase, k=10))
    password = ''.join(random.choices(string.ascii_lowercase, k=10))
    first_name = ''.join(random.choices(string.ascii_lowercase, k=10))

    return {
        "login": login,
        "password": password,
        "firstName": first_name
    }


@allure.step("Создать курьера")
def create_courier(courier_data):
    return requests.post(
        CREATE_COURIER_URL,
        json=courier_data
    )


@allure.step("Авторизоваться под курьером")
def login_courier(login, password):
    return requests.post(
        LOGIN_COURIER_URL,
        json={
            "login": login,
            "password": password
        }
    )


@allure.step("Удалить курьера")
def delete_courier(courier_id):
    return requests.delete(f"{CREATE_COURIER_URL}/{courier_id}")


@allure.step("Создать заказ")
def create_order(order_data):
    from data import CREATE_ORDER_URL

    return requests.post(
        CREATE_ORDER_URL,
        json=order_data
    )


@allure.step("Получить список заказов")
def get_orders():
    from data import LIST_ORDERS_URL

    return requests.get(LIST_ORDERS_URL)


@allure.step("Зарегистрировать нового курьера")
def register_new_courier_and_return_login_password():
    courier_data = generate_courier_data()

    response = create_courier(courier_data)

    assert response.status_code == 201

    return courier_data

@allure.step("Авторизоваться без пароля")
def login_courier_without_password(login):
    return requests.post(
        LOGIN_COURIER_URL,
        json={"login": login}
    )