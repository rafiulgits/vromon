from api.serializer import HotelSerializer, PlaceSerializer, RestaurantSerializer
from home.models import Hotel, Place, Restaurant

from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response


@api_view(['GET'])
def nearby_hotel(request, format=None):
	lat = request.GET.get('lat', None)
	lng = request.GET.get('lng', None)

	if lat is None or lng is None:
		raise NotFound('request not found')


	query = Hotel.objects.all()
	serializer = HotelSerializer(query, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def nearby_restaurant(request, format=None):
	lat = request.GET.get('lat', None)
	lng = request.GET.get('lng', None)

	if lat is None or lng is None:
		raise NotFound('request not found')

	query = Restaurant.objects.all()
	serializer = RestaurantSerializer(query, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def nearby_place(request, format=None):
	lat = request.GET.get('lat', None)
	lng = request.GET.get('lng', None)

	if lat is None or lng is None:
		raise NotFound('request not found')


	query = Place.objects.all()
	serializer = PlaceSerializer(query, many=True)
	return Response(serializer.data)
