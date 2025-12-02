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
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect("wishlist")

@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.filter(user=request.user, product=product).delete()
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

    return redirect('view_bag')
