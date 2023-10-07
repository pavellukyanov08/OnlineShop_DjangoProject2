from django.shortcuts import render
from main_page.models import Menu


def about(request):
    menu = Menu.objects.all()
    return render(request, 'about/about.html', {'menu': menu})
