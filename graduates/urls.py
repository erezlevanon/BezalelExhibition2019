from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:year>', views.year, name='year'),
    path('<int:year>/<str:name>', views.graduate, name='graduate'),
]
