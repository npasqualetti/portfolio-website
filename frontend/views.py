from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    title = "Expert Website Development Consulting - Create a Stunning Website Today"
    meta_desciption = "Take your online presence to the next level with our professional website development consulting services. From design to launch, we'll help you create a stunning website that drives business growth."
    context = {
        'title': title,
        'meta_description': meta_desciption,
    }
    return render(request, 'index.html', context)  

def about(request):
    title = "Get to Know Our Website Development Team - Technet Consulting LLC"
    meta_desciption = "Learn more about our experienced and dedicated website development team. With years of experience, we're committed to helping businesses achieve online success. Read more about us and our approach to website development."
    context = {
        'title': title,
        'meta_description': meta_desciption,
    }
    return render(request, 'about.html', context)  

def contact(request):
    if request.method == 'POST':
        email = (request.POST.get("email"))
        subject = (request.POST.get("subject"))
        message = (request.POST.get("message"))
        send_mail(
            subject=subject,
            message=f"{email} \n {message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['nick@technetconsultingllc.com']
        )
        messages.success(request, 'We have received your email. We will be in contact within 24 hours.')
        return redirect('/contact/#contact-form')
    title = "Get in Touch with Our Website Development Team - Technet Consulting LLC"
    meta_desciption = "Need help with your website development project? Contact us today and one of our experienced consultants will be in touch. We're here to answer any questions you may have and help you achieve your online goals."
    context = {
        'title': title,
        'meta_description': meta_desciption,
    }
    return render(request, 'contact.html', context)  

def portfolio(request):
    title = "View Our Latest Website Development Projects - Technet Consulting LLC"
    meta_desciption = "Check out our portfolio and see for yourself the high-quality website development projects we've completed for our clients. From small business websites to complex e-commerce solutions, we have the skills and experience to deliver exceptional results."
    context = {
        'title': title,
        'meta_description': meta_desciption,
    }
    return render(request, 'portfolio.html', context)  

def terms(request):
    title = "Terms of Service - Technet Consulting LLC"
    meta_desciption = "Read our terms and conditions before engaging with our website development consulting services. Learn more about our terms of use, service and privacy policy."
    context = {
        'title': title,
        'meta_description': meta_desciption,
    }
    return render(request, 'terms.html', context)  

def privacy(request):
    title = "Privacy Policy - Technet Consulting LLC"
    meta_desciption = "Read our privacy policy to understand how we collect, use and protect your personal information when you engage with our website development consulting services."
    context = {
        'title': title,
        'meta_description': meta_desciption,
    }
    return render(request, 'privacy.html', context)  
