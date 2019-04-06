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
	geo_long = models.CharField(max_length=10)
	geo_lat = models.CharField(max_length=10)
	address = models.CharField(max_length=30)
	total_rating = models.PositiveIntegerField(default=0)
	total_rated = models.PositiveIntegerField(default=0)
	image = models.ImageField(upload_to='images/')


class Hotel(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	geo_long = models.CharField(max_length=10)
	geo_lat = models.CharField(max_length=10)
	address = models.CharField(max_length=30)
	avg_rating = models.SmallIntegerField(default=0)
	total_rating = models.PositiveIntegerField(default=0)
	total_rated = models.PositiveIntegerField(default=0)
	image = models.ImageField(upload_to='images/')


class Place(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	geo_long = models.CharField(max_length=10)
	geo_lat = models.CharField(max_length=10)
	address = models.CharField(max_length=30)
	total_rating = models.PositiveIntegerField(default=0)
	total_rated = models.PositiveIntegerField(default=0)
	image = models.ImageField(upload_to='images/')



class ReviewComment(models.Model):
	uid = models.UUIDField(primary_key=True, default=uuid4)
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	body = models.TextField()
	for_model = models.CharField(max_length=1, choices=_REVIEW_MODEL)
	date_time = models.DateTimeField(auto_now_add=True)