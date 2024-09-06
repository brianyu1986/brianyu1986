def TestCase(url, method="get"):
    response = requests.request(method, url)
    jsonResult = json.loads(response.text)
    return jsonResult
