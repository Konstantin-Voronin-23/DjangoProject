from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from catalog.models import Product
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Создаёт группу Модератор продуктов с нужными правами'

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='Модератор продуктов')

        content_type = ContentType.objects.get_for_model(Product)

        can_unpublish = Permission.objects.get(codename='can_unpublish_product', content_type=content_type)
        delete_product = Permission.objects.get(codename='delete_product', content_type=content_type)

        group.permissions.add(can_unpublish, delete_product)

        self.stdout.write(self.style.SUCCESS('Группа Модератор продуктов создана и права назначены'))