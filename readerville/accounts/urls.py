from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.edit_profile, name='edit_profile'),
]