from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'trackerApp/base_index.html', {})
