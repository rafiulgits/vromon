from django.shortcuts import render, redirect



def list(request):
	context = {}
	return render(request, 'home/index.html', context)


def detail(request, uid):
	context = {}
	return render(request, 'home/index.html', context)


def create(request, name):
	context = {}
	return render(request, 'home/index.html', context)