# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem, Package
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, package=package)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_details')

@login_required
def cart_details(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'cart/cart_details.html', {'cart': cart})

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    if item.cart.user == request.user:  # Security check
        item.delete()
    return redirect('cart_details')