from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from main_page.models import Menu


def signupuser(request):
    menu = Menu.objects.all()
    if request.method == 'GET':
        return render(request, 'authentication/signupuser.html', {'form': UserCreationForm(), 'menu': menu})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('main_page:index')
            except IntegrityError:
                return redirect(request, 'authentication/signupuser.html',
                                {'form': UserCreationForm(),
                                 'error': 'Пользователь с таким именем уже существует!', 'menu': menu})

        else:
            return render(request, 'authentication/signupuser.html',
                          {'form': UserCreationForm(),
                           'error': 'Пароли не совпали', 'menu': menu})


def logoutuser(request):

    if request.method == 'POST':
        logout(request)
        return redirect('main_page:index')


def loginuser(request):
    menu = Menu.objects.all()
    if request.method == 'GET':
        return render(request, 'authentication/loginuser.html', {'form': AuthenticationForm(), 'menu': menu})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'authentication/loginuser.html', {'form': AuthenticationForm(),
                                                                     'error': 'Неверные данные для входа!',
                                                                     'menu': menu})
        else:
            login(request, user)
            return redirect('main_page:index')
