from rest_framework.serializers import ModelSerializer
from home.models import Hotel, Restaurant, Place


class HotelSerializer(ModelSerializer):
	class Meta:
		model = Hotel
		fields = ('__all__')



class RestaurantSerializer(ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ('__all__')



class PlaceSerializer(ModelSerializer):
	class Meta:
		model = Place
		fields = ('__all__')