from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from core.utils.helpers import calculate_cart_totals
from .models import Product, Cart
from .serializers import ProductSerializer, CartSerializer


# Create your views here.

from django.http import JsonResponse

# home view (/)
def home(request):
    return JsonResponse({"message": "Welcome to MyStore API!"})

# /api/add_product/
@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    # check for valid format
    if serializer.is_valid():
        # save the data in db
        serializer.save()
        return Response({"message": "product added successfully in database", "product": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)





@api_view(['POST'])
def add_to_cart(request):
    product_codes = request.data.get('products', [])
    if not product_codes:
        return Response({"error": "No products provided"}, status=400)

    # Loop through each product code and add to the cart
    for product_data in product_codes:
        product_code = product_data.get('product_code')
        quantity = product_data.get('quantity', 1)

        try:
            product = Product.objects.get(product_code=product_code)
        except Product.DoesNotExist:
            return Response({"error": f"Product {product_code} not found"}, status=404)

        # Create or update the cart item
        cart_item, created = Cart.objects.get_or_create(product=product)
        cart_item.quantity += quantity
        cart_item.save()

    # Calculate the totals after adding all the products to the cart
    total_price, total_items = calculate_cart_totals()

    return Response({
        "message": "Products added to cart",
        "total_items": total_items,
        "total_price": total_price
    })
