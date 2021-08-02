from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name = "blog"),
    # Detectamos lo que hay entre las barras, lo guardamos como un parámetro, y lo pasaremos a la vista
    #Importante, lo pilla por defecto en cadena de caracteres, tenemos que forzar la conversión a entero
    path('category/<int:category_id>/', views.category, name='category')
]