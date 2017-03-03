from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import UserProfile

@login_required(login_url='accounts/login/')
def view_profile(request):
    return render(request, 'profile/view-profile.html')

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    profile_form = ProfileForm(request.POST or None, instance=profile)
    if profile_form.is_valid():
        profile_form.save()

    return render(request, 'profile/edit-profile.html', context={"profile_form": profile_form})