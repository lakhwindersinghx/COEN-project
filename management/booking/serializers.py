from rest_framework import serializers
from .models import Booking
from management.package.models import Package

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


