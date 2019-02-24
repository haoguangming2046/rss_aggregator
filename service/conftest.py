import pytest


@pytest.fixture
def feed():
    return {
        "id": 1,
        "title": 'Example Title',
        "author": 'Example Author',
        "added_on": '2019-02-26 04:14:08.094998',
        "summary": 'Example Summary',
        "slug": 'example-slug',
        "link": 'http:www.example.com',
        "links": '{"http//www.example.com": "text/html"}'
    }
