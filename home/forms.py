from django import forms

from generic.variables import IMAGE_DIR
from home.models import ReviewComment


class ReviewCommentForm(forms.ModelForm):
	class Meta:
		model = ReviewComment
		fields = ['body']

	def save(self, commit=True):
		comment = super(ReviewCommentForm, self).save(commit=False)
		comment.user = self.user
		comment.for_model = self.for_model

		if commit:
			comment.save()
		return comment


	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		self.for_model = kwargs.pop('for_model', None)

		super(ReviewCommentForm, self).__init__(*args, *kwargs)
