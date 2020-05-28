from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import logout
# Auth require to access views
from django.contrib.auth.decorators import login_required

# Models
from .models import Project

# ModelForms
from .forms import ProjectForm

# Create your views here.


@login_required
def index(request):
    projects = Project.objects.all()

    return render(request, 'project/index.html', {'projects': projects})


@login_required
def create(request):
    form = ProjectForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('projects.index')

    return render(request, 'project/create.html', {'form': form})


@login_required
def update(request, id):
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None,
                       request.FILES or None, instance=project)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('projects.index')

    return render(request, 'project/update.html', {'form': form})


@login_required
def delete(request, id):
    project = get_object_or_404(Project, pk=id)
    project.delete()

    return redirect('projects.index')


def logout_adm(request):
    logout(request)

    return redirect('login')
