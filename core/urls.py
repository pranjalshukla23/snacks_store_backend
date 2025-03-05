from django.urls import path
from .views import add_product, add_to_cart, get_all_products

urlpatterns = [
    path('products/', get_all_products, name='get_all_products'),
    path('add-product/', add_product, name="add-product"),
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
]
