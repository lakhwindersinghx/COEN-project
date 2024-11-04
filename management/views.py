from django.shortcuts import render
from management.package.models import Package

def index(request):
    try:
        package_alberta = Package.objects.get(pk=1)  # Replace with the actual ID
        package_newyork = Package.objects.get(pk=3)  # Replace with the actual ID
        package_mumbai = Package.objects.get(pk=2)  # Replace with the actual ID
    except Package.DoesNotExist:
        package_alberta = package_newyork = package_mumbai = None

        # Pass them to the context
    context = {
        'package_alberta': package_alberta,
        'package_newyork': package_newyork,
        'package_mumbai': package_mumbai,
    }

    return render(request, 'index.html', context)
    # return render(request, 'index.html')