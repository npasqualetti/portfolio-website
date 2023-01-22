from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)  

def about(request):
    context = {}
    return render(request, 'about.html', context)  

def contact(request):
    if request.method == 'POST':
        print(dir(request.POST))
        print(request.POST)
        send_mail(
            subject='Hi',
            message='Test',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['nick@technetconsultingllc.com']
        )
        messages.success(request, 'We have received your email. We will be in contact within 24 hours.')
        return redirect('/')
    context = {}
    return render(request, 'contact.html', context)  

def portfolio(request):
    context = {}
    return render(request, 'portfolio.html', context)  
