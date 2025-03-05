from django.urls import path
from .views import add_product, add_to_cart

urlpatterns = [
    path('add-product/', add_product, name="add-product"),
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
]
