from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
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
    title = 'Projetos'

    return render(request, 'project/index.html', {'projects': projects, 'title': title})


@login_required
def create(request):
    form = ProjectForm(request.POST or None, request.FILES or None)
    title = 'Criar projeto'

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
    title = 'Editar projeto'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('projects.index')

    return render(request, 'project/update.html', {'form': form, 'title': title})


@login_required
def delete(request, id):
    project = get_object_or_404(Project, pk=id)
    project.delete()

    return redirect('projects.index')
