from .views import index, create, update, delete
from django.urls import path

urlpatterns = [
    path('about/', index, name='aboutme.index'),
    path('about/create', create, name='aboutme.create'),
    path('about/update/<int:id>', update, name='aboutme.update'),
    path('about/delete/<int:id>', delete, name='aboutme.delete')
]
