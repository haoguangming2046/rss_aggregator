# Service file used to talk to grpc service and helper methods for views
import os

import grpc
from google.protobuf.json_format import MessageToDict

import feeds_pb2
import feeds_pb2_grpc


MAX_MESSAGE_LENGTH = 4 * 1024 * 1024 * 10
options = [
    ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
    ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)
]
channel = grpc.insecure_channel(
    os.environ.get("FEED_MANAGER_HOST", "localhost:50053"),
    options=options,
)

stub = feeds_pb2_grpc.FeedsStub(channel)


def get_all_feed_sources():
    response = stub.GetAllFeedSources(feeds_pb2.EmptyRequest())
    return MessageToDict(response, including_default_value_fields=True)


def create_feed_source(link):
    response = stub.CreateFeedSource(feeds_pb2.FeedSource(link=link))
    return MessageToDict(response, including_default_value_fields=True)


def update_feed_source(source_id):
    response = stub.UpdateFeedSource(feeds_pb2.FeedSource(id=source_id))
    return MessageToDict(response, including_default_value_fields=True)


def get_feeds():
    response = stub.GetAllFeeds(feeds_pb2.EmptyRequest())
    return MessageToDict(response, including_default_value_fields=True)


def get_custom_feeds(paginate_number="0"):
    query = feeds_pb2.Query(paginate_number=paginate_number)
    response = stub.GetCustomFeeds(query)
    return MessageToDict(response, including_default_value_fields=True)


def get_feed(slug):
    response = stub.GetFeed(feeds_pb2.Feed(slug=slug))
    return MessageToDict(response, including_default_value_fields=True)


def get_user_bookmarks(username):
    response = stub.GetAllBookmark(feeds_pb2.User(username=username))
    return MessageToDict(response, including_default_value_fields=True)


def create_user_bookmark(feed_id, username):
    response = stub.CreateFeedBookmark(feeds_pb2.FeedBookmark(
        user=feeds_pb2.User(username=username),
        feed=feeds_pb2.Feed(id=feed_id),
    ))
    return MessageToDict(response)


def create_user_comment(feed_id, text, username):
    response = stub.CreateFeedComment(feeds_pb2.FeedComment(
        comment=feeds_pb2.Comment(
            user=feeds_pb2.User(username=username),
            text=text,
        ),
        feed=feeds_pb2.Feed(id=feed_id),
    ))
    return MessageToDict(response)
