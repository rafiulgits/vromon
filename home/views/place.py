from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, HttpResponse
from home.forms import ReviewCommentForm
from home.models import Place, ReviewComment

def single(request, uid):

	try:
		context = {}
		place = Place.objects.get(id=uid)
		comments = ReviewComment.objects.filter(for_model='P')

		context['place'] = place
		context['comments'] = comments

		if request.user.is_authenticated:
			form = ReviewCommentForm()
			context['form'] = form

			if request.method == 'POST':
				pass

		return render(request, 'home/place/single.html', context)

	except ObjectDoesNotExist as e:
		pass
	return HttpResponse('request not found')


def all(request):
	places = Place.objects.all()
	context = {}
	context['places'] = places

	return render(request, 'home/place/all.html', context)