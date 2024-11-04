from django.urls import path
from .views import book_package, booking_success,confirm_booking
from management.booking import views

urlpatterns = [
    path('book/', book_package, name='book_package'),
    path('booking/success/<int:booking_id>/', booking_success, name='booking_success'),
    path('book hotel/', views.book_hotel, name='book_hotel'),
    path('book flight/', views.book_flight, name='book_flight'),
    path('hotels/', views.hotels_list, name='hotels_list'),
    path('flights/', views.flights_list, name='flights_list'),
    path('confirm-booking/', confirm_booking, name='confirm_booking'),
    path('book/flight/', views.book_flight, name='book_flight'),
    path('activities/', views.activity_list, name='activity_list'),
    path('add_activity/', views.add_activity, name='add_activity'),
    path('book/flight/', views.book_flight, name='book_flight'),
]
