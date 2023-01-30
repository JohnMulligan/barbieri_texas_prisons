from django.contrib import admin
from person.models import *

class PersonAdmin(admin.ModelAdmin):
	model=Person

admin.site.register(Person,PersonAdmin)