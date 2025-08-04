from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Category


def product_list (request):
    """Контроллер для отображения базовой страницы"""

    products = Product.objects.all()
    context = {"products" : products}
    return render(request, 'product_list.html', context)


def product_detail(request, pk):
    """Контроллер для отображения страницы по одному товару"""

    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_detail.html', context)


def contacts(request):
    return render(request, "contacts.html")