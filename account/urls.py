from account.views import auth, manage

from django.urls import path
from django.contrib.auth import views as resetviews


urlpatterns = [

	path('', manage.profile, name='profile'),
	path('update/', manage.update, name='profile-update'),
	

	path('signin/', auth.signin, name='signin'),
	path('signup/', auth.signup, name='signup'),
	path('signout/', auth.signout, name='signout'),
	path('change-password/', auth.change_password, name='change_password'),
	
	path('password-reset/', resetviews.PasswordResetView.as_view(
		template_name='account/password/reset.html'),name='password_reset'),

    path('password-reset/done/', resetviews.PasswordResetDoneView.as_view(
    	template_name='account/password/reset-done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', resetviews.PasswordResetConfirmView.as_view(
    	template_name='account/password/reset-confirm.html'), name='password_reset_confirm'),

    path('password-reset-complete/', resetviews.PasswordResetCompleteView.as_view(
    	template_name='account/password/reset-complete.html'), name='password_reset_complete'),
]