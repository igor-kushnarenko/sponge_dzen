import locale
from datetime import datetime

import pyowm

locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))
OWM = pyowm.OWM('59ff4e66ae7a38fcb9a7a637165a4172')

monthes = {
    1: 'января',
    2: 'февраля',
    3: 'марта',
    4: 'апреля',
    5: 'мая',
    6: 'июня',
    7: 'июля',
    8: 'августа',
    9: 'сентября',
    10: 'октября',
    11: 'ноября',
    12: 'декабря',
}


def get_weekday_date():
    today = datetime.today()
    str_today = datetime.today().strftime('%A, %d').lower()
    return f'{str_today.title()} {monthes[today.month]}'


def get_weather_today():
    manager = OWM.weather_manager()
    observation = manager.weather_at_place("Анапа, Россия")
    weather = observation.weather
    temp = weather.temperature('celsius')['temp']
    detailed = weather.clouds
    weather_message = f'Погода: +{str(round(temp))} C, облачность: {detailed}%'
    return weather_message