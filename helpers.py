import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps

def lookup(location, timesteps):
    
    #lookup the weather for a location
    try:
        BASE_URL = "https://api.tomorrow.io/v4/weather/forecast"
        api_key = "eEgWKij4Z9p2Mvf6WYAAX3Wj0zFa2U1L"
        url = f"{BASE_URL}?location={location}&timesteps={timesteps}&units=metric&apikey={api_key}"
        headers = {"accept": "application/json"}
        r = requests.get(url, headers=headers)
        r.raise_for_status()
    except requests.RequestException:
        return None
    
    #parse the response
 
    weather = {}

    location = (r.json()["location"]["name"])

    values = {}
    count = 0
    
    if timesteps == "1d":
        t = "daily"
        max_temp = "temperatureMax"
        avg_temp = "temperatureAvg"
        min_temp = "temperatureMin"
        precipitation = "precipitationProbabilityAvg"
        max_rain = "rainIntensityAvg"
        avg_gust = "windGustAvg"
        avg_wind_speed = "windSpeedAvg"

    else:
        t = "hourly"
        max_temp ="temperature"
        avg_temp ="temperature"
        min_temp ="temperature"
        precipitation = "precipitationProbability"
        max_rain = "rainIntensity"
        avg_gust = "windGust"
        avg_wind_speed = "windSpeed"


    for i in r.json()["timelines"][t]:
        values[f"t{count}"] = {
        "utc_time": i["time"],
        "max_temp": i["values"][max_temp],
        "avg_temp": i["values"][avg_temp],
        "min_temp": i["values"][min_temp],
        "precipitation": i["values"][precipitation],
        "max_rain": i["values"][max_rain],
        "avg_gust": i["values"][avg_gust],
        "avg_wind_speed": i["values"][avg_wind_speed],
        }
        if count > 23:
            break
        else:
            count += 1

    weather["values"] = values
    weather["location"] = location

    return weather

def onedp(value):
    """Format value as 1 decimal place."""
    return f"{value:,.1f}°C"

def feel(temp):
    if temp <= 5:
        return "\U0001F976"
    elif temp > 5 and temp < 14:
        return "\U0001F610"
    elif temp >=14 and temp < 20:
        return "\U0001F642"
    elif temp >= 20 and temp < 25:
        return "\U0001F60E"
    else:
        return "\U0001F975"


def rain(prob_precip):
    drop = "\U0001F4A7"
    rain = prob_precip
    if rain > 70:
        return f"{drop}"*5
    elif rain > 60:
        return f"{drop}"*4
    elif rain > 50:
        return f"{drop}"*3
    elif rain > 40:
        return f"{drop}"*2
    elif rain > 30:
        return f"{drop}"*1
    elif rain > 20:
        return "\U0001F326"
    else:
        return "\U00002600"
    
def wind(windspeed):
    light = "\U0001F343"
    mild = "\U0001F32C"
    heavy = "\U0001F32A"
    if windspeed > 38:
        return heavy
    elif windspeed > 15:
        return mild
    elif windspeed > 8:
        return light
    else:
        return ""

