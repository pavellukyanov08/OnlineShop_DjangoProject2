from django.shortcuts import render
from main_page.models import Menu


def home_page(request):
    menu = Menu.objects.all()

    return render(request, 'home_page/home_page.html',
                  {'menu': menu})
