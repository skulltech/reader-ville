from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^accounts/profile', views.edit_profile, name='edit_profile'),
	url(r'^accounts/libraries', views.view_library, name="view_library")
]