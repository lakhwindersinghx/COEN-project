from django.urls import path, include
from . import views
from management.booking.views import BookingViewSet
from management.searchitem.views import search_results

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('management.package.urls')),
    path('package/', include('management.booking.urls')),
    path('', include('management.signin.urls')),
    path('search/', search_results, name='search_results'),
    path('Booking/', BookingViewSet.as_view({'get': 'list'}), name='Bookings'),
    path('', include('management.user_profile.urls')),
    path('',include('management.booking.urls')),
    path('add_to_cart/',include( "management.cart.urls"), name='add_to_cart'),
    path('', include('management.payment.urls')),

]
