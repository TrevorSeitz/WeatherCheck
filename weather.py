from wsgiref.util import request_uri
import requests
import apiKeys

weather_key = apiKeys.API_KEY
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

request_uri = f"{BASE_URL}?appid={weather_key}&q={city}"
response = requests.get(request_uri)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("An error occurred")