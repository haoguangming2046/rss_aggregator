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
    feed["details"] = feeds_pb2.FeedDetail(
        content_json=details,
    )
    comments = [feeds_pb2.Comment(**{
        "user": comment.user,
        "added_on": str(comment.added_on),
        "text": comment.text}
    ) for comment in comments]
    feed["comment_data"] = comments
    return feed


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
        "source": feeds_pb2.FeedSource(
            id=feed.source.id,
            name=feed.source.name,
        ),
    }


def get_feed_sources_list(feed_sources):
    """ Return All feed sources as Proto objects
    """
    feed_sources_pb_list = [feeds_pb2.FeedSource(**{
        "id": feed_source.id,
        "name": feed_source.name,
        "status": feed_source.status,
        "link": feed_source.link,
        "logo_link": feed_source.logo_link,
        "last_active_on": str(feed_source.last_active_on)}
    ) for feed_source in feed_sources]
    return feed_sources_pb_list
