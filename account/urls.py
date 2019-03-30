from account.views import auth, manage

from django.urls import path
from django.contrib.auth import views as resetview


urlpatterns = [

	path('', manage.profile, name='profile'),
	path('update/', manage.update, name='profile-update'),
	path('dashboard/', manage.dashboard, name='dashboard'),

	path('signin/', auth.signin, name='signin'),
	path('signup/', auth.signup, name='signup'),
	path('signout/', auth.signout, name='signout'),
]