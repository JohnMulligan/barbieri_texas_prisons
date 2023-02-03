from django.db import models
from person.models import *
from event.models import *

class Person(models.Model):
	name=models.CharField(max_length = 200,null=True,blank=True)
	def __str__(self):
		return str(self.name) or "None"
