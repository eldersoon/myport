"""myport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView as login, LogoutView as logout

from .views import site, test, logout_adm, admin_site
from projects import urls as projects_url
from home import urls as home_url
from aboutme import urls as aboutme_url
from techs import urls as techs_url

# Development only:
from django.conf import settings
from django.conf.urls.static import static
# ADD: + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# TO END OF urlpatterns[]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('vsfv/', admin.site.urls),
    path('login/', login.as_view(), name='login'),
    path('logout/', logout_adm, name='logout'),
    path('', site, name='site'),
    path('dimim/dashboard', admin_site, name='dashboard'),
    path('dimim/', include(projects_url)),
    path('dimim/', include(home_url)),
    path('dimim/', include(aboutme_url)),
    path('dimim/', include(techs_url)),
    path('test/', test, name='test'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
