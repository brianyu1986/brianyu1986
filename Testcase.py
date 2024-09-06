import pytest
import TestFunction


@pytest.mark.string
def test_case():    # TestCase use to check Status 
    assert TestFunction.Callapi("https://swapi.dev/api/films/", "POST") == {'detail': "Method 'POST' not allowed."}  # Case 1
    assert TestFunction.Callapi("https://swapi.dev/api/films/7") == {'detail': 'Not found'}                          # Case 4
    assert TestFunction.Callapi("https://swapi.dev/api/films/a") == {'detail': 'Not found'}                          # Case 5


def Case2():
    url = "https://swapi.dev/api/films/"
    response = requests.request("get", url)
    jsonResult = json.loads(response.text)
    print(jsonResult)


def Case3(url):
    uurl = "https://swapi.dev/api/films/1/"
    response = requests.request("get", url)
    jsonResult = json.loads(response.text)
    print(jsonResult)


def Case6():
    url = "https://swapi.dev/api/films/1/"
    response = requests.request("get", url)
    jsonResult = json.loads(response.text)
    print(jsonResult["vehicles"])
