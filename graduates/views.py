from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Class, Graduate

app_name = 'graduates'
SESSION_GRADUATES_KEY = 'graduates'


def index(request):
    viewed = request.session.get(SESSION_GRADUATES_KEY, [])
    visited_graduates = Graduate.objects.filter(name_en__in=viewed)
    return HttpResponse(visited_graduates)


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
