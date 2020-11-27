from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == "POST":
        if request.POST["passwd1"] == request.POST["passwd2"]:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["passwd1"])
            auth.login(request,user)
            return redirect('index')
        return render(request,'accounts/signup.html')
    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        passwd = request.POST["passwd"]
        user = auth.authenticate(request, username=username, passwd=passwd)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or passwd is incorrect'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')
# Create your views here.
