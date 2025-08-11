from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Загружает фикстуры с категориями и продуктами'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write('Загружаем категории...')
        call_command('loaddata', 'category_fixture.json')
        self.stdout.write('Загружаем продукты...')
        call_command('loaddata', 'product_fixture.json')
        self.stdout.write(self.style.SUCCESS('Фикстуры успешно загружены'))