from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from management.signin.views import signup, signin, forgotpassword, Logout
from management.package.views import package_list, package_create, package_details
from management.booking.views import BookingViewSet
from management.searchitem.views import search_results
from management.booking.views import book_package

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', search_results, name='search_results'),
]
