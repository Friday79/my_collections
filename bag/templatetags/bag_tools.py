from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(product_or_price, quantity):
    """
    Accept either a product object or a raw Decimal price
    """
    # If it's a product object
    try:
        price = product_or_price.sale_price if product_or_price.is_on_sale else product_or_price.price
    except AttributeError:
        # Fallback: it's already a Decimal
        price = product_or_price  

    return price * quantity
