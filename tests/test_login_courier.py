import allure

from helpers import login_courier, login_courier_without_password


class TestLoginCourier:

    @allure.title("Авторизация курьера с корректными данными")
    def test_login_courier_success(self, courier):
        response = login_courier(
            courier["login"],
            courier["password"]
        )

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Авторизация курьера без логина")
    def test_login_courier_without_login_returns_error(self, courier):
        response = login_courier(
            "",
            courier["password"]
        )

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Авторизация курьера без пароля")
    def test_login_courier_without_password_returns_error(self, courier):
        response = login_courier_without_password(courier["login"])

        assert response.status_code == 504

    @allure.title("Авторизация курьера с неверным паролем")
    def test_login_courier_with_wrong_password_returns_error(self, courier):
        response = login_courier(
            courier["login"],
            "wrong_password_123"
        )

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Авторизация курьера с несуществующим логином")
    def test_login_courier_with_nonexistent_login_returns_error(self):
        response = login_courier(
            "nonexistent_courier_123456",
            "123456"
        )

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"