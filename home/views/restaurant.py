from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, HttpResponse

from home.forms import ReviewCommentForm
from home.models import Restaurant


def single(request, uid):
	try:
		context = {}
		restaurant = Restaurant.objects.get(id=uid)
		comments = ReviewComment.objects.filter(for_model='R')

		context['restaurant'] = restaurant
		context['comments'] = comments

		if request.user.is_authenticated:
			form = ReviewCommentForm()
			context['form'] = form

			if request.method == 'POST':
				pass

		return render(request, 'home/restaurant/single.html', context)

	except ObjectDoesNotExist as e:
		pass
	return HttpResponse('request not found')


def all(request):
	context = {}
	restaurants = Restaurant.objects.all()

	return render(request, 'home/restaurant/all.html', context)