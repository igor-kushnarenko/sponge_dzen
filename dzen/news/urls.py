from django.urls import path

from news import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]
