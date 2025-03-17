from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity', 1))  # Ensure quantity is always an integer
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size', None)  # Get size safely
    bag = request.session.get('bag', {})

    if size:
        if item_id in bag:
            if 'items_by_size' in bag[item_id] and size in bag[item_id]['items_by_size']:
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'] = bag[item_id].get('items_by_size', {})
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in bag:
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag  # Update session
    return redirect(redirect_url)