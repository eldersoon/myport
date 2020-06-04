# views file
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout

from home.models import Home
from aboutme.models import Aboutme


def site(request):
    home = Home.objects.first()
    aboutme = Aboutme.objects.first()
    return render(request, 'layouts/site.html', {
        'home': home,
        'aboutme': aboutme,
    })


def admin_site(request):
    title = 'Dashboard'
    return render(request, 'layouts/dashboard.html', {'title': title})


def test(request):
    return render(request, 'project/projects.html')


def logout_adm(request):
    logout(request)

    return redirect('login')
