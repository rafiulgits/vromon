from account.models import Account,GuideProfile

from django.db import models

from uuid import uuid4


class Spot(models.Model):
	uid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	description = models.TextField()



class SpotGallery(models.Model):
	uid = models.UUIDField(default=uuid4, primary_key=True)
	path = models.TextField()
	spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now=True)



class SpotComment(models.Model):
	uid = models.UUIDField(default=uuid4, primary_key=True)
	body = models.TextField()
	spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now=True)



class SpotGuide(models.Model):
	uid = models.AutoField(primary_key=True)
	guide = models.ForeignKey(GuideProfile, on_delete=models.CASCADE)
	spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
	details = models.TextField()



class SpotGuideMedia(models.Model):
	uid = models.UUIDField(default=uuid4, primary_key=True)
	path = models.TextField()
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