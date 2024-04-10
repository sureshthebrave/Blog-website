from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

# Create your views here.

def  register(request):


    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=email,first_name=username,email=email,password=password)
        user.save()

        return redirect('login')

    return render(request,"users/signup.html")





def  login_view(request):

    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)


        if user is not None:
            login(request,user)
            return redirect('home')

    return render(request,"users/login.html")


def logout_view(request):
    logout(request)
    return redirect('home')