import requests

BASIC_URL = "https://petstore.swagger.io/v2/pet"

def construct_url(common_url, api):
    return common_url + api

def test_get_status_code_equals_200():
    url = construct_url(BASIC_URL)
    response = requests.post(url, data={"id":1, "category":{"id":1, "name":"Vasya"}})
    assert response.status_code == 200, print(
        "Got wrong status code, expected is: {}, actual is  {}".format("200", response.status_code))