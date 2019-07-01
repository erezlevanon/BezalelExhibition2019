from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:class_year>', views.year, name='year'),
    path('<int:class_year>/<str:name>', views.graduate, name='graduate'),
]
