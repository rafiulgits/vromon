from django import forms
from generic.media import Image
from generic.variables import IMAGE_DIR
from home.models import (SpotComment , Event , EventComment,SpotGuide,
	SpotGuideMedia)

class SpotCommentForm(forms.ModelForm):

	class Meta:
		model = SpotComment
		fields = ["body"]

		widgets = {
			"body": forms.TextInput(attrs={'placeholder':'giver your comment'})
		}


	def save(self, commit=True):
		spot_comment = super(SpotCommentForm, self).save(commit=False)
		spot_comment.user = self.user
		spot_comment.spot = self.spot
		if commit:
			spot_comment.save()

		return spot_comment


	def __init__(self, *args, **kwargs):
		self.spot = kwargs.pop('spot', None)
		self.user = kwargs.pop('user', None)
		super(SpotCommentForm, self).__init__(*args, **kwargs)



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


	def save(self, commit=True):
		event = super(EventForm, self).save(commit=False)
		event.organizer = self.organizer
		if commit:
			event.save()
		return event


	def __init__(self, *args, **kwargs):
		self.organizer = kwargs.pop('organizer', None)
		super(EventForm, self).__init__(*args, **kwargs)



class EventCommentForm(forms.ModelForm):
	class Meta:
		model = EventComment
		fields = [
			"body"
		]

		widgets = {
			"body": forms.TextInput(attrs={'placeholder':'giver your comment'})
		}



	def save(self, commit=True):
		event_comment = super(EventCommentForm, self).save(commit=False)
		event_comment.user = self.user
		event_comment.event = self.event
		if commit:
			event_comment.save()
		return event_comment



	def  __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		self.event = kwargs.pop('event', None)
		super(EventCommentForm, self).__init__(*args, **kwargs)



class SpotGuideForm(models.ModelForm):

	class Meta:
		model = SpotGuide
		fields = ['spot', 'detail', 'logo']

		widgets = {
			'spot' : forms.Select(attrs={
				'class' : ''
				}),

			'detail' : forms.TextInput(attrs={
				'class' : ''
				}),

			'logo' : forms.FileInput(attrs={
				'class' : ''
				})
		}


	def save(self, commit=True):
		spot_guide = super(SpotGuideForm, self).save(commit=False)
		if commit:
			spot_guide.guide = self.guide
			spot_guide.save()

		return spot_guide


	def __init__(self, *args, **kwargs):
		self.guide = kwargs.pop('guide', None)
		super(SpotGuideForm, self).__init__(*args, **kwargs)


class SpotGuideMediaForm(model.ModelForm):
	class Meta:
		model = SpotGuideMedia
		fields = ['image']

		widgets = {
			'image' : forms.FileInput(attrs={
				'class' : ''
			})
		}


	def save(self, commit=True):
		spot_guide_media = super(SpotGuideMediaForm, self).save(commit=False)
		spot_guide_media.spot_guide = self.spot_guide

		if commit:
			spot_guide_media.save()
		return spot_guide_media


	def __init__(self, *args, **kwargs):
		self.spot_guide = kwargs.pop('spot_guide', None)
		super(SpotGuideMediaForm, self).__init__(*args, **kwargs)