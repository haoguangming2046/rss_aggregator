def test_valid_fields_feed(feed):
    assert feed["id"] == 1
    assert feed["title"] == 'Example Title'
    assert feed["author"] == 'Example Author'
    assert feed["added_on"] == '2019-02-26 04:14:08.094998'
    assert feed["summary"] == 'Example Summary'
    assert feed["slug"] == 'example-slug'
    assert feed["link"] == 'http:www.example.com'
    assert feed["links"] == '{"http//www.example.com": "text/html"}'
