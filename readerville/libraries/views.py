from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from .models import Library


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