from django.shortcuts import render, redirect



def list(request):
	context = {}
	return render(request, 'home/index.html', context)


def detail(request, name):
	context = {}
	return render(request, 'home/index.html', context)