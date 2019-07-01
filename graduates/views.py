from django.shortcuts import render

from django.http import HttpResponse
from .models import Class, Graduate

app_name = 'graduates'


def index(requset):
    return HttpResponse("Index")


def year(request, class_year):
    return HttpResponse("welcome to " + str(class_year))


def graduate(request, class_year, name):
    y = Class.objects.get(year=class_year)
    g = Graduate.objects.get(year=y, name=name)
    return HttpResponse("Hello, world. You're at the polls index.")
