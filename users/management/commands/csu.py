from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'Создаёт администратора'

    def handle(self, *args, **kwargs):
        email = 'admin@example.com'
        password = '123qaz'

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING(f'Пользователь {email} уже существует'))
        else:
            user = User.objects.create_user(email=email)
            user.set_password(password)
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Суперпользователь {email} создан'))