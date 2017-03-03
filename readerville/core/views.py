from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from accounts.forms import LoginForm


def home(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user = authenticate(username=login_form.username, password=login_form.password)
        if user is not None:
            login(request, user)
    return render(request, 'home.html', context={"login_form": login_form})
