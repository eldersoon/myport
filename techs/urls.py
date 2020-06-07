from django.urls import path

from .views import index, create, update, delete

urlpatterns = [
    path('techs/', index, name='techs.index'),
    path('techs/create/', create, name='techs.create'),
    path('techs/update/<int:id>', update, name='techs.update'),
    path('techs/delete/<int:id>', delete, name='techs.delete'),
]
