import requests

from data import BASE_URL


class TestCreateCourier:

    def test_create_courier_success(self, new_courier_data):
        response = requests.post(
            f"{BASE_URL}/api/v1/courier",
            json=new_courier_data
        )

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    def test_create_courier_duplicate_login_returns_error(self, courier):
        response = requests.post(
            f"{BASE_URL}/api/v1/courier",
            json=courier
        )

        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."    

    def test_create_courier_without_login_returns_error(self, new_courier_data):
        courier_data = new_courier_data.copy()
        del courier_data["login"]

        response = requests.post(
            f"{BASE_URL}/api/v1/courier",
            json=courier_data
        )

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"    

    def test_create_courier_without_password_returns_error(self, new_courier_data):
        courier_data = new_courier_data.copy()
        del courier_data["password"]

        response = requests.post(
            f"{BASE_URL}/api/v1/courier",
            json=courier_data
        )

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"    

    
    def test_create_courier_without_first_name_success(self, new_courier_data):
        courier_data = new_courier_data.copy()
        del courier_data["firstName"]

        response = requests.post(
            f"{BASE_URL}/api/v1/courier",
            json=courier_data
        )

        assert response.status_code == 201
        assert response.json() == {"ok": True}    