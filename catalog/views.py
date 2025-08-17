from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm

from catalog.models import Product


class ProductlistView(ListView):
    """Класс контроллера для отображения списка продуктов"""

    model = Product


class ProductDetailView(DetailView):
    """Класс контроллера для отображения подробной информации"""

    model = Product

    def get_object(self, queryset=None):
        """Метод для отображения и счета количества просмотров"""
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    """Класс контроллера для Создания продукта"""

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    """Класс контроллера для Редактирования/Обновления продукта"""

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        """Метод для редиректа обновленного продукта на страницу этого продукта"""

        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

class ProductDeleteView(DeleteView):
    """Класс контроллера для Удаления продукта"""

    model = Product
    success_url = reverse_lazy('catalog:product_list')


def contacts(request):
    return render(request, "contacts.html")