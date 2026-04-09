
# Create your views here.
from django.shortcuts import render, redirect
from .models import Registration
from django.contrib import messages
import re

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # validation
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messages.error(request, "Invalid Email")
        elif not re.match(r"^[6-9]\d{9}$", phone):
            messages.error(request, "Invalid Phone")
        else:
            Registration.objects.create(name=name, email=email, phone=phone)
            messages.success(request, "Registered Successfully!")
            return redirect('myevents')

    return render(request, 'register.html')

def myevents(request):
    events = Registration.objects.all()
    return render(request, 'myevents.html', {'events': events})