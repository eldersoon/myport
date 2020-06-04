from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Home

# ModelForms
from .forms import HomeForm

# Create your views here.


# create, update, delete, edit ...

def index(request):
    home = Home.objects.first()
    title = 'Seção Início'

    return render(request, 'home/index.html', {'home': home, 'title': title})


def create(request):
    form = HomeForm(request.POST or None, request.FILES or None)
    title = 'Criar conteúdo da home'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home.index')

    return render(request, 'home/create.html', {'form': form, 'title': title})


def update(request, id):
    home = get_object_or_404(Home, pk=id)
    form = HomeForm(request.POST or None,
                    request.FILES or None, instance=home)
    title = 'Editar conteúdo da Home'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home.index')

    return render(request, 'home/update.html', {'form': form, 'title': title})


def delete(request, id):
    home = get_object_or_404(Home, pk=id)
    home.delete()

    return redirect('home.index')
