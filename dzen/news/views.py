from datetime import datetime
from django.shortcuts import render
from django.views import View

from static.scripts import parser_lenta, parser_tj, get_info, weather_maker


class Index(View):
    def get(self, request):
        weather_week = weather_maker.WeatherMaker().weather_parser()
        lenta = parser_lenta.lenta
        tjournal = parser_tj.tjournal
        date = get_info.get_weekday_date()
        weather = get_info.get_weather_today()
        context = {
            'title': 'Главное на сегодня',
            'lenta': lenta,
            'tjournal': tjournal,
            'date': date,
            'weather': weather,
            'weather_week': weather_week,
        }
        return render(request, 'news/index.html', context)
