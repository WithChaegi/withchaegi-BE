from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import auth
from django.contrib.auth.models import User

from .forms import UserCreateForm, SignUpForm

def signup_view(request):
    if request.method == 'GET':
        form = SignUpForm
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        form = SignUpForm(request.POST)

        if form.is_valid():
            instance = form.save()
            return redirect('main')
        else:
            return redirect('accounts:signup')
    # if request.method == 'POST':
    #     if request.POST['password1'] == request.POST['password2']:
    #         user = User.objects.create_user(
    #             username=request.POST['username'],
    #             password=request.POST['password1'],
    #             email=request.POST['email'],
    #         )
    #         auth.login(request, user)
    #         return redirect('/')
        
    # return render(request, 'accounts/signup.html')
        
def login_view(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'form': AuthenticationForm()})
    else:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            return redirect('main')
        else:
            return render(request, 'accounts/login.html', {'form': form})
    # if request.method == 'POST':
    #     username = request.POST["username"]
    #     password = request.POST["password"]
    #     user = auth.authenticate(request, username=username,password=password)
    #     if user is not None:
    #         auth.login(request, user)
    #         return redirect(request, 'login')
    # return render(request, 'accounts/login.html')
        
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('main')