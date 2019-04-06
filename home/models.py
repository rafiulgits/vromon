from account.models import Account
from django.db import models
from uuid import uuid4

_REVIEW_MODEL = (
	('R', "Restaurant"),
	('H', "Hotel"),
	('P', "Place"),
)



class Restaurant(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	geo_longitude = models.DecimalField(max_digits=8, decimal_places=3)
	geo_latitude = models.DecimalField(max_digits=8, decimal_places=3)
	address = models.TextField()
	avg_rating = models.SmallIntegerField(default=0)
	total_rated = models.IntegerField(default=0)


class Hotel(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	geo_longitude = models.DecimalField(max_digits=8, decimal_places=3)
	geo_latitude = models.DecimalField(max_digits=8, decimal_places=3)
	address = models.TextField()
	avg_rating = models.SmallIntegerField(default=0)
	total_rated = models.IntegerField(default=0)
	avg_price = models.CharField(max_length=12)


class Place(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	geo_longitude = models.DecimalField(max_digits=8, decimal_places=3)
	geo_latitude = models.DecimalField(max_digits=8, decimal_places=3)
	address = models.TextField()
	avg_rating = models.SmallIntegerField(default=0)
	total_rated = models.IntegerField(default=0)



class ReviewComment(models.Model):
	uid = models.UUIDField(primary_key=True, default=uuid4)
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	body = models.TextField()
	for_model = models.CharField(max_length=1, choices=_REVIEW_MODEL)
	date_time = models.DateTimeField(auto_now_add=True)