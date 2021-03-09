from django.contrib import admin
from django.urls import path, include
from fest import views


urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("events", views.events, name="events"),
    path("register", views.register, name="register"),
]
