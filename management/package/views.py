from django.shortcuts import redirect
from datetime import datetime
from .models import Package
from .forms import PackageForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'index.html')
# class PackageView(ListView):
#     model = Post
@login_required()
def packages(request):
    form = PackageForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        destination=request.POST.get('destination')
        activities=request.POST.get('activities')
        package=Package.objects.create(destination=destination, activities=activities,date = datetime.now())
        package.save()
    return render(request, 'package/package.html')

# @login_required(login_url='signin')
def package_list(request):
    packages = Package.objects.all()

    return render(request, 'package/package_list.html', {'packages': packages})

def package_details(request, package_id):
    package = get_object_or_404(Package, pk=package_id)
    # package = Package.objects.get(pk=pk)
    destination = package.destination

    destination_images = {
        'Mumbai': ['mumbai1.jpg', 'mumbai2.jpg', 'mumbai3.jpg', 'mumbai4.jpg'],
        'Toronto': ['toronto1.jpg', 'toronto2.jpg', 'toronto3.jpg', 'toronto4.jpg'],
        'Vancouver': ['vancouver1.jpg', 'vancouver2.jpg', 'vancouver3.jpg', 'vancouver4.jpg'],
        'Newyork': ['newyork1.jpg', 'newyork2.jpg', 'newyork3.jpg', 'newyork4.jpg'],
        'Paris': ['paris1.jpg', 'paris2.jpg', 'paris3.jpg', 'paris4.jpg'],
        'Mississauga': ['mississauga1.jpg', 'mississauga2.jpg', 'mississauga3.jpg', 'mississauga4.jpg'],
        'Calgary': ['calgary1.jpg', 'calgary2.jpg', 'calgary3.jpg', 'calgary4.jpg'],
        'Alberta': ['alberta1.jpg', 'alberta2.jpg', 'alberta3.jpg', 'alberta4.jpg'],
        'Regina': ['regina1.jpg', 'regina2.jpg', 'regina3.jpg', 'regina4.jpg'],
        'Hamilton': ['hamilton1.jpg', 'hamilton2.jpg', 'hamilton3.jpg', 'hamilton4.jpg']
    }

    # Check if the destination is in the dictionary
    if destination in destination_images:
        image_list = destination_images[destination]
        context = {'package': package, destination.lower() + '_images': image_list}
    else:
        # Handle other destinations
        context = {'package': package}

    return render(request, 'package/package_detail.html', context)


@login_required
def package_create(request):
    if not request.user.is_superuser and not (
            request.user.has_perm('management.view_package')
            or request.user.has_perm('management.add_package')
    ):
        return HttpResponseForbidden("You are not authorized to view this page")
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('package_list')
    else:
        form = PackageForm()
    return render(request, 'package/package_form.html', {'form': form})
