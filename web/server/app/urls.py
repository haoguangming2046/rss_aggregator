from django.urls import path
from django.http import HttpResponseRedirect

from app.views.home import home
from app.views.feed import feed
from app.views.signup import signup
from app.views.settings import settings
from app.views.api import (
    api_all_feed_sources, api_all_feeds,
    api_user_bookmarks, api_create_bookmark,
    api_create_comment, api_create_feed_source,
    api_update_feed_source
)


app_name = 'app'
urlpatterns = [
    path('feed/<slug:id>/', feed, name='feed'),
    path('', lambda r: HttpResponseRedirect('/home')),
    path('signup', signup, name='signup'),
    path('home', home, name='home'),
    path('settings', settings, name='settings'),
    path('api/feed/sources', api_all_feed_sources, name="all_feed_sources"),
    path('api/feed/source/<int:id>/update/', api_update_feed_source, name="update_feed_source"),
    path('api/feed/source/create', api_create_feed_source, name="create_feed_source"),
    path('api/feeds', api_all_feeds, name="all_feeds"),
    path('api/user/bookmark/create', api_create_bookmark, name="create_user_bookmark"),
    path('api/user/bookmarks', api_user_bookmarks, name="user_bookmarks"),
    path('api/user/comment/create', api_create_comment, name="create_user_comment"),
]
