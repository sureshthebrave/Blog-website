from django.shortcuts import render,redirect
from django.http import HttpResponse
from blogapp.models import Category,Post
from .models import Contact

def home(request):
    posts = Post.objects.filter(is_published=True)
    categories = Category.objects.all()

    context = {
        'posts':posts,
        'categories':categories,
    }

    return render(request,"index.html",context)

def about(request):
    return render(request,"pages/about.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        c = Contact(name=name,email=email,subject=subject,message=message)
        c.save()
        return redirect('contact')

    return render(request,"pages/contact.html")


