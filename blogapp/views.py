from django.shortcuts import render,redirect
from .models import Category,Post
# Create your views here.

def blog(request):

    posts = Post.objects.filter(is_published=True)
    categories = Category.objects.all()

    context = {
        'posts':posts,
        'categories':categories,
    }


    return render(request,"blog/blog.html",context)


def post(request,title):
    post = Post.objects.get(title=title)
    categories = Category.objects.all()
    context = {
        'post':post,
        'categories':categories,
    }
    return render(request,"blog/post.html",context)


def search_view(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')


        posts = Post.objects.filter(title__icontains=keyword)
        categories = Category.objects.all()

        context = {
            'posts':posts,
            'categories':categories,
        }

    return render(request,"blog/blog.html",context)


def get_category(request,cat):
    category = Category.objects.get(name=cat)
    posts = Post.objects.filter(category=category)
    categories = Category.objects.all()
    context = {
        'posts':posts,
        'categories':categories,
    }
    return render(request,"blog/categories.html",context)