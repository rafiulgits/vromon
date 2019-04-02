from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, HttpResponse

from home.models import Spot,SpotGallery,SpotGuide


def list(request):
	context = {}
	spots = Spot.objects.all()
	context['spots'] = spots
	return render(request, 'home/spot/list.html', context)


def detail(request, name):
	context = {}
	try:
		spot = Spot.objects.get(name__iexact=name)
		gallery = SpotGallery.objects.filter(spot_id=spot.uid)
		guides = SpotGuide.objects.filter(spot_id=spot.uid)
		context['spot'] = spot
		context['gallery'] = gallery
		context['guides'] = guides
		print(guides)

		return render(request, 'home/spot/detail.html', context)

	except ObjectDoesNotExist as e:
		pass

	return HttpResponse('<h1 align="center">Spot not found</h1>')