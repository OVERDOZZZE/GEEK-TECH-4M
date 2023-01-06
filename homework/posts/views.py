from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Product, Category, Reviews
from .forms import ProductCreateForm, CommentCreateForm
from .constants import PAGINATION_LIMIT
# Create your views here.


def main_view(request):
    return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method == 'GET':
        category_id = int(request.GET.get('category_id', 0))
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if category_id:
            posts = Product.objects.filter(category__in=[category_id])
        else:
            posts = Product.objects.all()

        max_page = posts.__len__() / PAGINATION_LIMIT

        if round(max_page) < max_page:
            max_page = round(max_page) + 1

        max_page = int(max_page)
        posts = posts[PAGINATION_LIMIT * (page-1):PAGINATION_LIMIT * page]

        if search:
            posts = posts.filter(title__icontains=search)

        context = {
            'posts': posts,
            'user': None if request.user.is_anonymous else request.user,
            'max_page': range(1, max_page + 1)
        }
        return render(request, 'posts/posts.html', context=context)


def post_detail_view(request, id):
    if request.method == 'GET':
        post = Product.objects.get(id=id)
        context = {
            'post': post,
            'reviews': post.reviews.all(),
            'comment_form': CommentCreateForm
        }
        return render(request, 'posts/detail.html', context=context)

    if request.method == 'POST':
            post = Product.objects.get(id=id)
            form = CommentCreateForm(data=request.POST)

            if form.is_valid():
                Reviews.objects.create(
                    author=request.user,
                    post_id=id,
                    text=form.cleaned_data.get('text')
                )
                return redirect(f'/posts/{id}/')
            else:
                return render(request, 'posts/detail.html',context={
                    'post': post,
                    'reviews': post.reviews.all(),
                    'cats': post.categories.all(),
                    'comment_form': form
                })


def show_categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories/categories.html', context=context)


def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'posts/create_product.html', context={'form': ProductCreateForm})

    context = {
        'title_error': 'Минимальное значение title - 8'
    }

    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)

        if form.is_valid():
            Product.objects.create(
                author=request.user,
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
                rate=form.cleaned_data.get('rate', 0),
                commentable = form.cleaned_data.get('commentable', True)
            )
            return redirect('/posts/')
        else:
            return render(request, 'posts/create.html', context={'form': form})