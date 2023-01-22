from django.urls import path
from .views import (
    index,
    about,
    contact,
    portfolio,
    terms,
    privacy,
)


urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('portfolio/', portfolio, name="portfolio"),
    path('terms/', terms, name="terms"),
    path('privacy/', privacy, name="privacy"),
]
