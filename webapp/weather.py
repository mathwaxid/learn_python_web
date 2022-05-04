from flask import current_app
import requests


def weather_by_city(city='Tomsk,Russia'):
    weather_url = current_app.config['WEATHER_API_URL']
    params = {
        'key': current_app.config['WEATHER_API_KEY'],
        'q': city,
        'format': 'json', 
        'num_of_days': '3',
        'lang': 'ru',
    }
    try:
        result = requests.get(weather_url, params=params)
        result.raise_for_status()
        weather = result.json()
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    weather = weather['data']['current_condition'][0]
                    return weather
                except(IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):
        return False


if __name__ == '__main__':
    weather_by_city('Tomsk,Russia')
