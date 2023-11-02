from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from main_page.models import Menu, Review


def signupuser(request):
    menu = Menu.objects.all()
    if request.method == 'GET':
        return render(request, 'users/signupuser.html', {'form': UserCreationForm(), 'menu': menu})
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
                return redirect(request, 'users/signupuser.html',
                                {'form': UserCreationForm(),
                                 'error': 'Пользователь с таким именем уже существует!', 'menu': menu})

        else:
            return render(request, 'users/signupuser.html',
                          {'form': UserCreationForm(),
                           'error': 'Пароли не совпали', 'menu': menu})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('main_page:index')


def loginuser(request):
    menu = Menu.objects.all()
    if request.method == 'GET':
        return render(request, 'users/loginuser.html', {'form': AuthenticationForm(), 'menu': menu})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'users/loginuser.html', {'form': AuthenticationForm(),
                                                            'error': 'Неверные данные для входа!',
                                                            'menu': menu})
        else:
            login(request, user)
            return redirect('main_page:index')


@login_required
def user_profile(request):
    menu = Menu.objects.all()
    profile = request.user.profile
    reviews = profile.review_set.all()

    cart_prods_counter = request.user.shoppingcart_set.all()
    favourite_prods_counter = request.user.favourite_set.all()
    compare_prods_counter = request.user.compare_set.all()

    return render(request, 'users/profile.html', {
        'menu': menu,
        'profile': profile,
        'reviews': reviews,
        'cart_prods_counter': cart_prods_counter,
        'favourite_prods_counter': favourite_prods_counter,
        'compare_prods_counter': compare_prods_counter,
    })


@login_required(login_url='login')
def edit_profile(request):
    menu = Menu.objects.all()

    profile = request.user.profile
    edit_form = EditProfileForm(instance=profile)
    if request.method == 'POST':
        edit_form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if edit_form.is_valid():
            edit_form.save()

            messages.success(request, 'Account edited successfully!')
            return redirect('profile')

    context = {
        'edit_form': edit_form,
        'profile': profile,
        'menu': menu
    }
    return render(request, 'users/edit-profile.html', context)
