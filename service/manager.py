import feeds_pb2_grpc
from lib.main import (
    get_all_feed_sources, create_new_feed_source, update_feed_source,
    get_all_feeds, create_comment_for_feed, create_bookmark_for_feed,
    get_custom_feeds, get_feed
)
from utils.logging import log_rpc


class FeedManager(feeds_pb2_grpc.FeedsServicer):
    @log_rpc()
    def GetAllFeeds(self, request, context):
        """ Return 10 feeds at a time
        """
        return get_all_feeds(request)

    @log_rpc()
    def GetCustomFeeds(self, request, context):
        """ Return 10 feeds with custom query params
        """
        return get_custom_feeds(request)

    @log_rpc()
    def GetFeed(self, request, context):
        """ Return feeds with details and Original JSON
        """
        return get_feed(request)

    @log_rpc()
    def CreateFeedComment(self, request, context):
        """ Add a comment to a feed
        """
        return create_comment_for_feed(request)

    @log_rpc()
    def CreateFeedBookmark(self, request, context):
        """ Create a new bookmark to a feed
        """
        return create_bookmark_for_feed(request)

    @log_rpc()
    def CreateFeedSource(self, request, context):
        """ Validate and Create new Feed Source
        """
        return create_new_feed_source(request)

    @log_rpc()
    def UpdateFeedSource(self, request, context):
        """ Update Feed Source Active Status
        """
        return update_feed_source(request)

    @log_rpc()
    def GetAllFeedSource(self, request, context):
        """ Return All Feed Sources
        """
        return get_all_feed_sources(request)
