from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from .models import ContactUs
from .forms import ContactUsForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


def services(request):
    return render(request, 'home.html')

    
def about(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            
            # name = form.cleaned_data.get('name')
            # phone = form.cleaned_data.get('phone')
            # email = form.cleaned_data.get('email')
            # message = form.cleaned_data.get('message')

            messages.info(request, "We'll touch in with you soon.")
            return redirect('home')
    else:
        form = ContactUsForm()
    return render(request, 'contact.html', {'form': form})

