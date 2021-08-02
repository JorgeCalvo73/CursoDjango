from django.shortcuts import render
from .models import Service

# Create your views here.

def services(request):

    #Saco la lista de servicios que he metido en el panel de administrador y los guardo en services
    services = Service.objects.all()

    #Devuelvo dicha lista de servicios
    return render(request, "services/services.html", {'services' : services})