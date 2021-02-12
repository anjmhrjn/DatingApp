from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import ExtendedUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'Landing/main.html')


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                first_time = [eu.first_login for eu in ExtendedUser.objects.filter(user=user)]
                messages.success(request, f'Logged in as {username}!')
                if first_time[0]:
                    return redirect('First')
                else:
                    return redirect('Dash')

                return redirect('Home')
            else:
                messages.warning(request, f'Invalid Credentials!')
                return render(request, 'Landing/main.html')
    return render(request, 'Landing/main.html')


def submit(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    username = request.POST.get('reg-username')
    contact = request.POST.get('contact')
    address = request.POST.get('address')
    email = request.POST.get('email')
    password = request.POST.get('reg-password')

    user = User.objects.create_user(username=username, password=password, first_name=fname, last_name=lname, email=email)
    newExtendedUser = ExtendedUser(phone=contact, address=address, user=user)
    newExtendedUser.save()
    messages.success(request, f'Yay! Data submitted successfully.')
    return render(request, 'Landing/Main.html')
