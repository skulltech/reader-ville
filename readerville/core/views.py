from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import ProfileForm, LoginForm, BookForm
from .models import UserProfile, Library

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

@login_required(login_url='/accounts/login')
def view_library(request):
    try:
        library = request.user.library
    except Library.DoesNotExist:
        library = Library(user=request.user)
        library.save()

    books = library.book_set.all()

    book_form = BookForm(request.POST or None)
    if book_form.is_valid():
        book = book_form.save(commit=False)
        book.library = library
        book.save()

    return render(request, 'profile/view-library.html', context={"book_form": book_form, "books": books})