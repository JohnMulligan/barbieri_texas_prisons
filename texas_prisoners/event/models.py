from django.db import models
from place.models import *

class EventType(models.Model):
	name=models.CharField(max_length = 100)
	def __str__(self):
		return str(self.name)

class EventTime(models.Model):
	year=models.IntegerField(null=True,blank=True)
	month=models.IntegerField(null=True,blank=True)
	day=models.IntegerField(null=True,blank=True)
	hour=models.IntegerField(null=True,blank=True)
	minute=models.IntegerField(null=True,blank=True)
	second=models.IntegerField(null=True,blank=True)
	
	def __str__(self):
		mdy=[str(i) for i in [self.month,self.day,self.year] if i is not None]
		if len(mdy)>0:
			mdy='/'.join(mdy)
		else:
			mdy=None
		hms=[str(i) for i in [self.hour,self.minute,self.second] if i is not None]
		if len(mdy)>0:
			hms=":".join(hms)
		else:
			hms=None
		
		fulldate=[i for i in [mdy,hms] if i is not None]
		if len(fulldate)>0:
			fulldate=' '.join(fulldate)
		else:
			fulldate=None
		
		return fulldate
	
class Event(models.Model):
	date_time=models.ForeignKey(EventTime,null=True,blank=True,on_delete=models.CASCADE)
	place=models.ForeignKey(Place,null=True,blank=True,on_delete=models.CASCADE)
	type=models.ForeignKey(EventType,null=True,blank=True,on_delete=models.CASCADE)
	def __str__(self):
		return "%s - %s - %s" %(self.type,self.place,self.date_time)
	class Meta:
		abstract=True
