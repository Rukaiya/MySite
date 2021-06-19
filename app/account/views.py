from typing import Generic
from django.http import response
from django.shortcuts import redirect, render
from .forms import RegisterForm, LoginForm

# Create your views here.
 
def register(response):
    
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/accounts")
    else:
        form = RegisterForm()
    return render(response, "accounts/register.html", {"form": form})

def login(response):
    form = LoginForm(response.POST)
    return render(response, "registration/login.html", {"form": form})
