from django.shortcuts import render

from django.http import HttpResponse

app_name = 'graduates'

def index(requset):
    return HttpResponse("Index")

def year(request, year):
    return HttpResponse("welcome to " + str(year))

def graduate(request, year, name):
    print('heyyyyyyyyy ' + str(year) + " " + name)
    return HttpResponse("Hello, world. You're at the polls index.")
