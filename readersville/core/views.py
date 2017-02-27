from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

# Create your views here.

@login_required(login_url='accounts/login/')
def home(request):
	return render(request, 'home.html')

@login_required(login_url='accounts/login/')
def view_profile(request):
	return render(request, 'profile/view-profile.html')

@login_required(login_url='accounts/login/')
def edit_profile(request):
	form = ProfileForm(request.POST or None)
	if form.is_valid():
		    profile = form.save(commit=False)
		    profile.user = request.user
		    profile.save()

	return render(request, 'profile/edit-profile.html', context={"profile_form": form})