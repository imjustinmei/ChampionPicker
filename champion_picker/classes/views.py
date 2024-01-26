from django.shortcuts import render, redirect
from classes.models import Class

from champions.models import Champion
# Create your views here.


def index(request):
    classes = Class.objects.all()
    champions = Champion.classes.through.objects.select_related(
        'champion', 'class').all().order_by('class', 'champion')

    if champions.count() == 0:
        return redirect("/")

    context = {'classes': classes, 'champions': champions}

    return render(request, 'classes.html', context)
