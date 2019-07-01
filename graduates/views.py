from django.shortcuts import render

from django.http import HttpResponse

app_name = 'graduates'


def index(requset):
    return HttpResponse("Index")


def year(request, class_year):
    return HttpResponse("welcome to " + str(class_year))


def graduate(request, class_year, name):
    print('heyyyyyyyyy ' + str(class_year) + " " + name)
    return HttpResponse("Hello, world. You're at the polls index.")
