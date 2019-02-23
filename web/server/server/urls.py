from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='registration/login.pug')),
    path('logout/', LogoutView.as_view()),
    path('', include('app.urls', namespace='app')),
]
