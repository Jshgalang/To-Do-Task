from django.db import models


class Item(models.Model):
	text = models.TextField(default="")
	list = models.ForeignKey('List', default=None) # added to clear error 4


class List(models.Model):
	pass

# Create your models here.
