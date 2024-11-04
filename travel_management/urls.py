# travel_management/urls.py
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Voyage "
admin.site.site_title = "ClumsyCoders Admin Portal"
admin.site.index_title = "Welcome to Travel Management Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('management.urls')),
]
