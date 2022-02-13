from django.shortcuts import render
from django.views import View


class Index(View):
    def get(self, request):
        context = {'title': 'Главное на сегодня'}
        return render(request, 'news/index.html', context)
