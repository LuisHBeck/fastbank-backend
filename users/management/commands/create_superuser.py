from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Cria um superusuário personalizado'

    def handle(self, *args, **options):
        User = get_user_model()
        User.objects.create_superuser(123, '123')