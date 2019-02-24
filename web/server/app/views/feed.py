from django.shortcuts import render

from app.stubs.feed_service import get_feed


def feed(request, id):
    """The view used for feed page
    """
    template = "views/feed.pug"
    context = {
        "feed": get_feed(id)
    }
    return render(request, template, context)
