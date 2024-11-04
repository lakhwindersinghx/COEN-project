# from django.urls import path
# # from management.booking.views import CreateCheckoutSessionView
# from .views import CreateCheckoutSessionView
# urlpatterns = [
#     path('create-checkout-session/<slug:package_destination>/', CreateCheckoutSessionView.as_view(), name='create_checkout_session'),
# ]


# urls.py
from django.urls import path
from . import  views
# from .views import create_checkout_session, payment_success, payment_cancel ,HomePageView ,stripe_config

urlpatterns = [
    # path('create-checkout-session/', create_checkout_session, name='create_checkout_session'),
    # path('success/', payment_success, name='payment_success'),
    # path('cancel/', payment_cancel, name='payment_cancel'),


    path('home/', views.HomePageView, name='home'),
    path('create-checkout-session/', views.create_checkout_session),
    path('config/', views.stripe_config),
    path('success/', views.SuccessView.as_view()),
    path('cancelled/', views.CancelledView.as_view()),


]