from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from landing.models import Interest, ExtendedUser


# Create your views here.
def dashboard(request):
    return render(request, 'user/profile_landing.html')


def firstTime(request):
    if request.method == 'POST':
        preference = request.POST.get("preference")
        gender = request.POST.get("gender")
        bio = request.POST.get("bio")
        user_hobbies = request.POST.get("hobby")
        rating = request.POST.get("rating")
        photo = request.POST.get("photo")
        print(request.user)
        print(ExtendedUser.objects.filter(user=request.user))
        ExtendedUser.objects.filter(user=request.user).update(
            gender=gender,
            bio=bio,
            preferences=preference,
            photo=photo,
            first_login=False
        )
        return redirect('Dash')

    hobby = Interest.objects.all()
    context = {
        "hobbies": hobby,
    }
    return render(request, 'user/first_time.html', context)


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect('Home')
