from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Class, Graduate

app_name = 'graduates'
SESSION_GRADUATES_KEY = 'graduates'


def index(request):
    viewed = request.session.get(SESSION_GRADUATES_KEY, [])
    visited_graduates = Graduate.objects.filter(name_en__in=viewed)
    graduates = Graduate.objects.all().order_by("name_he")
    return render(request, 'graduates/index.html', {
        'has_visited': visited_graduates.__len__() > 0,
        'visited_graduates': visited_graduates,
        'graduates': graduates,
    })


def year(request, class_year):
    return redirect('/', permanent=True)


def instagram_helper(instagram):
    if not instagram:
        return False
    return 'http://www.instagram.com/' + instagram.split('/')[-1]


def website_helper(website):
    if not website:
        return False
    if not str(website).startswith('http'):
        return 'http://' + website
    return website


def graduate(request, class_year, name_en):
    y = Class.objects.get(year=class_year)
    cur_graduate = Graduate.objects.get(year=y, name_en__iexact=name_en)

    # Update visited graduates list.
    graduates_set = set(request.session.get(SESSION_GRADUATES_KEY, []))
    graduates_set.add(cur_graduate.name_en)
    request.session[SESSION_GRADUATES_KEY] = list(graduates_set)

    return render(request, 'graduates/graduate.html', {
        'graduate': cur_graduate,
        'instagram': instagram_helper(cur_graduate.instagram),
        'website': website_helper(cur_graduate.personal_website),
    })
