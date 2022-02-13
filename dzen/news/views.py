from django.shortcuts import render
from django.views import View

from static.scripts import parser_lenta, parser_tj


class Index(View):
    def get(self, request):
        lenta = parser_lenta.lenta
        tjournal = parser_tj.tjournal
        context = {'title': 'Главное на сегодня', 'lenta': lenta, 'tjournal': tjournal}
        return render(request, 'news/index.html', context)
