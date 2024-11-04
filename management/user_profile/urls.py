from django.urls import path
from .views import view_profile, my_orders, my_profile, all_bookings, booking_update, all_packages, package_update, \
    all_users, user_profile_update

urlpatterns = [
    path('profile/<int:user_id>/', view_profile, name='view_profile'),
    path('my-orders/', my_orders, name='my_orders'),
    path('profile/my_profile/', my_profile, name='my_profile'),
    path('my-orders/<str:filter_by>/', my_orders, name='my-orders-filter'),
    path('all_bookings/', all_bookings, name='all_bookings'),
    path('bookings/<int:pk>/edit/', booking_update, name='booking_update'),
    path('all_packages', all_packages, name='all_packages'),
    path('package/<int:pk>/edit/', package_update, name='package_update'),
    path('all-users/', all_users, name='all_users'),
    path('edit-profile/<int:pk>/', user_profile_update, name='profile_update'),
]
