from django.shortcuts import render, redirect



def view(request):
	context = {}
	return render(request, 'home/index.html', context)