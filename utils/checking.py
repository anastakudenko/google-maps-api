"""Метод для проверки ответов наших запросов"""
import json


class Checking:
    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f'Успешно. Статус код = {response.status_code}')
        else:
            print(f'Неуспешно. Статус код = {response.status_code}')

    """Метод для проверки наличия обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_token(response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")

    """Метод для проверки значений обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f'{field_name} верен')

