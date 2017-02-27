from django import forms
from .models import UserProfile, Genre

class ProfileForm(forms.ModelForm):
	genres = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), required=True, queryset=Genre.objects.all())
	class Meta:
		model = UserProfile
		exclude = ['user']