from django.shortcuts import render
from django.views.generic import CreateView


def site_view(request):
    return render(request, 'studios/main.html', {})
