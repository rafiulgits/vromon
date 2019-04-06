from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, HttpResponse

from home.forms import ReviewCommentForm
from home.models import Hotel,ReviewComment

def single(request, uid):
	try:
		context = {}
		hotel = Hotel.objects.get(id=uid)
		comments = ReviewComment.objects.filter(for_model = 'H')

		if hotel.total_rated != 0:
			context['rating'] = float(hotel.total_rating/hotel.total_rated)
		else:
			context['rating'] = 0

		context['hotel'] = hotel
		context['comments'] = comments

		if request.user.is_authenticated:

			if request.method == 'POST':
				form = ReviewCommentForm(request.POST,user=request.user,for_model='H')
				if form.is_valid():
					form.save()
					return redirect('/hotel/'+str(uid)+'/')

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