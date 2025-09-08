from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductlistView, ProductDetailView, contacts, ProductCreateView, ProductUpdateView, ProductDeleteView, CategoryProductsView, categories_list


app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductlistView.as_view(), name='product_list'),
    path("contacts/", contacts, name="contacts"),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('catalog/create/', ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('categories/', categories_list, name='categories_list'),
    path('category/<str:category_name>/', CategoryProductsView.as_view(), name='category_products'),
]