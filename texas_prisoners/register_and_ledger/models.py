from django.db import models
from person.models import *
from event.models import *
from place.models import *

class Pardon(Event):
	conviction=models.ForeignKey('Conviction',null=True,blank=True,on_delete=models.CASCADE,related_name='pardon')
	pardoner=models.ForeignKey(Person,null=True,blank=True,on_delete=models.CASCADE,related_name='pardon')

class Conviction(models.Model):
	place=models.ForeignKey(Place,null=True,blank=True,on_delete=models.CASCADE,related_name='conviction_place')
	time=models.ForeignKey(EventTime,null=True,blank=True,on_delete=models.CASCADE,related_name='conviction_time')
	place_of_residence=models.ForeignKey(Place,null=True,blank=True,on_delete=models.CASCADE,related_name='residence')
	complexion=models.ForeignKey('RacialCategory',null=True,blank=True,on_delete=models.CASCADE)
	marital_relations=models.ForeignKey('MaritalCategory',null=True,blank=True,on_delete=models.CASCADE) 
	offence=models.ForeignKey('OffenceCategory',null=True,blank=True,on_delete=models.CASCADE)
	term=models.FloatField()
	expires=models.ForeignKey(EventTime,null=True,blank=True,on_delete=models.CASCADE,related_name='conviction_expires')
	pardons=models.ManyToManyField(Pardon,null=True,blank=True,related_name='parents')
	convict_record=models.ForeignKey('ConvictRecord',null=True,blank=True,on_delete=models.CASCADE,related_name='conviction')
	occupation=models.ForeignKey('OccupationalCategory',null=True,blank=True,on_delete=models.CASCADE,related_name='conviction')
	def __str__(self):
		return str(self.convict.person.name) or "None"

class OffenceCategory(models.Model):
	name=models.CharField(max_length = 100)
	def __str__(self):
		return str(self.name) or "None"
class OccupationalCategory(models.Model):
	name=models.CharField(max_length = 100)
	def __str__(self):
		return str(self.name) or "None"

class MaritalCategory(models.Model):
	name=models.CharField(max_length = 100)
	def __str__(self):
		return str(self.name) or "None"

class RacialCategory(models.Model):
	name=models.CharField(max_length = 100)
	def __str__(self):
		return str(self.name) or "None"

class Birth(Event):
	notes=models.TextField(null=True,blank=True)
	birth_parents=models.ManyToManyField(Person,null=True,blank=True,related_name='parents')

class Transfer(Event):
	number=models.IntegerField(null=True,blank=True)

class Death(Event):
	cause=models.CharField(max_length = 100,null=True,blank=True)
	killed=models.BooleanField(null=True,blank=True)
	suicide=models.BooleanField(null=True,blank=True)
	disease=models.BooleanField(null=True,blank=True)

class Hospitalization(Event):
	cause=models.CharField(max_length = 100,null=True,blank=True)
	convict_record=models.ForeignKey('ConvictRecord',null=True,blank=True,on_delete=models.CASCADE,related_name='hospitalization')

class PunishmentMethod(models.Model):
	name=models.CharField(max_length = 100,null=True,blank=True)
	def __str__(self):
		return str(self.name) or "None"

class Punishment(Event):
	prison=models.ForeignKey(Place,null=True,blank=True,on_delete=models.CASCADE,related_name='punishment_prison')
	lessee=models.ForeignKey(Person,null=True,blank=True,on_delete=models.CASCADE)
	method=models.ManyToManyField(PunishmentMethod,null=True,blank=True,related_name='punishment_method')
	duration_in_days=models.IntegerField(null=True,blank=True)
	reason=models.CharField(max_length = 100,null=True,blank=True)
	note=models.TextField(null=True,blank=True)
	convict_record=models.ForeignKey('ConvictRecord',null=True,blank=True,on_delete=models.CASCADE,related_name='punishment')
	
class SelfMutilation(Event):
	def __str__(self):
		return str(self.type)

class Return(Event):
	new_conviction=models.BooleanField(null=True,blank=True)
	number=models.IntegerField(null=True,blank=True)
	parole_violation=models.BooleanField(null=True,blank=True)
	new_term=models.BooleanField(null=True,blank=True)
	outcome=models.CharField(max_length = 100)

class WorkType(models.Model):
	name=models.CharField(max_length = 100)
	def __str__(self):
		return str(self.name) or "None"

class Company(models.Model):
	name=models.CharField(max_length = 100)
	def __str__(self):
		return str(self.name) or "None"

class Lease(models.Model):
	start_date=models.ForeignKey(EventTime,null=True,blank=True,on_delete=models.CASCADE,related_name='lease_start_date')
	end_date=models.ForeignKey(EventTime,null=True,blank=True,on_delete=models.CASCADE,related_name='lease_end_date')
	number_days=models.IntegerField()
	where_after=models.ForeignKey(Place,null=True,blank=True,on_delete=models.CASCADE)
	convict=models.ForeignKey('Convict',null=True,blank=True,on_delete=models.CASCADE,related_name="convict_lease")
	lessee=models.ForeignKey(Company,null=True,blank=True,on_delete=models.CASCADE,related_name="lessee_lease")
	convict_record=models.ForeignKey('ConvictRecord',null=True,blank=True,on_delete=models.CASCADE,related_name='lease')
	
class WorkForPrison(models.Model):
	work_type=models.ForeignKey(WorkType,null=True,blank=True,on_delete=models.CASCADE)
	convict_record=models.ForeignKey('ConvictRecord',null=True,blank=True,on_delete=models.CASCADE,related_name='work_for_prison')
	
class Escape(Event):
	trusty=models.BooleanField(null=True,blank=True)
	wounded=models.BooleanField(null=True,blank=True)
	recaptured=models.BooleanField(null=True,blank=True)
	surrender=models.BooleanField(null=True,blank=True)
	returned=models.BooleanField(null=True,blank=True)
	same_day=models.BooleanField(null=True,blank=True)
	convict_record=models.ForeignKey('ConvictRecord',null=True,blank=True,on_delete=models.CASCADE,related_name='escape')
	
class Convict(Person):
	person=models.ForeignKey('Convict',null=True,blank=True,on_delete=models.CASCADE)
	def __str__(self):
		return str(person.name) or "None"

class ConvictRecord(models.Model):
	person=models.ForeignKey(Person,null=True,blank=True,on_delete=models.CASCADE)
	convict_numer=models.IntegerField(null=True,blank=True)
	birth=models.ForeignKey(Birth,null=True,blank=True,on_delete=models.CASCADE)
	death=models.ForeignKey(Death,null=True,blank=True,on_delete=models.CASCADE)
	name=models.CharField(max_length = 200,null=True,blank=True)
	record_date=models.ForeignKey(EventTime,null=True,blank=True,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.person.name) or "None"