import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from app.stubs.feed_service import get_all_feed_sources


@login_required
def settings(request):
    """The view used for settings page
    """
    template = "views/settings.pug"
    context = {
        "feed_sources": json.dumps(get_all_feed_sources())
    }
    return render(request, template, context)
