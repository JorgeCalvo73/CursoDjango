from django.contrib import admin
from .models import Category, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields =('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    #Distintos campos para poder personalizar el panel de administrador
    readonly_fields =('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    #Creamos un campo personalizado y lo llamamos en list_display
    #Ese obj hace referencia a cada fila que queremos mostrar
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    
    #De esta manera cambiamos el nombre que se muestra en post_categories
    post_categories.short_description = "Categorías"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)