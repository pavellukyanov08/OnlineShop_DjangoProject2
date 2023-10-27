from django.shortcuts import render
from main_page.models import Menu


def home_page(request):
    menu = Menu.objects.all()
    context = {'menu': menu}
    return render(request, 'home_page/home.html', context)
