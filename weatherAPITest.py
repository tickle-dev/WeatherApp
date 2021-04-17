import requests
import json

parameraters = {
    "q": 'Jacksonville,NC,840',
    "units": 'imperial',
    'appid': '6c3234d29cece444ce059634f21ac09f'
}

request = requests.get('http://api.openweathermap.org/data/2.5/forecast?', params=parameraters)

def jprint (obj):

    with open("Weather.json", "w") as file:
        json.dump(obj, file, sort_keys=True, indent=4)
    

def get_Next_Three_Hour_Weather():
    with open("Weather.json") as file:
        data = json.load(file)
        nextThreeHour = data['list'][0]
        for item, info in nextThreeHour.items():
            if item == 'dt_txt':
                print('Here is the weather information for', info)
            if item == 'main':
                for key, key_desc in info.items():
                    print(key + ':', key_desc)



