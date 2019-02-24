import feedparser


def parse_new_feeds(source_link):
    """ Parse Feed entries and Feed details for a give source
    """
    response = feedparser.parse(source_link)
    if response["bozo"] == 0:
        feeds = [feed for feed in response["entries"]]
        return {"status": True, "feeds": feeds, "details": response["feed"]}
    else:
        return {"status": False}
