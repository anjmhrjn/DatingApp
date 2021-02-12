from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'Landing/home.html')


def login(request):
    return render(request, 'Landing/login.html')


def register(request):
    return render(request, 'Landing/register.html')
