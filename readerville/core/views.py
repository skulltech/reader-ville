from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import ProfileForm, LoginForm
from .models import UserProfile

# Create your views here.

def home(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user = authenticate(username=login_form.username, password=login_form.password)
        if user is not None:
            login(request, user)
    return render(request, 'home.html', context={"login_form": login_form})

@login_required(login_url='accounts/login/')
def view_profile(request):
    return render(request, 'profile/view-profile.html')

@login_required(login_url='accounts/login/')
def edit_profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    profile_form = ProfileForm(request.POST or None, instance=profile)
    if profile_form.is_valid():
        profile_form.save()

    return render(request, 'profile/edit-profile.html', context={"profile_form": profile_form})