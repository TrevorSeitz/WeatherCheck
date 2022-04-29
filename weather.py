from wsgiref.util import request_uri
import requests
import getData 

incomingData = getData.theData()
statusCode = incomingData[1]
data = incomingData[0]

if statusCode == 200:
    weather = data['weather'][0]["description"]
    print("Weather: ", weather)
    temperatureC = round(data["main"]["temp"]-273.15, 1)
    temperatureF = round(temperatureC*9/5 + 32, 1)
    print("Temp: ", temperatureC, " C or ", temperatureF, " F")
else:
    print("An error occurred")