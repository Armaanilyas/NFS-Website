
from django.shortcuts import render, redirect
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')
def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    if request.method == 'POST':
        return redirect('success')
    return render(request, 'myapp/contact.html')

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