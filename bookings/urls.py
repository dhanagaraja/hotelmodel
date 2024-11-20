"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import index, booking, contact, testimonials, service, about, team, news_letter
from django.contrib.auth import views

admin.site.site_header = "HOTEL Niva Admin"
admin.site.site_title = "HOTEL Niva Admin Portal"
admin.site.index_title = "Welcome to HOTEL Niva Portal"

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('booking/', booking, name='booking'),
    path('contact/', contact, name='contact'),
    path('testimonials/', testimonials, name='testimonials'),
    path('service/', service, name='service'),
    path('team/', team, name='team'),
    path('news-letter/', news_letter, name='news_letter'),
]

