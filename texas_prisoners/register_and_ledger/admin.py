from django.contrib import admin
from place.models import *
from person.models import *
from register_and_ledger.models import *
from event.models import *

'''


class Transfer(Event):
	number=models.IntegerField()


	
class SelfMutilation(Event):
	def __str__(self):
		return str(self.type)

class Return(Event):
	new_conviction=models.BooleanField(null=True)
	number=models.IntegerField()
	parole_violation=models.BooleanField(null=True)
	new_term=models.BooleanField(null=True)
	outcome=models.CharField(max_length = 100)


class Lease(models.Model):
	start_date=models.ForeignKey(EventTime,null=True,on_delete=models.CASCADE,related_name='lease_start_date')
	end_date=models.ForeignKey(EventTime,null=True,on_delete=models.CASCADE,related_name='lease_end_date')
	number_days=models.IntegerField()
	where_after=models.ForeignKey(Place,null=True,on_delete=models.CASCADE)
	convict=models.ForeignKey('Convict',null=True,on_delete=models.CASCADE,related_name="convict_lease")
	lessee=models.ForeignKey(Company,null=True,on_delete=models.CASCADE,related_name="lessee_lease")

class WorkForPrison(models.Model):
	work_type=models.ForeignKey(WorkType,null=True,on_delete=models.CASCADE)
	
class Convict(Person):
	person=models.ForeignKey('Convict',on_delete=models.CASCADE)
	def __str__(self):
		return str(person.name)


'''

class CompanyAdmin(admin.ModelAdmin):
	model=Company

class WorkForPrisonAdmin(admin.ModelAdmin):
	model=WorkForPrison

class WorkForPrisonInline(admin.TabularInline):
	model=WorkForPrison
	classes=['collapse']
	extra=0

class LeaseAdmin(admin.ModelAdmin):
	model=Lease

class LeaseInline(admin.TabularInline):
	model=Lease
	exclude=['convict']
	classes=['collapse']
	extra=0

class PardonAdmin(admin.ModelAdmin):
	exclude=['conviction']
	model=Pardon

class EventTypeAdmin(admin.ModelAdmin):
	model=EventType

class EventTimeAdmin(admin.ModelAdmin):
	model=EventTime

class HospitalizationAdmin(admin.ModelAdmin):
	model=Hospitalization

class PunishmentMethodAdmin(admin.ModelAdmin):
	model=PunishmentMethod

class PunishmentAdmin(admin.ModelAdmin):
	model=Punishment
class HospitalizationInline(admin.TabularInline):
	model=Hospitalization
	classes=['collapse']
	extra=0

class PunishmentInline(admin.TabularInline):
	model=Punishment
	classes=['collapse']
	extra=0
class EscapeAdmin(admin.ModelAdmin):
	model=Escape

class OccupationalCategoryAdmin(admin.ModelAdmin):
	model=OccupationalCategory
	
class OffenceCategoryAdmin(admin.ModelAdmin):
	model=OffenceCategory

class RacialCategoryAdmin(admin.ModelAdmin):
	model=RacialCategory

class EscapeInline(admin.TabularInline):
	model=Escape
	classes=['collapse']
	extra=0

class WorkTypeAdmin(admin.ModelAdmin):
	model=WorkType

class DeathAdmin(admin.ModelAdmin):
	model=Death

class BirthAdmin(admin.ModelAdmin):
	model=Birth

class MaritalCategoryAdmin(admin.ModelAdmin):
	model=MaritalCategory

class MaritalCategoryInline(admin.TabularInline):
	model=MaritalCategory
	classes= ['collapse']
	extra=0

class ConvictionInline(admin.TabularInline):
	model=Conviction
	classes= ['collapse']
	extra=0

class ConvictRecordAdmin(admin.ModelAdmin):
	inlines=(
		ConvictionInline,
		EscapeInline,
		PunishmentInline,
		HospitalizationInline,
		LeaseInline,
		WorkForPrisonInline
		
	)
	model=ConvictRecord

admin.site.register(EventType,EventTypeAdmin)
admin.site.register(Pardon,PardonAdmin)
admin.site.register(RacialCategory,RacialCategoryAdmin)
admin.site.register(ConvictRecord,ConvictRecordAdmin)
admin.site.register(MaritalCategory,MaritalCategoryAdmin)
admin.site.register(Birth,BirthAdmin)
admin.site.register(Death,DeathAdmin)
admin.site.register(WorkType,WorkTypeAdmin)
admin.site.register(PunishmentMethod,PunishmentMethodAdmin)
admin.site.register(EventTime,EventTimeAdmin)
admin.site.register(OccupationalCategory,OccupationalCategoryAdmin)
admin.site.register(OffenceCategory,OffenceCategoryAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(WorkForPrison,WorkForPrisonAdmin)