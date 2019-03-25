from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager,PermissionsMixin, 
	_user_has_module_perms, _user_has_perm, _user_get_all_permissions)

from django.contrib.auth import get_backends
from django.db import models

# Create your models here.

_GENDER = (
	('F', 'Female'),
	('M', 'Male'),
	('O', 'Other')
)

class UserManager(BaseUserManager):
	def create_user(self,phone,password=None,name=None,email=None, gender=None,
		is_staff=False,is_admin=False):

		if not password:
			raise ValueError('password needed')
		if not name:
			raise ValueError('name needed')
		if not email:
			raise ValueError('email needed')

		if not gender:
			raise ValueError('gender needed')

		user = self.model(phone=phone)
		user.name = name
		user.email = email
		user.gender = gender
		user.is_admin = is_admin
		user.is_staff = is_staff
		user.set_password(password)
		user.save(self._db)
		return user

	def create_staffuser(self, phone, password, name, email, gender):
		"""
		to create custom permission level user
		"""
		if not phone or password:
			raise ValueError('must have the userid and password')
		if not name:
			raise ValueError('name needed')
		if not email:
			raise ValueError('email needed')
		if not gender:
			raise ValueError('gender needed')


		user = self.create_user(phone, password, name, email, gender, True,False)
		return user

	def create_superuser(self, phone, password, name, email, gender):
		"""
		to create an admin
		"""
		if not phone or not password:
			raise ValueError('must have a phone and password')
		if not name:
			raise ValueError('name needed')
		if not email:
			raise ValueError('email needed')
		if not gender:
			raise ValueError('gender needed')


		user = self.create_user(phone, password, name, email, gender, True, True)
		return user




class Account(AbstractBaseUser,PermissionsMixin):
	phone = models.CharField(max_length=12, primary_key=True)
	email = models.EmailField(max_length=80)
	name = models.CharField(max_length=30)
	gender = models.CharField(max_length=1, choices=_GENDER)

	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)

	objects = UserManager()
	USERNAME_FIELD = 'phone'
	REQUIRED_FIELDS = ['email', 'name', 'gender']

	def has_perm(self, perm, obj=None):
		if self.is_admin:
			return True
		return _user_has_perm(self, perm, obj)

	def has_perms(self, perm_list, obj=None):
		return all(self.has_perm(perm, obj) for perm in perm_list)

	def has_module_perms(self, app_label):
		if self.is_admin or self.is_staff:
			return True
		return False

	def get_username(self):
		return self.userid


class GuideProfile(models.Model):
	account = models.OneToOneField(Account, primary_key=True, on_delete=models.CASCADE)
	description = models.TextField()
	rating = models.PositiveIntegerField(default=0)


class Spot(models.Model):
	uid = models.CharField(max_length=32, primary_key=True)
	name = models.CharField(max_length=30)
	location = models.TextField()



class SpotMedia(models.Model):
	uid = models.CharField(max_length=32, primary_key=True)
	path = models.TextField()
	spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now=True)




class SpotGuide(models.Model):
	uid = models.CharField(max_length=32, primary_key=True)
	guide = models.ForeignKey(GuideProfile, on_delete=models.CASCADE)
	spot = models.ForeignKey(Spot, on_delete=models.CASCADE)