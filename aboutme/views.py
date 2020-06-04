from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Aboutme

# ModelForms
from .forms import AboutmeForm

# Create your views here.


# create, update, delete, edit ...

def index(request):
    aboutme = Aboutme.objects.first()
    title = 'Seção sobre mim'

    return render(request, 'aboutme/index.html', {'aboutme': aboutme, 'title': title})


def create(request):
    form = AboutmeForm(request.POST or None, request.FILES or None)
    title = 'Criar conteúdo sobre mim'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('aboutme.index')

    return render(request, 'aboutme/create.html', {'form': form, 'title': title})


def update(request, id):
    aboutme = get_object_or_404(Aboutme, pk=id)
    form = AboutmeForm(request.POST or None,
                       request.FILES or None, instance=aboutme)
    title = 'Editar conteúdo sobre mim'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('aboutme.index')

    return render(request, 'aboutme/update.html', {'form': form, 'title': title})


def delete(request, id):
    Aboutme = get_object_or_404(Aboutme, pk=id)
    Aboutme.delete()

    return redirect('aboutme.index')
