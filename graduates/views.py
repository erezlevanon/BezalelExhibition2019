from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Class, Graduate

app_name = 'graduates'
SESSION_GRADUATES_KEY = 'graduates'


def index(requset):
    viewed = requset.session.get(SESSION_GRADUATES_KEY, [])
    return HttpResponse(viewed)


def year(request, class_year):
    return redirect('/', permanent=True)


def graduate(request, class_year, name_en):
    y = Class.objects.get(year=class_year)
    cur_graduate = Graduate.objects.get(year=y, name_en__iexact=name_en)

    # Update visited graduates list.
    graduates_set = set(request.session.get(SESSION_GRADUATES_KEY, []))
    graduates_set.add(cur_graduate.name_en)
    request.session[SESSION_GRADUATES_KEY] = list(graduates_set)

    return render(request, 'graduates/graduate.html', {'graduate': cur_graduate})
