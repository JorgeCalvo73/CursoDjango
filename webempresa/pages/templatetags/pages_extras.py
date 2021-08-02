from django import template
from pages.models import Page


# Tenemos que registrar el template tag que acabamos de crear en la librería de templates
register = template.Library()

# Esto es lo que vamos a devolver al template en forma de template tag
@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages