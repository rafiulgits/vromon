from django.urls import path
from home.views import event, index, spot

urlpatterns = [
    path('', index.view, name='home'),

    path('explore/', spot.list, name='spot-list'),
    path('spot/<name>/', spot.detail, name='spot-detail'),


    path('event/create/', event.create, name='event-create'),
    path('event/all/', event.list, name='event-list'),
    path('event/<uid>/', event.detail, name='event-detail'),
]