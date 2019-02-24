from concurrent import futures
import time
import os
import sys

import django
import grpc

django.setup()

import feeds_pb2_grpc
from manager import FeedManager

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    feeds_pb2_grpc.add_FeedsServicer_to_server(FeedManager(), server)

    PORT = os.environ.get("FEED_MANAGER_SERVER_PORT", "50053")
    server.add_insecure_port('[::]:{}'.format(PORT))
    sys.stdout.write(("Starting service server on port {}\n"
                      "Quit the server with CONTROL-C\n").format(PORT))
    sys.stdout.flush()
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
