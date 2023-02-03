from django.db import models

class Place(models.Model):
	name=models.CharField(max_length = 100,null=True,blank=True)
	latitude=models.FloatField(null=True,blank=True)
	longitude=models.FloatField(null=True,blank=True)
	bounds=models.JSONField(null=True,blank=True)
	def __str__(self):
		return self.name or "None"
