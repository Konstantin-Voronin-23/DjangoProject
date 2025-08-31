from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm, ProductModeratorForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from catalog.services import get_product_from_cache, get_products_by_category

from catalog.models import Product, Category


class OwnerOrModeratorMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        user = self.request.user
        if user.groups.filter(name='Модератор продуктов').exists() and user.has_perm('catalog.can_unpublish_product'):
            return True

        return obj.owner == user

    def handle_no_permission(self):
        raise PermissionDenied


class ProductlistView(ListView):
    """Класс контроллера для отображения списка продуктов"""

    model = Product

    def get_queryset(self):
        return get_product_from_cache()


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    """Класс контроллера для отображения подробной информации"""

    model = Product

    def get_object(self, queryset=None):
        """Метод для отображения и счета количества просмотров"""
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.views_counter += 1
            self.object.save()
            return self.object
        raise PermissionDenied


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Класс контроллера для Создания продукта"""

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, OwnerOrModeratorMixin, UpdateView):
    """Класс контроллера для Редактирования/Обновления продукта"""

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        """Метод для редиректа обновленного продукта на страницу этого продукта"""

        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        obj = self.get_object()
        if obj.owner == user:
            return ProductForm
        if user.groups.filter(name='Модератор продуктов').exists():
            return ProductModeratorForm
        return PermissionDenied

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Модератор продуктов').exists():
            return Product.objects.all()
        return Product.objects.filter(owner=user)

class ProductDeleteView(LoginRequiredMixin, OwnerOrModeratorMixin, DeleteView):
    """Класс контроллера для Удаления продукта"""

    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Модератор продуктов').exists():
            return Product.objects.all()
        return Product.objects.filter(owner=user)


def contacts(request):
    return render(request, "contacts.html")


class CategoryProductsView(ListView):
    """Представление для отображения продуктов по категории"""
    template_name = 'catalog/category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        result = get_products_by_category(category_name)
        self.extra_context = {'category': result['category']}
        return result['products']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


def categories_list(request):
    """Представление для отображения списка всех категорий"""
    categories = Category.objects.all()
    return render(request, 'catalog/categories_list.html', {'categories': categories})
