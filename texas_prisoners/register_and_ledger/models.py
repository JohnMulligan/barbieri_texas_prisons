from django.db import models
from person.models import *
from event.models import *
from place.models import *

class Pardon(Event):
	conviction=models.ForeignKey('Conviction',null=True,on_delete=models.CASCADE,related_name='pardon')
	pardoner=models.ForeignKey(Person,null=True,on_delete=models.CASCADE,related_name='pardon')

class Conviction(models.Model):
	place=models.ForeignKey(Place,on_delete=models.CASCADE,related_name='conviction_place')
	time=models.ForeignKey(EventTime,null=True,on_delete=models.CASCADE,related_name='conviction_time')
	place_of_residence=models.ForeignKey(Place,null=True,on_delete=models.CASCADE,related_name='residence')
	complexion=models.ForeignKey('RacialCategory',null=True,on_delete=models.CASCADE)
	marital_relations=models.ForeignKey('MaritalCategory',null=True,on_delete=models.CASCADE) 
	offence=models.ForeignKey('OffenceCategory',null=True,on_delete=models.CASCADE)
	term=models.FloatField()
	expires=models.ForeignKey(EventTime,null=True,on_delete=models.CASCADE,related_name='conviction_expires')
	pardons=models.ManyToManyField(Pardon,null=True,related_name='parents')
	convict_record=models.ForeignKey('ConvictRecord',null=True,on_delete=models.CASCADE,related_name='conviction')
	occupation=models.ForeignKey('OccupationalCategory',null=True,on_delete=models.CASCADE,related_name='conviction')
	def __str__(self):
		return str(convict.person.name)

class OffenceCategory(models.Model):
	name=models.CharField(max_length = 100)
	def __str__(self):
		return str(name)
class OccupationalCategory(models.Model):
	name=models.CharField(max_length = 100)
	def __str__(self):
		return str(name)

class MaritalCategory(models.Model):
	name=models.CharField(max_length = 100)
	def __str__(self):
		return str(name)

class RacialCategory(models.Model):
	name=models.CharField(max_length = 100)
	def __str__(self):
		return str(name)

class Birth(Event):
	notes=models.TextField()

class Death(Event):
	participants=models.ManyToManyField(Person,null=True,related_name='parents')
	notes=models.TextField()

class Transfer(Event):
	number=models.IntegerField()

class Death(Event):
	cause=models.CharField(max_length = 100)
	killed=models.BooleanField(null=True)
	suicide=models.BooleanField(null=True)
	disease=models.BooleanField(null=True)
	def __str__(self):
		return str(cause)

class Hospitalization(Event):
	cause=models.CharField(max_length = 100)
	convict_record=models.ForeignKey('ConvictRecord',null=True,on_delete=models.CASCADE,related_name='hospitalization')

class PunishmentMethod(models.Model):
	name=models.CharField(max_length = 100)
	def __str__(self):
		return str(name)

class Punishment(Event):
	prison=models.ForeignKey(Place,on_delete=models.CASCADE,related_name='punishment_prison')
	lessee=models.ForeignKey(Person,on_delete=models.CASCADE)
	method=models.ManyToManyField(PunishmentMethod,null=True,related_name='punishment_method')
	duration_in_days=models.IntegerField()
	reason=models.CharField(max_length = 100)
	note=models.TextField()
	convict_record=models.ForeignKey('ConvictRecord',null=True,on_delete=models.CASCADE,related_name='punishment')
	
class SelfMutilation(Event):
	def __str__(self):
		return str(self.type)

class Return(Event):
	new_conviction=models.BooleanField(null=True)
	number=models.IntegerField()
	parole_violation=models.BooleanField(null=True)
	new_term=models.BooleanField(null=True)
	outcome=models.CharField(max_length = 100)

class WorkType(models.Model):
	name=models.CharField(max_length = 100)
	def __str__(self):
		return str(name)

class Company(models.Model):
	name=models.CharField(max_length = 100)
	def __str__(self):
		return str(name)

class Lease(models.Model):
	start_date=models.ForeignKey(EventTime,null=True,on_delete=models.CASCADE,related_name='lease_start_date')
	end_date=models.ForeignKey(EventTime,null=True,on_delete=models.CASCADE,related_name='lease_end_date')
	number_days=models.IntegerField()
	where_after=models.ForeignKey(Place,null=True,on_delete=models.CASCADE)
	convict=models.ForeignKey('Convict',null=True,on_delete=models.CASCADE,related_name="convict_lease")
	lessee=models.ForeignKey(Company,null=True,on_delete=models.CASCADE,related_name="lessee_lease")
	convict_record=models.ForeignKey('ConvictRecord',null=True,on_delete=models.CASCADE,related_name='lease')
	
class WorkForPrison(models.Model):
	work_type=models.ForeignKey(WorkType,null=True,on_delete=models.CASCADE)
	convict_record=models.ForeignKey('ConvictRecord',null=True,on_delete=models.CASCADE,related_name='work_for_prison')
	
class Escape(Event):
	trusty=models.BooleanField(null=True)
	wounded=models.BooleanField(null=True)
	recaptured=models.BooleanField(null=True)
	surrender=models.BooleanField(null=True)
	returned=models.BooleanField(null=True)
	same_day=models.BooleanField(null=True)
	convict_record=models.ForeignKey('ConvictRecord',null=True,on_delete=models.CASCADE,related_name='escape')
	
class Convict(Person):
	person=models.ForeignKey('Convict',on_delete=models.CASCADE)
	def __str__(self):
		return str(person.name)

class ConvictRecord(models.Model):
	person=models.ForeignKey(Person,on_delete=models.CASCADE)
	convict_numer=models.IntegerField()
	birth=models.ForeignKey(Birth,null=True,on_delete=models.CASCADE)
	death=models.ForeignKey(Death,null=True,on_delete=models.CASCADE)
	name=models.CharField(max_length = 200)
	record_date=models.ForeignKey(EventTime,null=True,on_delete=models.CASCADE)
	def __str__(self):
		return str(person.name)