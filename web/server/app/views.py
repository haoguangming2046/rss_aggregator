from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "base.pug", {})


def home(request):
    return render(request, "views/home.pug", {})
