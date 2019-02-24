from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Craete a user and superuser for testing'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)

    def handle(self, *args, **options):
        user = User.objects.get(username="admin@rss.com")
        if not user:
            User.objects.create_superuser(
                username="admin@rss.com",
                email="admin@rss.com",
                password="admin",
            )
