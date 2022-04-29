from wsgiref.util import request_uri
import requests
import apiKeys as apiKeys

def theData():
    weather_key = apiKeys.API_KEY
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    # city = "Calgary"
    city = input("Enter a city name: ")

    request_uri = f"{BASE_URL}?appid={weather_key}&q={city}"

    response = requests.get(request_uri)

    statusCode = response.status_code

    data = response.json()
    # print("This is from getData", data)
    return data, statusCode