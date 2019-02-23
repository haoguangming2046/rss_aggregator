from django.shortcuts import render


def home(request):
    """The view used for home page
    """
    template = "views/home.pug"
    context = {}
    return render(request, template, context)
