from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product


class ProductlistView(ListView):
    """1"""

    model = Product


class ProductDetailView(DetailView):
    """1"""

    model = Product

    def get_object(self, queryset=None):
        """1"""
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    """1"""

    model = Product
    fields = ('name', 'description', 'image', 'category', 'price')
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    """1"""

    model = Product
    fields = ('name', 'description', 'image', 'category', 'price')
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        """1"""

        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

class ProductDeleteView(DeleteView):
    """1"""

    model = Product
    success_url = reverse_lazy('catalog:product_list')


def contacts(request):
    return render(request, "contacts.html")