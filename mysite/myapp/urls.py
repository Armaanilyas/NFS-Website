from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('Spring', views.Spring, name='Spring Perfume Recommendations'),

    path('Summer', views.Summer, name='Summer Recommendations'),
    path('Winter', views.Winter, name='Winter Recommendations'),
    path('Fall', views.Autumn, name='Autumn Recommendations'),
    ]
