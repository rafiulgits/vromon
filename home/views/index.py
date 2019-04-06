from django.shortcuts import render, redirect

from home.models import Hotel, Restaurant, Place
def view(request):
	context = {}

	hotels = Hotel.objects.all().order_by('-geo_lat').order_by('-geo_lng')[:3]
	restaurants = Restaurant.objects.all().order_by('-geo_lat').order_by('-geo_lng')[:3]
	places = Place.objects.all().order_by('-geo_lat').order_by('-geo_lng')[:3]

	context['hotels'] = hotels
	context['restaurants'] = restaurants
	context['places'] = places
	
	return render(request, 'home/index.html', context)