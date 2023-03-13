"""Hello URL Configuration

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
from django.urls import path, include
from home import views
from django.urls import path


urlpatterns = [
    path("", views.index, name='index'),
    path("index", views.index, name='index'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("booking", views.booking, name='booking'),
    path("destination", views.destination, name='Destination'),
    path("contact", views.contact, name='contact'),
    path("signup", views.signup, name='signup'),
    path("login", views.login, name='login'),
    path("logout", views.logout_view, name='logout'),
    path("search", views.search, name='search'),
    path("terms", views.terms, name='terms'),
    path("privacy-policy", views.privacy, name='privacy-policy'),
    path("password_change", views.password_change, name="password_change"),

]
