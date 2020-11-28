# views file
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout

from home.models import Home
from aboutme.models import Aboutme
from techs.models import Tech
from projects.models import Project

from django.contrib.auth.decorators import login_required


def site(request):
    home = Home.objects.first()
    aboutme = Aboutme.objects.first()
    techs = Tech.objects.all()
    projects = Project.objects.all()

    return render(request, 'layouts/site.html', {
        'home': home,
        'aboutme': aboutme,
        'techs': techs,
        'projects': projects
    })

@login_required
def admin_site(request):
    title = 'Dashboard'
    return render(request, 'layouts/dashboard.html', {'title': title})


def test(request):
    return render(request, 'project/projects.html')


def logout_adm(request):
    logout(request)

    return redirect('login')
