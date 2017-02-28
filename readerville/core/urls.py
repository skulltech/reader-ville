from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^profile/edit/', views.edit_profile, name='edit_profile')
]