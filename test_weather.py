import requests
import unittest
import getTestData



class TestWeather(unittest.TestCase):



    def test_weather_is_not_empty(self):
        self.assertIsNotNone(getTestData.theData()[0])
        
    def test_city_is_correct(self):
        city = "Calgary"
        data = getTestData.theData()[0]
        assert data["name"] == city

    def test_Fahrenheit_Not_To_High(self):
        data = getTestData.theData()[0]
        assert data["main"]["temp"] < 325

    def test_Fahrenheit_Not_To_Low(self):
        data = getTestData.theData()[0]
        assert data["main"]["temp"] > 220

if __name__ == '__main__':
    unittest.main()