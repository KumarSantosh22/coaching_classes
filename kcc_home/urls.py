from django.urls import path
from . import views

urlpatterns = [
    # Home urls
    path('', views.home, name='home'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]
