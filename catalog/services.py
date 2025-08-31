from django.shortcuts import get_object_or_404
from config.settings import CACHE_ENABLED
from django.core.cache import cache
from catalog.models import Product, Category


def get_product_from_cache():
    """Получает данные продукта из кэша, если кэш пусть берет данные из БД"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'product_list'
    product = cache.get(key)
    if product is not None:
        return product
    product = Product.objects.all()
    cache.set(key, product)
    return product


def get_products_by_category(category_name):
    """Возвращает список продуктов выбранной категории"""
    category = get_object_or_404(Category, name=category_name)
    products = Product.objects.filter(
        category=category,
        is_published=True
    ).select_related('category', 'owner').order_by('name')

    return {
        'category': category,
        'products': products
    }
