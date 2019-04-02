from account.models import Account
from django.db import models
from generic.variables import IMAGE_DIR
from uuid import uuid4


class Spot(models.Model):
	uid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	district = models.CharField(max_length=20)
	description = models.TextField()
	logo = models.ImageField(upload_to=IMAGE_DIR)

	def __str__(self):
		return self.name



class SpotGallery(models.Model):
	uid = models.UUIDField(default=uuid4, primary_key=True)
	image = models.ImageField(upload_to=IMAGE_DIR)
	spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now=True)



class SpotComment(models.Model):
	uid = models.UUIDField(default=uuid4, primary_key=True)
	body = models.TextField()
	spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now=True)



class GuideProfile(models.Model):
	uid = models.UUIDField(primary_key=True, default=uuid4)
	account = models.OneToOneField(Account, on_delete=models.CASCADE)
	description = models.TextField()
	rating = models.PositiveIntegerField(default=0)


class SpotGuide(models.Model):
	uid = models.AutoField(primary_key=True)
	guide = models.ForeignKey(GuideProfile, on_delete=models.CASCADE)
	spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
	details = models.TextField()
	logo = models.ImageField(upload_to=IMAGE_DIR)



class SpotGuideMedia(models.Model):
	uid = models.UUIDField(default=uuid4, primary_key=True)
	image = models.ImageField(upload_to=IMAGE_DIR)
	spot_guide = models.ForeignKey(SpotGuide, on_delete=models.CASCADE)



class Event(models.Model):
	uid = models.AutoField(primary_key=True)
	title = models.CharField(max_length=50)
	description = models.TextField()
	organizer = models.ForeignKey(Account, on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)



class EventComment(models.Model):
	uid = models.UUIDField(default=uuid4, primary_key=True)
	body = models.TextField()
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now=True)