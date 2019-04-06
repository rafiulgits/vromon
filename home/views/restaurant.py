from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, HttpResponse

from home.forms import ReviewCommentForm
from home.models import Restaurant, ReviewComment


def single(request, uid):
	try:
		context = {}
		restaurant = Restaurant.objects.get(id=uid)
		comments = ReviewComment.objects.filter(for_model='R')

		context['restaurant'] = restaurant
		context['comments'] = comments

		if request.user.is_authenticated:

			if request.method == 'POST':
				form = ReviewCommentForm(request.POST,user=request.user,for_model='H')
				if form.is_valid():
					form.save()
					return redirect('/hotel/'+str(uid)+'/')

			form = ReviewCommentForm()
			context['form'] = form

		return render(request, 'home/restaurant/single.html', context)

	except ObjectDoesNotExist as e:
		pass
	return HttpResponse('request not found')


def all(request):
	context = {}
	restaurants = Restaurant.objects.all()
	context['restaurants'] = restaurants

	return render(request, 'home/restaurant/all.html', context)