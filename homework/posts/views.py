from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Product, Category

# Create your views here.


def main_view(request):
    return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method =='GET':
        category_id = int(request.GET.get('category_id', 0))
        if category_id:
            posts = Product.objects.filter(category__in=[category_id])
        else:
            posts = Product.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'posts/posts.html', context=context)


def post_detail_view(request, id):
    if request.method == 'GET':
        post = Product.objects.get(id=id)
        context = {
            'post': post,
            'reviews': post.reviews.all()
        }
        return render(request, 'posts/detail.html', context=context)


def show_categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories/categories.html', context=context)


