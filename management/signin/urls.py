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
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', Logout, name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='signin/forgotpassword.html', ),
         name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='signin/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='signin/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='signin/password_reset_complete.html'),
         name='password_reset_complete'),
]
