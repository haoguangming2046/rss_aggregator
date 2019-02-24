import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from app.stubs.feed_service import (
    get_all_feed_sources, get_feeds, get_user_bookmarks,
    create_user_bookmark, create_user_comment, update_feed_source,
    create_feed_source, get_custom_feeds
)


@login_required
def api_all_feed_sources(request):
    """ This view is to retreive all feed sources
    """
    if request.is_ajax():
        return JsonResponse(get_all_feed_sources(), safe=False)


@login_required
def api_all_feeds(request):
    """ This views to retreive feeds
    """
    if request.is_ajax():
        return JsonResponse(get_feeds())


@login_required
def api_custom_feeds(request):
    """ This views to retreive feeds
    """
    if request.is_ajax():
        paginate_number = request.GET.get("paginate_number", "0")
        return JsonResponse(get_custom_feeds(paginate_number))


@login_required
def api_user_bookmarks(request):
    """ This API endpoint is to return all bookmarks for a user
    """
    if request.is_ajax():
        return JsonResponse(get_user_bookmarks(request.user.username), safe=False)


@login_required
def api_create_bookmark(request):
    """ This API endpoint is to create a new bookmark
    """
    if request.is_ajax() and request.method == "POST":
        data = json.loads(request.body)
        feed_id = int(data['data']['feed']['id'])
        return JsonResponse(
            create_user_bookmark(feed_id, request.user.username), safe=False)


@login_required
def api_create_comment(request):
    """ This API endpoint is to create a new comment for a feed
    """
    if request.is_ajax() and request.method == "POST":
        data = json.loads(request.body)
        feed_id = int(data['data']['feed']['id'])
        text = data['data']['feed']['commentText']
    return JsonResponse(
        create_user_comment(feed_id, text, request.user.username), safe=False)


@login_required
def api_update_feed_source(request, id):
    """ This API endpoint is to update the status of a feed source
    """
    if request.is_ajax() and request.method == "POST":
        return JsonResponse(update_feed_source(int(id)), safe=False)


@login_required
def api_create_feed_source(request):
    """ This API endpoint is to create a new feed source
    """
    if request.is_ajax() and request.method == "POST":
        data = json.loads(request.body)
        source_link = data['data']['link']
    return JsonResponse(create_feed_source(source_link), safe=False)
