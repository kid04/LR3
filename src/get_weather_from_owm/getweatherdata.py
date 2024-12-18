import requests
import json

def get_weather_data(place, api_key=None):
    with requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}'
    ) as f:
        res = f.json()
        res_json = {}
        res_json["name"] = res["name"]
        res_json["country"] = res["sys"]["country"]
        res_json["coord"] = res["coord"]
        tz = int(res["timezone"])
        if tz < 0:
            res_json["timezone"] = "UTC"+str(int(tz/3600))
        else:
            res_json["timezone"] = "UTC+"+str(int(tz/3600))
        res_json["feels_like"] = res["main"]["feels_like"]

    print(json.dumps(res_json, indent=4))

