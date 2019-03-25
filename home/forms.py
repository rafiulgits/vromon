from django import forms

from generic import Image

from home.models import (Account, GuideProfile, Spot, 
	SpotMedia)


class AccountCreateForm(forms.ModelForm):
	password1 = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ['phone','name','email','gender',]


	def clean_phone(self):
		"""	
		to check the user is already taken or not
		"""
		phone = self.cleaned_data.get('phone')
		query = User.objects.filter(phone=phone)

		if query.exists():
			raise forms.ValidationError('this phone is taken')

		email =  self.cleaned_data.get('email')
		query = User.objects.filter(email=email)

		if query.exists():
			raise forms.ValidationError('Email is taken')

		return phone

	def clean_password2(self):
		"""
		checking two raw passwords and return the password if matched
		"""
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Password don't matched")
		return password2
	


class GuideProfileForm(forms.ModelForm):
	class Meta:
		model = GuideProfile
		fields = ['__all__']



class  SpotMedia(forms.ModelForm):

	file = forms.ImageField(widget=forms.FileInput(attrs={}))
	class Meta:
		model = SpotMedia
		fields = ['']



	def save(self):
		file = self.cleaned_data['file']
		img_src = Image.load(file_stream=file)
