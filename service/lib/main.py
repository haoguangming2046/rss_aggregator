import json
from datetime import datetime

from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.template.defaultfilters import slugify
from django.db import transaction

from db.models import FeedSource, Feed, Bookmarked, Comment, FeedDetail
from utils.logging import logger
from utils.feed import (
    get_feed_list, get_feed_details, get_feed_sources_list,
    get_bookmark_list, get_link_from_feed, get_links_from_feed
)
from utils.parse import parse_new_feeds
import feeds_pb2


def create_new_feed(feed, source):
    """ Create a new feed
    """
    try:
        with transaction.atomic():
            slug = feed.get("id") + feed.get('title')
            new_feed = Feed.objects.create(
                feed_id=feed.get("id"),
                title=feed.get("title"),
                summary=feed.get("summary", ""),
                author=feed.get("author", ""),
                slug=slugify(slug[0:254]),
                link=get_link_from_feed(feed),
                links=get_links_from_feed(feed),
                source=source,
            )
            FeedDetail.objects.create(
                feed=new_feed,
                content_json=json.dumps(feed),
            )
            source.last_active_on = datetime.now()
            source.save()
    except ValidationError as e:
        exc = e
        logger(__name__, "Could not create new Feed due to {}".format(str(exc)))
        raise ValidationError(str(exc))
    logger(__name__, "Successfull create new feed")
    return


def get_all_feeds(request):
    """ Return all feeds
    """
    feeds = Feed.objects.all().order_by('-id')
    return get_feed_list(feeds)


def get_custom_feeds(request):
    """ Return 10 feeds with custom query params
    """
    start = int(request.paginate_number) * 10
    end = start + 10
    feeds = Feed.objects.all().order_by('-id')[start: end]
    return get_feed_list(feeds)


def get_feed(request):
    """ Return feeds with details and Original JSON
    """
    try:
        feed = Feed.objects.get(slug=request.slug)
        details = FeedDetail.objects.get(feed=feed.id)
        comments = Comment.objects.filter(feed=feed.id)
    except ObjectDoesNotExist as e:
        exc = e
        logger(__name__, "Could not get feed due to {}".format(str(exc)))
        return feeds_pb2.Feed()
    return get_feed_details(feed, details.content_json, comments)


def create_comment_for_feed(request):
    """ Add a comment to a feed
    """
    try:
        feed = Feed.objects.get(id=request.feed.id)
        Comment.objects.create(
            user=request.comment.user.username,
            feed=feed,
            text=request.comment.text,
        )
    except (ValidationError, Feed.DoesNotExist) as e:
        exc = e
        logger(__name__, "Could not add Comment due to {}".format(str(exc)))
        errors = _get_errors(exc)
        return feeds_pb2.OperationStatus(
            op_status=feeds_pb2.Status.Value('FAILURE'),
            details={'errors': feeds_pb2.RepeatedString(data=errors)},
        )
    return feeds_pb2.OperationStatus(
        op_status=feeds_pb2.Status.Value('SUCCESS'),
    )


def create_bookmark_for_feed(request):
    """ Create a new bookmark to a feed
    """
    try:
        feed = Feed.objects.get(id=request.feed.id)
        Bookmarked.objects.create(
            user=request.user.username,
            feed=feed,
        )
    except (ValidationError, Feed.DoesNotExist) as e:
        exc = e
        logger(__name__, "Could not add Bookmark due to {}".format(str(exc)))
        errors = _get_errors(exc)
        return feeds_pb2.OperationStatus(
            op_status=feeds_pb2.Status.Value('FAILURE'),
            details={'errors': feeds_pb2.RepeatedString(data=errors)},
        )
    return feeds_pb2.OperationStatus(
        op_status=feeds_pb2.Status.Value('SUCCESS'),
    )


def get_all_bookmark(request):
    """ Get all feed ids bookmaker for a user
    """
    bookmarks = Bookmarked.objects.filter(user=request.username)
    return get_bookmark_list(bookmarks)


def create_new_feed_source(link):
    """ Validate and Create new Feed Source
    """
    try:
        response = parse_new_feeds(link)
        if response["status"]:
            if "logo" in response["details"]:
                logo_link = response["details"]["logo"]
            elif "image" in response["details"]:
                logo_link = response["details"]["image"]["href"]
            else:
                logo_link = ''
            FeedSource.objects.create(
                name=response["details"]["title"],
                link=link,
                logo_link=logo_link,
                details=json.dumps(response["details"]),
            )
        else:
            return feeds_pb2.OperationStatus(
                op_status=feeds_pb2.Status.Value('FAILURE'),
                details={'errors': feeds_pb2.RepeatedString(data=['Could not parse given link'])},
            )
    except ValidationError as e:
        exc = e
        logger(__name__, "Could not add Feed Source due to {}".format(str(exc)))
        errors = _get_errors(exc)
        return feeds_pb2.OperationStatus(
            op_status=feeds_pb2.Status.Value('FAILURE'),
            details={'errors': feeds_pb2.RepeatedString(data=errors)},
        )
    return feeds_pb2.OperationStatus(
        op_status=feeds_pb2.Status.Value('SUCCESS'),
    )


def update_feed_source(request):
    """ Update Feed Source Active Status
    """
    try:
        feed = FeedSource.objects.get(id=request.id)
        feed.status = not feed.status
        feed.save()
    except (ValidationError, FeedSource.DoesNotExist) as e:
        exc = e
        logger(__name__, "Could not update Feed Source due to {}".format(str(exc)))
        errors = _get_errors(exc)
        return feeds_pb2.OperationStatus(
            op_status=feeds_pb2.Status.Value('FAILURE'),
            details={'errors': feeds_pb2.RepeatedString(data=errors)},
        )
    return feeds_pb2.OperationStatus(
        op_status=feeds_pb2.Status.Value('SUCCESS'),
    )


def get_all_feed_sources(request):
    """ Return All Feed Sources
    """
    feed_sources = FeedSource.objects.all().order_by('-id')
    return get_feed_sources_list(feed_sources)


def _get_errors(exc):
    """ Partial method to extract exception messages to list
    """
    if hasattr(exc, 'message'):
        errors = exc.messages
    else:
        errors = [str(exc)]
    return errors
