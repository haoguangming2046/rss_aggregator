import os
import logging
from functools import wraps

level = os.environ.get("logging_level", logging.INFO)
logging.basicConfig(level=level)


def logger(name, info):
    logger = logging.getLogger(name)
    logger.log(level=level, msg=info)


def log_rpc():
    def actual_decorator(function):
        @wraps(function)
        def inner_function(*args, **kwargs):
            resp = function(*args, **kwargs)
            logger(function.__name__, 'function called')
            return resp
        return inner_function
    return actual_decorator
