import sys

from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

try:
    from django.db import models
except Exception:
    print("There was an error loading django modules. Do you have django?")
    sys.exit()


class FeedSource(models.Model):
    name = models.TextField(null=False)
    status = models.BooleanField(default=True)
    link = models.TextField(null=False, default='')
    logo_link = models.TextField(default='')
    last_active_on = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    def __str__(self):
        return self.name

    def clean(self):
        if not (self.name or self.link or self.details):
            raise ValidationError(
                {NON_FIELD_ERRORS: 'Insufficient Data'}
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(FeedSource, self).save(*args, **kwargs)


class Feed(models.Model):
    feed_id = models.CharField(max_length=100, null=False, default='', unique=True)
    title = models.TextField(null=False, default='')
    summary = models.TextField()
    author = models.CharField(max_length=100, blank=True, default='')
    added_on = models.DateTimeField(auto_now_add=True)
    source = models.ForeignKey(FeedSource, on_delete=models.CASCADE)
    slug = models.CharField(max_length=255, null=False, unique=True)
    link = models.TextField(blank=True, default='')
    links = models.TextField()

    def __str__(self):
        return self.title

    def clean(self):
        if not (self.feed_id or self.title or self.slug or self.source):
            raise ValidationError(
                {NON_FIELD_ERRORS: 'Insufficient Data'}
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Feed, self).save(*args, **kwargs)


class FeedDetail(models.Model):
    feed = models.OneToOneField(Feed, on_delete=models.CASCADE)
    content_json = models.TextField()

    def __str__(self):
        return self.feed.title

    def clean(self):
        if not (self.feed or self.content_json):
            raise ValidationError(
                {NON_FIELD_ERRORS: 'Insufficient Data'}
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(FeedDetail, self).save(*args, **kwargs)


class Comment(models.Model):
    user = models.CharField(max_length=200, null=False)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    text = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    def clean(self):
        if not (self.user or self.feed or self.text):
            raise ValidationError(
                {NON_FIELD_ERRORS: 'Insufficient Data'}
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Comment, self).save(*args, **kwargs)


class Bookmarked(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    user = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.feed.title

    def clean(self):
        if not (self.feed or self.user):
            raise ValidationError(
                {NON_FIELD_ERRORS: 'Insufficient Data'}
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Bookmarked, self).save(*args, **kwargs)
