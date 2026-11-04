import requests

from data import BASE_URL


class TestLoginCourier:

    def test_login_courier_success(self, courier):
        response = requests.post(
            f"{BASE_URL}/api/v1/courier/login",
            json={
                "login": courier["login"],
                "password": courier["password"]
            }
        )

        assert response.status_code == 200
        assert "id" in response.json()


    def test_login_courier_without_login_returns_error(self, courier):
        response = requests.post(
            f"{BASE_URL}/api/v1/courier/login",
            json={"password": courier["password"]}
        )

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"


    def test_login_courier_without_password_returns_error(self, courier):
        response = requests.post(
            f"{BASE_URL}/api/v1/courier/login",
            json={"login": courier["login"]}
        )

        assert response.status_code == 504

    
    def test_login_courier_with_wrong_password_returns_error(self, courier):
        response = requests.post(
            f"{BASE_URL}/api/v1/courier/login",
            json={
                "login": courier["login"],
                "password": "wrong_password_123"
            }
        )

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    def test_login_courier_with_nonexistent_login_returns_error(self):
        response = requests.post(
            f"{BASE_URL}/api/v1/courier/login",
            json={
                "login": "nonexistent_courier_123456",
                "password": "123456"
            }
        )

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"