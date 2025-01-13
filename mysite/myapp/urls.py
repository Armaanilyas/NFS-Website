from django.urls import path
from . import views
from myapp.views import Success, contact

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('Success/', Success, name='success'),

    ]
