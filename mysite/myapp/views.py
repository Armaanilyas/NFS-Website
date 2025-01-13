
from django.shortcuts import render, redirect
from datetime import datetime
from django import forms
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
def index(request):
    return render(request, 'myapp/index.html')
def about(request):
    return render(request, 'myapp/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

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

    month = datetime.now().month
    if month in [12, 1, 2]:
        season = "Winter"
    elif month in [3, 4, 5]:
        season = "Spring"
    elif month in [6, 7, 8]:
        season = "Summer"
    else:
        season = "Autumn"


    return render(request, 'myapp/index.html', {'season': season})

def Success(request):
    return render(request, 'myapp/Success.html')