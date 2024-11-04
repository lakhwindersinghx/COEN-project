# urls.py
from django.urls import path
from .views import add_to_cart, cart_details ,remove_from_cart

urlpatterns = [
    path('add_to_cart/<int:package_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_details, name='cart_details'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
]
