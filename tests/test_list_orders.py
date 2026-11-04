import requests

from data import BASE_URL


class TestListOrders:

    def test_get_orders_list_returns_list(self):
        response = requests.get(f"{BASE_URL}/api/v1/orders")

        assert response.status_code == 200
        assert isinstance(response.json()["orders"], list)