from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Wishlist
from django.contrib import messages 

# Create your views here.
@login_required
def wishlist_view(request):
    items = Wishlist.objects.filter(user=request.user)
    return render(request, "wishlist/wishlist.html", {"items": items})

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    if created:
        messages.success(request, f"{product.name} has been added to your wishlist.")
    else:
        messages.info(request, f"{product.name} is already in your wishlist.")
    return redirect("wishlist")

@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    deleted, _ = Wishlist.objects.filter(user=request.user, product=product).delete()
    if deleted:
        messages.success(request, f"{product.name} has been removed from your wishlist.")
    else:
        messages.info(request, f"{product.name} was not in your wishlist.")
    return redirect("wishlist")

@login_required
def move_to_bag(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    bag = request.session.get('bag', {})

    # For products without size
    if str(product_id) in bag:
        bag[str(product_id)] += 1
    else:
        bag[str(product_id)] = 1

    # Save back to session
    request.session['bag'] = bag

    # Remove from wishlist
    Wishlist.objects.filter(user=request.user, product=product).delete()
    # Add success message
    messages.success(request, f"{product.name} has been moved to your bag.")

    return redirect('view_bag')
