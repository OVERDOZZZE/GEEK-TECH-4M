from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Product

# Create your views here.


def main_view(request):
    return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method =='GET':
        posts = Product.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'posts/posts.html', context=context)
