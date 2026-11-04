import allure

from helpers import create_courier


class TestCreateCourier:

    @allure.title("Создание курьера с корректными данными")
    def test_create_courier_success(self, new_courier_data):
        response = create_courier(new_courier_data)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Создание курьера с уже существующим логином")
    def test_create_courier_duplicate_login_returns_error(self, courier):
        response = create_courier(courier)

        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Создание курьера без логина")
    def test_create_courier_without_login_returns_error(self, new_courier_data):
        courier_data = new_courier_data.copy()
        del courier_data["login"]

        response = create_courier(courier_data)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Создание курьера без пароля")
    def test_create_courier_without_password_returns_error(self, new_courier_data):
        courier_data = new_courier_data.copy()
        del courier_data["password"]

        response = create_courier(courier_data)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Создание курьера без имени")
    def test_create_courier_without_first_name_success(self, new_courier_data):
        courier_data = new_courier_data.copy()
        del courier_data["firstName"]

        response = create_courier(courier_data)

        assert response.status_code == 201
        assert response.json() == {"ok": True}