
BASE_URL = "https://qa-scooter.praktikum-services.ru"

CREATE_COURIER_URL = f"{BASE_URL}/api/v1/courier"
LOGIN_COURIER_URL = f"{BASE_URL}/api/v1/courier/login"
CREATE_ORDER_URL = f"{BASE_URL}/api/v1/orders"
LIST_ORDERS_URL = f"{BASE_URL}/api/v1/orders"

ORDER_DATA = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": "Москва, Ленина, 10",
    "metroStation": 4,
    "phone": "+7 800 555-35-35",
    "rentTime": 5,
    "deliveryDate": "2026-11-10",
    "comment": "Тестовый заказ"
}
