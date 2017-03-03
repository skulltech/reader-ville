from django import forms
from django.urls import reverse
from .models import Book
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['libraries']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'bookForm'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('view_library')
        self.helper.add_input(Submit('submit', 'Add Book'))