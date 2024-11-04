from django.urls import path, include
from . import views
from management.package.views import package_list, package_create, package_details
urlpatterns = [
    path('', views.index, name='index'),
    path('packagelist/', package_list, name='package_list'),
    # path('package/', include('management.booking.urls')),
    path('package/create/', package_create, name='package_create'),
    path('package/<int:package_id>/', package_details, name='package_detail'),

]
