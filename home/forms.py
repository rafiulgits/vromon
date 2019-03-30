from django import forms
from home.models import SpotComment , Event , EventComment

class SpotCommentForm(forms.ModelForm):

	class Meta:
		model = SpotComment
		fields = ["body"]

		widgets = {
			"body": forms.TextInput(attrs={'placeholder':'giver your comment'})
		}


class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = [
			"title",
			"description"
		]

		widgets={
			"title": forms.TextInput(attrs={'placeholder' : 'event title'}),
			"description" : forms.TextInput(attrs={'placeholder' : 'event description'})
		}

class EventCommentForm(forms.ModelForm):
	class Meta:
		model = EventComment
		fields = [
			"body"
		]

		widgets = {
			"body": forms.TextInput(attrs={'placeholder':'giver your comment'})
		}

