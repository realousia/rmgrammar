from django.db import models

# Create your models here.
class Ramyeon(models.Model):
	name = models.CharField(max_length=64)
	company = models.CharField(max_length=64)
	sort = models.CharField(max_length=10)
	size = models.IntegerField(default=0)
	calories = models.IntegerField(default=0)
