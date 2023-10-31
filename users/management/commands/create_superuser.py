from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create a super user'

    def handle(self, *args, **options):
        User = get_user_model()
        User.objects.create_superuser(123, '123')