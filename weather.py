from wsgiref.util import request_uri
import requests
import apiKeys as apiKeys

weather_key = apiKeys.API_KEY
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

request_uri = f"{BASE_URL}?appid={weather_key}&q={city}"
response = requests.get(request_uri)

if response.status_code == 200:
    data = response.json()
    print("Data: ", data)
    weather = data['weather'][0]["description"]
    print("Weather: ", weather)
    temperatureC = round(data["main"]["temp"]-273.15, 1)
    temperatureF = round(temperatureC*9/5 + 32, 1)
    print("Temp: ", temperatureC, " C or ", temperatureF, " F")
else:
    print("An error occurred")