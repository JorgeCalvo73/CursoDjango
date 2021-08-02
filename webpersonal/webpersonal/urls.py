"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

# Importamos las vistas que tenemos en la app core (fichero views). 
from core import views as core_views

# Importamos las vistas que tenemos en la app fortfolio (fichero views). 
from portfolio import views as portfolio_views

from django.conf import settings

# Aquí es donde se ponen las urls de la aplicación. 
urlpatterns = [
    path('admin/', admin.site.urls),

    # Página principal de la aplicación
    path('', core_views.home, name='home'),

    # Página about me
    path('about-me/', core_views.about, name='about'),

    # Página portafolio
    path('portfolio/', portfolio_views.portfolio, name = 'portfolio'),

    # Página de contacto
    path('contact/', core_views.contact, name = 'contact')
]

# COnfiguración adicional para poder visualizar archivos media en entorno de desarrollo
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
