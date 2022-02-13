from django.shortcuts import render
from django.views import View

from static.scripts import parser


class Index(View):
    def get(self, request):
        lenta = parser.lenta
        context = {'title': 'Главное на сегодня', 'lenta': lenta}
        return render(request, 'news/index.html', context)
