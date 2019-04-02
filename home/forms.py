from django import forms

from generic.variables import IMAGE_DIR
from home.models import (SpotComment , Event , EventComment,SpotGuide,
	SpotGuideMedia, GuideProfile)


class GuideProfileForm(forms.ModelForm):
	class Meta:
		model = GuideProfile
		fields = ['description',]

		widgets = {
			'description' : forms.Textarea(attrs={
				'class' : 'form-control'})
		}


	def save(self, commit=True):
		if self.guide_profile != None:
			self.guide_profile.description = self.cleaned_data['description']
			self.guide_profile.save()
			return self.guide_profile

		guide_profile = super(GuideProfileForm, self).save(commit=False)
		guide_profile.user = self.user
		if commit:
			guide_profile.save()
		return guide_profile



	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		self.guide_profile = kwargs.pop('user', None)

		super(GuideProfileForm, self).__init__(*args, **kwargs)

		if self.guide_profile != None:
			self.fields['description'].initial = self.guide_profile.description




class SpotGuideForm(forms.ModelForm):

	class Meta:
		model = SpotGuide
		fields = ['spot', 'details', 'logo']

		widgets = {
			'spot' : forms.Select(attrs={
				'class' : 'custom-select'
				}),

			'details' : forms.Textarea(attrs={
				'class' : 'form-control'
				}),

			'logo' : forms.FileInput(attrs={
				'class' : 'form-control' ,
				'accept' : '.jpg, .png, .jpeg'
				})
		}


	def clean_spot(self):
		spot = self.cleaned_data['spot']
		query = SpotGuide.objects.filter(spot=spot, guide=self.guide)
		if query.exists():
			raise forms.ValidationError('You already created a page for this spot')

		return spot


	def __init__(self, *args, **kwargs):
		self.guide = kwargs.pop('guide', None)
		super(SpotGuideForm, self).__init__(*args, **kwargs)



# class SpotCommentForm(forms.ModelForm):

# 	class Meta:
# 		model = SpotComment
# 		fields = ["body"]

# 		widgets = {
# 			"body": forms.TextInput(attrs={'placeholder':'giver your comment'})
# 		}


# 	def save(self, commit=True):
# 		spot_comment = super(SpotCommentForm, self).save(commit=False)
# 		spot_comment.user = self.user
# 		spot_comment.spot = self.spot
# 		if commit:
# 			spot_comment.save()

# 		return spot_comment


# 	def __init__(self, *args, **kwargs):
# 		self.spot = kwargs.pop('spot', None)
# 		self.user = kwargs.pop('user', None)
# 		super(SpotCommentForm, self).__init__(*args, **kwargs)



# class EventForm(forms.ModelForm):
# 	class Meta:
# 		model = Event
# 		fields = [
# 			"title",
# 			"description"
# 		]

# 		widgets={
# 			"title": forms.TextInput(attrs={'placeholder' : 'event title'}),
# 			"description" : forms.TextInput(attrs={'placeholder' : 'event description'})
# 		}


# 	def save(self, commit=True):
# 		event = super(EventForm, self).save(commit=False)
# 		event.organizer = self.organizer
# 		if commit:
# 			event.save()
# 		return event


# 	def __init__(self, *args, **kwargs):
# 		self.organizer = kwargs.pop('organizer', None)
# 		super(EventForm, self).__init__(*args, **kwargs)



# class EventCommentForm(forms.ModelForm):
# 	class Meta:
# 		model = EventComment
# 		fields = [
# 			"body"
# 		]

# 		widgets = {
# 			"body": forms.TextInput(attrs={'placeholder':'giver your comment'})
# 		}



# 	def save(self, commit=True):
# 		event_comment = super(EventCommentForm, self).save(commit=False)
# 		event_comment.user = self.user
# 		event_comment.event = self.event
# 		if commit:
# 			event_comment.save()
# 		return event_comment



# 	def  __init__(self, *args, **kwargs):
# 		self.user = kwargs.pop('user', None)
# 		self.event = kwargs.pop('event', None)
# 		super(EventCommentForm, self).__init__(*args, **kwargs)






# class SpotGuideMediaForm(model.ModelForm):
# 	class Meta:
# 		model = SpotGuideMedia
# 		fields = ['image']

# 		widgets = {
# 			'image' : forms.FileInput(attrs={
# 				'class' : ''
# 			})
# 		}


# 	def save(self, commit=True):
# 		spot_guide_media = super(SpotGuideMediaForm, self).save(commit=False)
# 		spot_guide_media.spot_guide = self.spot_guide

# 		if commit:
# 			spot_guide_media.save()
# 		return spot_guide_media

# 		widgets = {
# 			"body": forms.TextInput(attrs={'placeholder':'giver your comment'})
# 		}

# 	def __init__(self, *args, **kwargs):
# 		self.spot_guide = kwargs.pop('spot_guide', None)
# 		super(SpotGuideMediaForm, self).__init__(*args, **kwargs)

