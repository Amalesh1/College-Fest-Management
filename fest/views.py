from django.shortcuts import render, HttpResponse
from fest.models import Contact, Register
from django.contrib import messages
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')

        contact = Contact(name=name, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Response recorded')
    return render(request, 'contact.html')
    

def events(request):
    return render(request, 'events.html')
    

def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        event = request.POST.get('event')
        register=Register(name=name, email=email, phone=phone, event=event, date=datetime.today())
        register.save()
        messages.success(request, 'Response recorded!')
    return render(request, 'register.html')

