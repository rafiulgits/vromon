from django.shortcuts import render, redirect , HttpResponse
from tourguide.forms import EventForm , EventCommentForm
from tourguide.models import Event , EventComment


def list(request):
	context = {}
	return render(request, 'home/index.html', context)


def detail(request, uid):
	context = {}
	try:
		event = Event.objects.get(uid=uid)
		all_comment = EventComment.objects.filter(event_id = event.uid).order_by('-date_time')
		if request.method == 'POST':
			form = EventCommentForm(request.POST)
			if form.is_valid():
				comment  = EventComment()
				comment.user= request.user
				comment.event = event
				comment.body = form.cleaned_data['body']
				comment.save()
				print(comment.body)
				return redirect("/event/"+str(event.uid) + "/#comments")



		form = EventCommentForm()
		context['event'] = event
		context['form'] = form
		context['all_comment'] = all_comment
		return render(request, 'home/event/detail.html', context)
	except Exception as e:
		pass

	return HttpResponse("request not found")


def create(request):
	context = {}
	if request.method == "POST":
		form= EventForm(request.POST , organizer=request.user)
		if form.is_valid():
			event = Event()
			event.organizer=request.user
			event.title = form.cleaned_data['title']
			event.description = form.cleaned_data['description']
			event.save()
			return redirect("/event/"+str(event.uid)+"/")


	form = EventForm(organizer=request.user)
	context["form"] = form
	return render(request, 'home/event/create.html', context)