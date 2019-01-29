from django.urls import path

from app.views import index, home

app_name = 'app'
urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='home'),
]
