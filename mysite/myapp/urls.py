from django.urls import path
from . import views
from myapp.views import Success, contact

from .views import search_perfumes



urlpatterns = [
    path('search/', search_perfumes, name='search_perfumes'),
    path('', views.ScentOfTheSeason, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('Success/', Success, name='success'),

path('spring/', views.spring, name='spring'),
    path('summer/', views.summer, name='summer'),
    path('autumn/', views.autumn, name='autumn'),
    path('winter/', views.winter, name='winter'),

    ]
