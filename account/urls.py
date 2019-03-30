from account.views import auth

from django.urls import path


urlpatterns = [

	path('signin/', auth.signin, name='signin'),
	path('signup/', auth.signup, name='signup'),
	path('signout/', auth.signout, name='signout'),
]