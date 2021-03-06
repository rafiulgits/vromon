from django.urls import path
from home.views import index, hotel, place, restaurant
from tourguide.views import spot, guide, event

urlpatterns = [
    path('', index.view, name='home'),

    path('hotel/all/', hotel.all, name='all-hotel'),
    path('hotel/<uid>/', hotel.single, name='single-hotel'),

    path('place/all/', place.all, name='all-place'),
    path('place/<uid>/', place.single, name='single-place'),

    path('restaurant/all/', restaurant.all, name='all-restaurant'),
    path('restaurant/<uid>/', restaurant.single, name='single-restaurant'),

    path('explore/', spot.list, name='spot-list'),
	path('spot/<name>/', spot.detail, name='spot-detail'),

	path('event/create/', event.create, name='event-create'),
	path('event/all/', event.list, name='event-list'),
	path('event/<uid>/', event.detail, name='event-detail'),


	path('guide/join/', guide.join, name='guide-join'),
	path('guide/update/', guide.update, name='guide-update'),
	path('guide/<uid>/', guide.dashboard, name='guide-dashboard'),
	path('guide/<uid>/create-spot-page/', guide.new_page, name='new-page'),
	path('guide/<uid>/spot/<name>/', guide.page, name='page'),
	path('guide/<uid>/spot/<name>/update/', guide.page_update, name='page-update'),
	path('guide/<uid>/spot/<name>/upload-image/', guide.upload_image)

]