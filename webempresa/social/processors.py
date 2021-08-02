from .models import Link

#Vamos a extender el contexto para poner las redes sociales mediante un procesador de contexto

def ctx_dict(request):
    #Creamos un diccionario con las redes sociales, con sus claves (key) y sus valores (url)
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx