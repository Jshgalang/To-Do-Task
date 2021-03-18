from django.db import models

# Create your models here.
class Item(models.Model):
	text = models.TextField(default='')
	list = models.ForeignKey('List', default=None)

class List(models.Model): # # research more about the magic in models.Model why it can be instantiated automatically
	pass