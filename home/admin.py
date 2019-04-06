from django.contrib import admin

# Register your models here.
from home.models import *

admin.site.register(Restaurant)
admin.site.register(Hotel)
admin.site.register(Place)

