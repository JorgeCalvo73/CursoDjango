from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.

def blog(request):
    posts = Post.objects.all()

    return render(request, "blog/blog.html", {'posts' : posts})

def category(request, category_id):
    """
    #El get nos permite recoger un solo registro filtrando
    category = get_object_or_404(Category, id=category_id)
    
    Esta sería una manera un poco rudimentaria de hacerlo, pero valdría
    #Pasamos los posts filtrando por categoría
    posts = Post.objects.filter(categories = category)

    return render(request, "blog/category.html", {'category': category, 'posts': posts})
    """
    category = get_object_or_404(Category, id=category_id)

    return render(request, "blog/category.html", {'category': category})