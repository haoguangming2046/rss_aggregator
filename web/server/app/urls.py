from django.urls import path
from django.http import HttpResponseRedirect

from app.views.home import home
from app.views.signup import signup

app_name = 'app'
urlpatterns = [
    path('', lambda r: HttpResponseRedirect('/home')),
    path('signup', signup, name='signup'),
    path('home', home, name='home'),
]
