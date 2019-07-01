from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from .models import Class, Graduate

app_name = 'graduates'


def index(requset):
    return HttpResponse("Index")


def year(request, class_year):
    return HttpResponse("welcome to " + str(class_year))


def graduate(request, class_year, name):
    y = Class.objects.get(year=class_year)
    cur_graduate = Graduate.objects.get(year=y, name=name)
    return render(request, 'graduates/graduate.html', {'graduate': cur_graduate})
