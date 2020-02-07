from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = KorisniciForm(request.POST)
        if form.is_valid():    
            form.save()
            messages.success(request, f'Registracija uspješna! Možete se prijaviti.')
            return redirect('login')
    else:
        form = KorisniciForm()
    return render(request, 'users/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = KorisniciLogin(request.POST)
        if form.is_valid():    
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Welcome!')
            return redirect('Sustav-Početna')
    else:
        form = KorisniciLogin()
    return render(request, 'users/login.html', {'form': form})

