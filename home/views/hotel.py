from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, HttpResponse

from home.forms import ReviewCommentForm
from home.models import Hotel,ReviewComment

def single(request, uid):
	try:
		context = {}
		hotel = Hotel.objects.get(id=uid)
		comments = ReviewComment.objects.filter(for_model = 'H')

		context['rating'] = float(hotel.total_rating/hotel.total_rated)
		context['hotel'] = hotel
		context['comments'] = comments

		if request.user.is_authenticated:

			if request.method == 'POST':
				pass

			form = ReviewCommentForm()
			context['form'] = form

		return render(request, 'home/hotel/single.html', context)

	except ObjectDoesNotExist as e:
		pass

	return HttpResponse('request not found')
	


def all(request):
	context = {}
	hotels = Hotel.objects.all()
	context['hotels'] = hotels
	return render(request, 'home/hotel/all.html', context)