from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Class, Graduate

app_name = 'graduates'


def index(requset):
    return HttpResponse("Index")


def year(request, class_year):
    return redirect('/', permanent=True)


def graduate(request, class_year, name_en):
    y = Class.objects.get(year=class_year)
    cur_graduate = Graduate.objects.get(year=y, name_en__iexact=name_en, )
    return render(request, 'graduates/graduate.html', {'graduate': cur_graduate})
