from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
# Auth require to access views
from django.contrib.auth.decorators import login_required

# Models
from .models import Tech

# ModelForms
from .forms import TechForm

# Create your views here.


@login_required
def index(request):
    techs = Tech.objects.all()
    title = 'Tecnologias'

    return render(request, 'techs/index.html', {'techs': techs, 'title': title})


@login_required
def create(request):
    form = TechForm(request.POST or None)
    title = 'Criar tecnologia'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('techs.index')

    return render(request, 'techs/create.html', {'form': form})


@login_required
def update(request, id):
    tech = get_object_or_404(Tech, pk=id)
    form = TechForm(request.POST or None, instance=tech)
    title = 'Editar projeto'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('techs.index')

    return render(request, 'techs/update.html', {'form': form, 'title': title})


@login_required
def delete(request, id):
    tech = get_object_or_404(Tech, pk=id)
    tech.delete()

    return redirect('techs.index')


# Create your views here.
