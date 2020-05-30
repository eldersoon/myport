# views file
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'layouts/site.html')


def test(request):
    return render(request, 'project/projects.html')
