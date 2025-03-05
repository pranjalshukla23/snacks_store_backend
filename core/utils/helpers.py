from core.models import Cart
from decimal import Decimal

# Apply discount or special pricing rules for the products
def calculate_cart_totals():
    cart_items = Cart.objects.all()
    total_price = 0
    total_items = 0

    for item in cart_items:
        code = item.product.product_code
        quantity = item.quantity
        price_per_unit = item.product.price

        # Green Tea (BOGO)
        if code == "GR1":
            free_items = quantity  
            total_price += (quantity * price_per_unit)  
            total_items += (quantity + free_items)  

        # Strawberries (Bulk Discount)
        elif code == "SR1":
            if quantity >= 3:
                total_price += quantity * Decimal(4.50)  
            else:
                total_price += quantity * price_per_unit
            total_items += quantity

        # Coffee (Bulk Discount)
        elif code == "CF1":
            if quantity >= 3:
                total_price += quantity * (price_per_unit * Decimal(2 / 3)) 
            else:
                total_price += quantity * price_per_unit
            total_items += quantity

        else:
            total_price += quantity * price_per_unit
            total_items += quantity

    return round(total_price, 2), total_items