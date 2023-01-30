from django.contrib import admin
from place.models import *

class PlaceAdmin(admin.ModelAdmin):
	model=Place

admin.site.register(Place,PlaceAdmin)