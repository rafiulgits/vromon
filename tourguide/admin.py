from django.contrib import admin

# Register your models here.
from tourguide.models import *
admin.site.register(Spot)
admin.site.register(SpotGallery)
admin.site.register(SpotComment)
admin.site.register(GuideProfile)
admin.site.register(SpotGuide)
admin.site.register(SpotGuideMedia)