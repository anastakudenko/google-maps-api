from utils.http_method import HttpMethod
"""Методы для тестирования Google Maps API"""


base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"


class GoogleMapsAPI:

    @staticmethod
    def create_new_place():
        json_for_create_new_place = {
            "location": {

            "lat": -38.383494,

            "lng": 33.427362

            }, "accuracy": 50,

            "name": "Frontline house",

            "phone_number": "(+91) 983 893 3937",

            "address": "29, side layout, cohen 09",

            "types": [

             "shoe park",

            "shop"

             ],

             "website": "http://google.com",

            "language": "French-IN"

             }

        post_resource = '/maps/api/place/add/json'
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = HttpMethod.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post



    @staticmethod
    def get_new_place(place_id):
        get_resource = '/maps/api/place/get/json'
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = HttpMethod.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def update_new_place(place_id):
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_loc = {
            "place_id": place_id,
            "address":"100 Lenina street, RU",
            "key":"qaclick123"
        }
        result_put = HttpMethod.put(put_url, json_for_update_loc)
        print(result_put.text)
        return result_put

    @staticmethod
    def delete_location(place_id):
        delete_resource = '/maps/api/place/delete/json'
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_for_delete_location = {
            "place_id": place_id
        }
        result_delete = HttpMethod.delete(delete_url, json_for_delete_location)
        print(result_delete.text)
        return result_delete
