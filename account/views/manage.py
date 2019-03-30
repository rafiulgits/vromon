from django.shortcuts import render, redirect
from account.models import Account


def profile(request):
	context = {}
	user = request.user
	return render(request, 'account/profile/view.html',context)


def update(request):
	context = {}
	return render(request, 'account/profile/update.html',context)



def dashboard(request):
	context = {}
	return render(request, 'account/profile/guide-dash.html',context)