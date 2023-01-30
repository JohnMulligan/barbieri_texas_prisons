from django.db import models
from place.models import *

class EventType(models.Model):
	name=models.CharField(max_length = 100)
	def __str__(self):
		return str(self.name)

class EventTime(models.Model):
	year=models.IntegerField()
	month=models.IntegerField()
	day=models.IntegerField()
	hour=models.IntegerField()
	minute=models.IntegerField()
	second=models.IntegerField()
	
	def __str__(self):
		mdy=[str(i) for i in [month,day,year] if i is not None]
		if len(mdy)>0:
			mdy=mdy.join('/')
		else:
			mdy=None
		
		hms=[str(i) for i in [hour,minute,second] if i is not None]
		if len(mdy)>0:
			hms=hms.join(':')
		else:
			hms=None
		
		fulldate=[i for i in [mdy,hms] if i is not None]
		if len(fulldate)>0:
			fulldate=fulldate.join(' ')
		else:
			fulldate=None
		
		return fulldate
	
class Event(models.Model):
	date_time=models.ForeignKey(EventTime,null=True,on_delete=models.CASCADE)
	place=models.ForeignKey(Place,null=True,on_delete=models.CASCADE)
	type=models.ForeignKey(EventType,null=True,on_delete=models.CASCADE)
	def __str__(self):
		return "%s"
	class Meta:
		abstract=True
