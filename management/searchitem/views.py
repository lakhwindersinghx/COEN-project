from management.package.models import Package
from django.shortcuts import render

# def index(request):
#     return render(request, 'index.html')
# # class PackageView(ListView):
# #     model = Post
def search_results(request):
    query = request.GET.get('q')
    results = None
    if query:
        results = results = Package.objects.filter(destination__icontains=query)
    return render(request, 'searchresult/search_results.html', {'results': results, 'query': query})
