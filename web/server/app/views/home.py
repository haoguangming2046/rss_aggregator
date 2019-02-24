from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    """The view used for home page
    """
    template = "views/home.pug"
    context = {}
    return render(request, template, context)
