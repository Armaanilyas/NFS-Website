
from django.shortcuts import render, redirect
from datetime import datetime, timezone
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from django.db import models
from .models import Perfume, Season, Contact
from django.db.models import Q
# Create your views here.

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
def index(request):
    season = ScentOfTheSeason
    return render(request, 'myapp/index.html', {'season': season})
def about(request):
    return render(request, 'myapp/about.html')


def spring(request):
    return render(request, 'myapp/spring.html')

def summer(request):
    return render(request, 'myapp/summer.html')

def autumn(request):
    return render(request, 'myapp/autumn.html')

def winter(request):
    perfume = Perfume.objects.get(name='Guerlain Oud Kohl')
    return render(request, 'myapp/winter.html', {'perfume': perfume})

def recommendations(request, season):
    season_obj = Season.objects.get(name=season)
    perfumes = Perfume.objects.filter(seasons=season_obj)
    context = {
        'season': season,
        'perfumes': perfumes
    }
    return render(request, 'your_app/recommendations.html', context)
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            Contact.objects.create(
                name=name,
                email=email,
                message=message,
            )

            # First email (to admin)
            send_mail(
                subject=f'New Contact form message from {name}',
                message=f'From: {name}\nEmail: {email}\nMessage: {message}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False
            )

            # Second email (confirmation to user)
            send_mail(
                subject=f'Thank you for contacting NFS Perfumery',
                message=f'Dear {name}, Thank you for your message, We have received it, and will get back to you in due course. '
                        f'\n\n Regards, \n NFS Perfumery Team',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )

            return redirect('success')
    else:
        form = ContactForm()

    return render(request, template_name='myapp/contact.html', context={'form': form})


def ScentOfTheSeason(request):

    month = 9
    #month = datetime.now().month
    if month in [12, 1, 2]:
        season = "winter"
    elif month in [3, 4, 5]:
        season = "spring"
    elif month in [6, 7, 8]:
        season = "summer"
    else:
        season = "autumn"


    return render(request, 'myapp/index.html', {'season': season})


def Success(request):
 latest_contact = Contact.objects.latest('id')
 return render(request, template_name='myapp/success.html', context={'email': latest_contact.email})

def search_perfumes(request):
    query = request.GET.get('q', '')
    if query:
        perfumes = Perfume.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        perfumes = Perfume.objects.none()

    return render(request, 'myapp/search_results.html',{
        'perfumes': perfumes,
        'query': query

    })
