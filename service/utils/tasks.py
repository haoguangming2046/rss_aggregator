import os
from datetime import timedelta

import django
from django.core.exceptions import ValidationError

from celery import Celery

django.setup()

from db.models import FeedSource
from lib.main import create_new_feed
from utils.parse import parse_new_feeds

celery = Celery(
    __name__,
    broker=os.environ.get(
        "TASKS_QUEUE_HOST",
        "amqp://guest:guest@localhost:5672//"
    ),
)
celery.config_from_object(__name__)


@celery.task
def get_new_feeds():
    """ Scheduled tasks to fetch new feeds
    """
    feed_sources = FeedSource.objects.filter(status=True)
    for source in feed_sources:
        retry_limit = 0
        status = False
        while retry_limit < 3 and not status:
            response = parse_new_feeds(source.link)
            if response["status"]:
                status = True
            retry_limit += 1
        if response["status"]:
            for feed in response["feeds"]:
                if retry_limit < 3:
                    try:
                        create_new_feed(feed, source)
                    except ValidationError:
                        retry_limit += 1
    return


CELERYBEAT_SCHEDULE = {
    'get_new_feeds': {
        'task': 'utils.tasks.get_new_feeds',
        'schedule': timedelta(seconds=10),
    },
}
