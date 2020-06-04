from django.urls import path

from .views import index, create, update, delete

# Development only:
# from django.conf import settings
# from django.conf.urls.static import static
# ADD: + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# TO END OF urlpatterns[]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('projects/', index, name='projects.index'),
    path('create/', create, name='projects.create'),
    path('update/<int:id>', update, name='projects.update'),
    path('delete/<int:id>', delete, name='projects.delete'),
]
