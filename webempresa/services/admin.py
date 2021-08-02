from django.contrib import admin
from .models import Service
# Register your models here.

# Cambiamos la configuración del panel de admin para que los ampos created y updated sean de sólo lectura
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# Registramos el servicio y su configuración
admin.site.register(Service, ServiceAdmin)