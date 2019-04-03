from django.shortcuts import render, redirect

from home.models import Spot, Event


def view(request):
	context = {}
	spots = Spot.objects.all()[:6]
	events = Event.objects.all()[:6]

	context['spots'] = spots
	context['events'] = events
	
	return render(request, 'home/index.html', context)