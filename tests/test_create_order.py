import allure

from data import ORDER_DATA
from helpers import create_order


class TestCreateOrder:

    @allure.title("Создание заказа с цветом BLACK")
    def test_create_order_with_black_color_returns_track(self):
        order_data = ORDER_DATA.copy()
        order_data["color"] = ["BLACK"]

        response = create_order(order_data)

        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Создание заказа с цветом GREY")
    def test_create_order_with_grey_color_returns_track(self):
        order_data = ORDER_DATA.copy()
        order_data["color"] = ["GREY"]

        response = create_order(order_data)

        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Создание заказа с двумя цветами")
    def test_create_order_with_both_colors_returns_track(self):
        order_data = ORDER_DATA.copy()
        order_data["color"] = ["BLACK", "GREY"]

        response = create_order(order_data)

        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Создание заказа без указания цвета")
    def test_create_order_without_color_returns_track(self):
        order_data = ORDER_DATA.copy()

        response = create_order(order_data)

        assert response.status_code == 201
        assert "track" in response.json()