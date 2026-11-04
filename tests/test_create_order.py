import pytest
import requests

from data import BASE_URL, ORDER_DATA


class TestCreateOrder:

    @pytest.mark.parametrize(
        "color",
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            None
        ]
    )
    def test_create_order_with_different_colors_returns_track(self, color):
        order_data = ORDER_DATA.copy()

        if color is not None:
            order_data["color"] = color

        response = requests.post(
            f"{BASE_URL}/api/v1/orders",
            json=order_data
        )

        assert response.status_code == 201
        assert "track" in response.json()