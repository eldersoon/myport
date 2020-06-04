from django.urls import path

from .views import index, create, update, delete

urlpatterns = [
    path('home/', index, name='home.index'),
    path('home/create', create, name='home.create'),
    path('home/update/<int:id>', update, name='home.update'),
    path('home/delete/<int:id>', delete, name='home.delete')
]
