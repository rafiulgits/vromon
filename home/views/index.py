from django.shortcuts import render, redirect

from home.models import Spot


def view(request):
	context = {}
	spots = Spot.objects.all()[:6]
	context['spots'] = spots
	return render(request, 'home/index.html', context)