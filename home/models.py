from django.db import models

# Create your models here.

_GENDER = (
	('F', 'Female'),
	('M', 'Male'),
	('O', 'Other')
)

class Account(models.Model):
	pass


class TouristProfile(models.Model):
	phone = models.CharField(max_lenngth=12, primary_key=True)
	email = models.EmailField(max_lenngth=80)
	name = models.CharField(max_lenngth=30)
	gender = models.CharField(max_lenngth=1, choices=_GENDER)


class GuideProfile(models.Model):
	phone = models.CharField(max_lenngth=12, primary_key=True)
	email = models.EmailField(max_lenngth=80)
	name = models.CharField(max_lenngth=30)
	gender = models.CharField(max_lenngth=1, choices=_GENDER)
	description = models.TextField()
	rating = models.PositiveIntegerField(default=0)


class Spot(models.Model):
	uid = models.CharField(max_lenngth=32, primary_key=True)
	name = models.CharField(max_lenngth=30)
	location = models.TextField()



class SpotMedia(models.Model):
	uid = models.CharField(max_lenngth=32, primary_key=True)
	path = models.TextField()
	spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now=True)




class SpotGuid(models.Model):
	uid = models.CharField(max_lenngth=32, primary_key=True)
	guide = models.ForeignKey(GuideProfile, on_delete=models.CASCADE)
	spot = models.ForeignKey(Spot, on_delete=models.CASCADE)