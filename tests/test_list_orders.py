import allure

from helpers import get_orders


class TestListOrders:

    @allure.title("Получение списка заказов")
    def test_get_orders_list_returns_list(self):
        response = get_orders()

        assert response.status_code == 200
        assert isinstance(response.json()["orders"], list)