from django.db import models

class Place(models.Model):
	name=models.CharField(max_length = 100)
	latitude=models.FloatField()
	longitude=models.FloatField()
	bounds=models.JSONField()
	def __str__(self):
		return str(person.name)
