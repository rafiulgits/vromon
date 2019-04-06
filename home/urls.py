from django.urls import path
from home.views import index, hotel, place, restaurant

urlpatterns = [
    path('', index.view, name='home'),

    path('hotel/all/', hotel.all, name='all-hotel'),
    path('hotel/<uid>/', hotel.single, name='single-hotel'),

    path('place/all/', place.all, name='all-place'),
    path('place/<uid>/', place.single, name='single-place'),

    path('restaurant/all/', restaurant.all, name='all-restaurant'),
    path('restaurant/<uid>', restaurant.single, name='single-restaurant'),

]