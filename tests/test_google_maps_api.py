import json

from utils.api import GoogleMapsAPI
from utils.checking import Checking


class TestCreatePlace:
    def test_create_new_place(self):
        print("Метод POST")
        result_post = GoogleMapsAPI.create_new_place()cd
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        print(result_post.status_code)
        token = json.loads(result_post.text) #получаем поля, которые будем ожидать
        print(list(token))
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, "status", "OK")

        print("Метод GET created location")
        result_get = GoogleMapsAPI.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        print(list(token))
        print(result_get.text)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, "address", "29, side layout, cohen 09")

        print("Метод PUT")
        result_put = GoogleMapsAPI.update_new_place(place_id)
        Checking.check_json_token(result_put, ['msg'])
        print(result_put)
        Checking.check_json_value(result_put, "msg", "Address successfully updated")

        print("Метод GET updated location")
        result_get2 = GoogleMapsAPI.get_new_place(place_id)
        Checking.check_status_code(result_get2, 200)
        print(result_get2.text)
        Checking.check_json_value(result_get2, "address", "100 Lenina street, RU")

        print("Метод DELETE location")
        result_delete = GoogleMapsAPI.delete_location(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_value(result_delete, "status", "OK")

        print("Метод GET deleted location")
        result_get3 = GoogleMapsAPI.get_new_place(place_id)
        Checking.check_status_code(result_get3, 404)
        print(result_get3.text)
        Checking.check_json_value(result_get3, "msg", "Get operation failed, looks like place_id  doesn't exists")
