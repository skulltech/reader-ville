from django import forms
from .models import UserProfile, Genre

class ProfileForm(forms.ModelForm):
	genres = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), required=True, queryset=Genre.objects.all())
	class Meta:
		model = UserProfile
		exclude = ['user']

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=50)
	password = forms.CharField(label='Password', max_length=50)