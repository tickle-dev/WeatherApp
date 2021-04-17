import requests
import json


request = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=Jacksonville,NC,840&appid=6c3234d29cece444ce059634f21ac09f')

def jprint (obj):

    with open("Weather.json", "w") as file:
        json.dump(obj, file, sort_keys=True, indent=4)
    

def weatherInfo():
    with open("Weather.json") as file:
        data = json.load(file)
        nextDayWeather = data['list'][0]
        for item in nextDayWeather.items():
            print(item)
weatherInfo()

