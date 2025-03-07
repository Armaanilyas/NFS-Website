from django.shortcuts import render, redirect
from forms import ContactForm
from django.http import HttpResponse


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def Success(request):
    return render(request, 'mysite/myapp/templates/myapp/Success.html')