import json
from urllib.request import urlopen

from bs4 import BeautifulSoup

import feeds_pb2


def get_feed_list(feeds):
    """ Return List of Proto Feed Object
    """
    feeds_pb_list = [feeds_pb2.Feed(**_get_valid_fields_feed(feed)) for feed in feeds]
    return feeds_pb2.FeedList(data=feeds_pb_list)


def get_feed_details(feed, details, comments):
    """ Return Feed with Details and Original JSON Contant
    """
    feed = _get_valid_fields_feed(feed)
    feed["details"] = details
    comments = [feeds_pb2.Comment(**{
        "user": feeds_pb2.User(username=comment.user),
        "added_on": str(comment.added_on),
        "text": comment.text}
    ) for comment in comments]
    feed["comment_data"] = comments
    return feeds_pb2.Feed(**feed)


def get_feed_sources_list(feed_sources):
    """ Return All feed sources as Proto objects
    """
    feed_sources_pb_list = [feeds_pb2.FeedSource(**{
        "id": feed_source.id,
        "name": feed_source.name,
        "status": feed_source.status,
        "link": feed_source.link,
        "logo_link": feed_source.logo_link,
        "last_active_on": str(feed_source.last_active_on),
        "details": feed_source.details}
    ) for feed_source in feed_sources]
    return feeds_pb2.FeedSourceList(data=feed_sources_pb_list)


def get_bookmark_list(bookmarks):
    """ Return Bookmarked feed ids list
    """
    bookmark_feed_pb_list = [feeds_pb2.Feed(**{
        'id': bookmark.feed.id,
    }) for bookmark in bookmarks]
    return feeds_pb2.FeedList(data=bookmark_feed_pb_list)


def get_link_from_feed(feed):
    """ Get image link from feed parsed
    """
    link_text = ''
    for link in feed.get("links", []):
        if "image" in link.get("type", ""):
            link_text = link.get("href", "")
            break
    if not link_text:
        link_text = _try_from_page_extract(feed)
    return link_text


def get_links_from_feed(feed):
    """ Extract all links from feed and build list
    """
    links_extracted = {}
    for link in feed.get("links", []):
        link_type = link.get("type", "text/html")
        link_value = link.get("href", "")
        if link_value:
            links_extracted[link_value] = link_type
    default_link = feed.get("link", "")
    if default_link:
        links_extracted[default_link] = "text/html"
    return json.dumps(links_extracted)


def _get_valid_fields_feed(feed):
    """ Return Valid Fields in Dict for Building Proto Feed
    """
    return {
        "id": feed.id,
        "title": feed.title,
        "feed_id": feed.feed_id,
        "author": feed.author,
        "added_on": str(feed.added_on),
        "summary": feed.summary,
        "slug": feed.slug,
        "source": feeds_pb2.FeedSource(
            id=feed.source.id,
            name=feed.source.name,
        ),
        "link": feed.link,
        "links": json.loads(feed.links),
    }


def _try_from_page_extract(feed):
    """ Try to extract image url from feed external links
    """
    link_text = ''
    for link in feed["links"]:
        href = link.get("href", "")
        if href:
            html_content = urlopen(href).read()
            soup = BeautifulSoup(html_content)
            for meta in soup(["meta"]):
                for meta_key, meta_value in meta.attrs.items():
                    if "property" == meta_key and meta_value == "og:image":
                        link_text = meta.get("content", "")
                        break
    return link_text
